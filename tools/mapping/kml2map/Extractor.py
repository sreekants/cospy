#!/usr/bin/python
# Filename: Extractor.py
# Description: Extractor for KML files.


from cos.core.utilities.ActiveRecord import ActiveRecord
from xml.etree import ElementTree as ET
import os, uuid, math, sys

from pyproj import CRS, Transformer

class Interpolator:
	def __init__(self, rfrom, rto):
		self.rfrom  = rfrom
		self.rto    = rto
		return
	
	def __call__(self, v):
		return self.rto[0]+ (self.rto[1]-self.rto[0])*(v-self.rfrom[0])/(self.rfrom[1]-self.rfrom[0])
	
class Task:
	def __init__(self, kml_path, csv_dir, csv_file):
		self.kml_path	= kml_path
		self.csv_dir	= csv_dir
		self.csv_file	= csv_file
		self.input		= None
		self.output		= None
		return
	
class Mapper:
	def __init__(self, src, dest, destoffset ):
		self.srcoffset	= 0
		self.destoffset	= destoffset
		self.scale		= Interpolator(src, dest)
		self.range		= dest
		return

	def __str__(self):
		""" Displays the mapper in a string format:
		"""

		return f'scale= {self.scale.rfrom} => {self.scale.rto} offset={self.destoffset}'

class Projection:
	def __init__(self, x, y):
		self.mapx = Mapper( x[0], x[1], x[2] )
		self.mapy = Mapper( y[0], y[1], y[2] )
		return


