#!/usr/bin/python
# Filename: Extractor.py
# Description: Extractor for KML files.


from cos.core.utilities.ActiveRecord import ActiveRecord
from xml.etree import ElementTree as ET
import os
import uuid

from pyproj import CRS, Transformer

class Interpolator:
	def __init__(self, rfrom, rto):
		self.rfrom  = rfrom
		self.rto    = rto
		return
	
	def __call__(self, v):
		return self.rto[0]+ (self.rto[1]-self.rto[0])*(v-self.rfrom[0])/(self.rfrom[1]-self.rfrom[0])
	
	
class Mapper:
	def __init__(self, mapping):
		self.offset = mapping[2]
		self.soffset = mapping[3]
		self.scale  = Interpolator(mapping[0], mapping[1])
		self.range  = mapping[1]
		return
		

class Extractor:
	def __init__(self, args):
		self.output = {}

		self.resetdb    = True
	
		self.mapx = Mapper( args["mapping"]["x"] )
		self.mapy = Mapper( args["mapping"]["y"] )

		self.zone_number = args["zone"]["number"]
		self.zone_letter = args["zone"]["letter"]
		return


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


	def map_to_screen( self, lat, long ):
		"""
		maps map coord to screen.

		Args:
            lon (float): Longitude.
            lat (float): Latitude.

		Returns:
    		list: A list of tuples containing (longitude, latitude, altitude).
		"""
		
		mlong, mlat = self.latlon_to_utm(lat, long)
		# return mlat, mlong
	
		molong   = mlong - self.mapx.offset
		molat    = mlat - self.mapy.offset
		# return molong, molat
	
		long    = self.mapx.soffset + self.mapx.scale(molong)
		lat     = self.mapy.soffset + self.mapy.scale(molat)
			
		return lat, long



	def save_coordinates_to_csv( self, points, kml_path, output_csv_path ):
		"""
		Extract coordinates from a .kml file.

		Args:
		kml_path (str): Path to the .kml file.

		Returns:
		list: A list of tuples containing (longitude, latitude, altitude).
		"""
		# Parse the .kml file
		tree = ET.parse(kml_path)
		root = tree.getroot()


		# Namespace definitions for KML
		namespaces = {'kml': 'http://www.opengis.net/kml/2.2'}

		# Extract all coordinates
		coords = []
		for placemark in root.findall(".//kml:Placemark", namespaces):
			for coord in placemark.findall(".//kml:coordinates", namespaces):
				coord_text = coord.text.strip()
				coord_list = coord_text.split()
				# Collect all coordinates in the required format
				for c in coord_list:
					lon, lat, *_        = map(float, c.split(','))
					map_lat, map_lon     = self.map_to_screen(lat, lon)
					# Format with four digits of precision
					formatted_lon = f"{map_lon:.2f}"
					formatted_lat = f"{(self.mapy.range[1]-map_lat):.2f}"

					points[0].append(map_lon)
					points[1].append(map_lat)

					coords.append(f"{formatted_lon},{formatted_lat}")

			polypath = " ".join(coords)
			# Save to CSV
			with open(output_csv_path, mode='w', newline='') as csvfile:
				csvfile.write(polypath)  # Write all coordinates as a single line
				
		return polypath

	def extract(self, path, indir, outdir):
		"""
		Convert all .kml files in a directory to .csv files in another directory.

		Args:
			path (str): Root directory of the files.
			indir (str): Directory containing .kml files.
			outdir (str): Directory where .csv files will be saved.
		"""

		indir	= os.path.join(path,indir)
		outdir	= os.path.join(path,outdir)

		# Ensure the output directory exists
		os.makedirs(outdir, exist_ok=True)

		points     = [list(), list()]
		# Iterate through all .kml files in the source directory
		for kml_file in os.listdir(indir):
			if kml_file.endswith(".kml"):
				kml_path = os.path.join(indir, kml_file)
				csv_file = os.path.splitext(kml_file)[0] + ".csv"
				csv_path = os.path.join(outdir, csv_file)

				# Convert and save the .csv file
				output = self.save_coordinates_to_csv(points, kml_path, csv_path)
				print(f"Converted {kml_path} to {csv_path}")
				
				self.output[csv_file]   = output

		minx    = min(points[0])
		maxx    = max(points[0])
		miny    = min(points[1])
		maxy    = max(points[1])

		print( f'range of data: x({minx:.4f} - {maxx:.4f}={(maxx-minx):.4f}) y({miny:.4f} - {maxy:.4f}={(maxy-miny):.4f}) ')
		return

	def dump(self, path, type, dbfile):
		if len(path) > 0:
			dbpath  = os.path.join(path, dbfile)
		else:
			dbpath  = path
		
		if self.resetdb == True:
			ActiveRecord.clear(dbpath)
			
		db  = ActiveRecord.create('', dbpath, 'isohypses')
			
		for k, v in self.output.items():
			if k.startswith(type) == False:
				continue
			
			print( f'Writing {k} to {dbpath}' )
			
			name 	= self.get_name( type, os.path.splitext(k)[0] )
			guid	= str(uuid.uuid1()).lower()
			values = {
                'guid': guid,
                'name': name,
                'type': self.get_type(type, v),
                'path': v,
                self.get_depth_field(type): 0,
				'color': self.get_color(type),				
                'visible': 'Y' }
			
			db.add(values)
		return

	def get_depth_field(self, type):
		return { "land":"height", "sea":"depth", "sky":"height"}[type]

	def get_color(self, type):
		return { "land":"#3CB371", "sea":"#47B9C6", "sky":"#47B9C6"}[type]

	def get_type(self, type, name):
		return { "land":100000, "sea":100000, "sky":100000}[type]

	def get_name(self, type, name):
		if name.startswith(type) == False:
			return name
		
		ndx 	= len(type)
		if name[ndx] == '-':
			ndx	= ndx+1

		return name[ndx:]

if __name__ == "__main__":
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