class Extractor:
	def __init__(self, args):
		self.output = {}

		self.resetdb    = True
	
		# Setup projections
		mapping			= args["mapping"]

		self.proj		= Projection( mapping["x"], mapping["y"] )

		self.zone_number = args["zone"]["number"]
		self.zone_letter = args["zone"]["letter"]
		return

	def get_files(self, path, indir, outdir):
		"""
		Builds a tasklist of all the files to processs.
		Args:
			path (str): Root directory of the files.
			indir (str): Directory containing .kml files.
			outdir (str): Directory where .csv files will be saved.
		"""
		fullpath	= os.path.join( path, indir )
		outdir		= os.path.join(path,outdir)
		files		= []
		for kml_file in os.listdir(fullpath):
			if kml_file.endswith(".kml"):
				kml_path = os.path.join(fullpath, kml_file)
				csv_file = os.path.splitext(kml_file)[0] + ".csv"

				files.append( Task(kml_path, outdir, csv_file) )

		return files

	def latlon_to_utm( self, lat, lon ):
		"""
		Converts latitude and longitude of a position to a defined UTM projection.
		Parameters:
            lat: latitude
            lon: longitude
		Returns:
    		tuple: easting, northing
		"""
		
		# Determine if the zone is in the northern or southern hemisphere
		is_northern = self.zone_letter.upper() >= "N"
		
		# Define the UTM coordinate system based on zone and hemisphere
		utm_crs     = CRS.from_proj4(f"+proj=utm +zone={self.zone_number} +{'north' if is_northern else 'south'} +ellps=WGS84")
		wgs84_crs   = CRS.from_epsg(4326)  # EPSG:4326 for WGS84
		
		# Create a transformer object
		transformer = Transformer.from_crs(wgs84_crs, utm_crs)
		
		# Perform the transformation
		easting, northing = transformer.transform(lat, lon)
		return easting, northing


	def map_to_screen( self, proj, utmlat, utmlong ):
		"""
		maps map coord to screen.

		Args:
			proj (Projection): Scaling projection 
            utmlat (float): Latitude.
            utmlong (float): Longitude.

		Returns:
    		list: A list of tuples containing (longitude, latitude, altitude).
		"""
			
		molong   = utmlong	- proj.mapx.srcoffset
		molat    = utmlat	- proj.mapy.srcoffset
		# return molong, molat
	
		long    = proj.mapx.destoffset + proj.mapx.scale(molong)
		lat     = proj.mapy.destoffset + proj.mapy.scale(molat)
			
		return lat, long

	
	def extract(self, path, indir, outdir):
		"""
		Convert all .kml files in a directory to .csv files in another directory.
		Args:
			path (str): Root directory of the files.
			indir (str): Directory containing .kml files.
			outdir (str): Directory where .csv files will be saved.
		"""

		tasks	= self.get_files(path, indir, outdir)

		# Ensure the output directory exists
		os.makedirs(os.path.join(path,outdir), exist_ok=True)

		self.analyze(tasks)
		self.save(tasks)
		return


	def analyze(self, tasks):
		print( f'Extracting files:')
		points     = [list(), list()]

		# Iterate through all .kml files in the source directory
		for t in tasks:
			print( f'   File: {t.kml_path}')
			t.input		= self.extract_polygons(points, t)

		print( f'\nAnalyzing cartographic data:')
		minx    = min(points[0])
		maxx    = max(points[0])
		miny    = min(points[1])
		maxy    = max(points[1])

		scalex	= Extractor.scale('x', min(points[0]), max(points[0]) )
		scaley	= Extractor.scale('y', min(points[1]), max(points[1]) )

		self.proj.mapx.srcoffset	= scalex[0]
		self.proj.mapy.srcoffset	= scaley[0]

		min_lat, min_lon     = self.map_to_screen(self.proj, minx, miny)
		max_lat, max_lon     = self.map_to_screen(self.proj, maxx, maxy)

		self.proj.mapx.range = (min_lon, max_lon)
		self.proj.mapy.range = (min_lat, max_lat)

		lat, lon    		 = self.map_to_screen(self.proj, scalex[3], scaley[3])
		self.proj.mapy.range = (min_lat, lat)

		print('')
		return


	def extract_polygons( self, points, task ):
		"""
		Extract coordinates from a .kml file.

		Args:
		task (Task): Task to process.

		Returns:
		list: A list of tuples containing (longitude, latitude, altitude).
		"""
		# Parse the .kml file
		tree = ET.parse(task.kml_path)
		root = tree.getroot()


		# Namespace definitions for KML
		namespaces = {'kml': 'http://www.opengis.net/kml/2.2'}

		# Extract all coordinates
		polygons = []
		for placemark in root.findall(".//kml:Placemark", namespaces):
			name = placemark.find(".//kml:name", namespaces)
			if name is None:
				continue
			# Extract the place nme
			place = name.text.strip()
			if not place:
				continue

			print( f'    - {place}')

			coord = placemark.find(".//kml:coordinates", namespaces)
			if coord is None:
				continue

			coord_text = coord.text.strip()
			coord_list = coord_text.split()

			# Collect all coordinates in the required format
			if len(coord_list) == 0:
				continue
			
			# Generate the list of coordinates into a polygon
			polygon	= []
			for c in coord_list:
				lon, lat, *_	= map(float, c.split(','))
				utmlon, utmlat	= self.latlon_to_utm(lat, lon)

				points[0].append(utmlon)
				points[1].append(utmlat)

				polygon.append( (utmlon, utmlat, lon, lat) )

			polygons.append( (place, polygon) )

		return polygons

	def generate( self, task ):
		"""
		Generates polygons from a .kml file.

		Args:
		kml_path (str): Path to the .kml file.

		Returns:
		list: A list of tuples containing (longitude, latitude, altitude).
		"""

		# Create a map of places
		places = {}

		for place, polygon in task.input:
			csv_path	= os.path.join(task.csv_dir, f'{place}.csv' )

			# Build the polygon path description
			coords 	= []
			for coord in polygon:
				lon	= coord[0]
				lat	= coord[1]

				map_lat, map_lon     = self.map_to_screen(self.proj, lat, lon)

				# Format with four digits of precision
				formatted_lon = f"{map_lon:.2f}"
				formatted_lat = f"{(self.proj.mapy.range[1]-map_lat):.2f}"

				coords.append(f"{formatted_lon},{formatted_lat}")

			polypath 		= " ".join(coords)
			places[place]	= polypath

			with open(csv_path, mode='w', newline='') as csvfile:
				csvfile.write( polypath )  # Write all coordinates as a single line


		return places

	def save(self, tasks):
		print( f'Generating maps:')
		print( f'  Mapper(x) : {self.proj.mapx}')
		print( f'  Mapper(y) : {self.proj.mapx}')

		# Iterate through all .kml files in the source directory
		for t in tasks:
			self.output[t.csv_file] = self.generate(t)

		print('')
		return


	def clear(self, path, dbfile):
		if len(path) > 0:
			dbpath  = os.path.join(path, dbfile)
		else:
			dbpath  = path
		
		if self.resetdb == True:
			ActiveRecord.clear(dbpath)

	def dump(self, path, type, dbfile):
		if len(path) > 0:
			dbpath  = os.path.join(path, dbfile)
		else:
			dbpath  = path

		is_first	= True				
		db  		= ActiveRecord.create('', dbpath, 'isohypses')
		polygons	= self.output.values()

		for polygon in polygons:
			for k, v in polygon.items():
				if k.startswith(type) == False:
					continue

				if is_first == True:
					print( f'Writing {type} to {dbfile}:')
					is_first	= False

				print( f'  {k}' )
				
				name 	= Extractor.get_name( type, os.path.splitext(k)[0] )
				guid	= str(uuid.uuid1()).lower()
				depth	= Extractor.get_depth( type, name )
				values = {
					'guid': guid,
					'name': name,
					'type': Extractor.get_type(type, v),
					'path': v,
					Extractor.get_depth_field(type): depth,
					'color': Extractor.get_color(type, depth),
					'visible': 'Y' }
				
				db.add(values)
		return

	@staticmethod
	def get_depth(type:str, name:str):
		if name[0].isdigit() == False:
			return 0
		ndx 		= name.find('-')
		if (ndx <2 ) or (ndx > 4):
			return 0
		
		depth = name[:ndx-1]
		return int(depth)
	
	@staticmethod
	def get_depth_field(type:str):
		return { "land":"height", "sea":"depth", "tss":"depth", "sky":"height"}[type]

	@staticmethod
	def get_color(type:str, depth):
		return { "land":"#3CB371", "sea":"#47B9C6", "tss":"#FFB9C6", "sky":"#47B9C6"}[type]

	@staticmethod
	def get_type(type:str, name):
		return { "land":100000, "sea":100000, "tss":100000, "sky":100000}[type]

	@staticmethod
	def get_name(type:str, name:str):
		if name.startswith(type) == False:
			return name
		
		ndx 	= len(type)
		if name[ndx] == '-':
			ndx	= ndx+1

		return Extractor.uncamelize(name[ndx:])

	@staticmethod
	def uncamelize(s:str):
		if not s:
			return s

		last	= ''
		result	= []
		for n in range(0, len(s)):
			ch	= s[n]

			if ((n != 0) and ch.isupper()) and last.isalpha():
				result.append( ' '+ch )
				continue

			result.append(ch)
			last	= ch

		return ''.join(result)

	@staticmethod
	def base(x):
		log10	= math.log10(x)
		b		= int(log10)
		m		= x/pow(10,b)

		return m, b

	@staticmethod
	def scale(parm, minx, maxx):
		rangex				= maxx-minx
		midx				= minx + rangex/2.0
		mantissax, basex	= Extractor.base(rangex)
		print( f'  Range of data (UTM): {parm} ({minx:.4f} - {maxx:.4f}={rangex:.4f})')

		spread	= math.ceil(mantissax)*pow(10, basex) * 1.2
		result	= ( int(midx - spread/2.0), 
					int(midx + spread/2.0),
					midx, rangex, spread
					)
		
		print( f'    Log: {parm}={mantissax} * 10^{basex}')
		print( f'    Position: {parm}= left {result[0]}, right {result[1]}, mid {int(result[2])}')
		print( f'    Span: range {int(result[3])}, spread {int(result[4])}')
		return result



if __name__ == "__main__":
	print( Extractor.scale('x', 669398.9694 , 675397.4265) )
	print( Extractor.scale('y', 4545463.8699, 4553787.3030) )
	sys.exit(0)

	test = Extractor( {
            "zone":{
                "number":35,
                "letter":"N"
            },
            "mapping":{
				# source range, targe range, start offset
                "x": ( [400,7800],    	[0,1200],   1874000 ),
                "y": ( [12400,22000],   [0,800],   	3280000 )
            }
        })

    # Automate the process
	test.extract("kml", "csv")
