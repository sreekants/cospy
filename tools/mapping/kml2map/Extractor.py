#!/usr/bin/python
# Filename: Extractor.py
# Description: Extractor for KML files.


from xml.etree import ElementTree as ET
import csv
import os
import numpy as np

from scipy.interpolate import interp1d
from pyproj import CRS, Transformer

# Map a point to a 1200 x 800 pixel zone
mapper = (
            (interp1d([400,7800],[0,1200]), 1874000), 
            (interp1d([12400,22000],[0,800]), 3280000)
            )

zone_number = 35
zone_letter ="N"

def latlon_to_utm( lat, lon ):
    """
    Converts latitude and longitude of a position to a defined UTM projection.
    Parameters:
    lat: latitude
    lon: longitude
    zone_number (int): UTM zone number
    zone_letter (str): UTM zone letter (N or S)
    Returns:
    tuple: easting, northing
    """
    # Determine if the zone is in the northern or southern hemisphere
    is_northern = zone_letter.upper() >= "N"
    # Define the UTM coordinate system based on zone and hemisphere
    utm_crs = CRS.from_proj4(f"+proj=utm +zone={zone_number} +{'north' if is_northern else 'south'} +ellps=WGS84")
    wgs84_crs = CRS.from_epsg(4326)  # EPSG:4326 for WGS84
    # Create a transformer object
    transformer = Transformer.from_crs(wgs84_crs, utm_crs)
    # Perform the transformation
    easting, northing = transformer.transform(lat, lon)
    return easting, northing


def map_to_screen(long, lat, mapper):
    """
    maps map coord to screen.

    Args:
        lon (float): Longitude.
        lat (float): Latitude.
        mapper (float): Scale mapping.

    Returns:
        list: A list of tuples containing (longitude, latitude, altitude).
    """
    xoff        = mapper[0][1]
    yoff        = mapper[1][1]
    mlong, mlat = latlon_to_utm(long, lat)
    mlong   = mlong-xoff
    mlat    = mlat-yoff

    return mapper[0][0](mlong), mapper[1][0](mlat)

def save_coordinates_to_csv(points, kml_file_path, output_csv_path):
    """
    Extract coordinates from a .kml file.

    Args:
        kml_file_path (str): Path to the .kml file.

    Returns:
        list: A list of tuples containing (longitude, latitude, altitude).
    """
    # Parse the .kml file
    tree = ET.parse(kml_file_path)
    root = tree.getroot()


    # Namespace definitions for KML
    namespaces = {'kml': 'http://www.opengis.net/kml/2.2'}

    # Extract all coordinates
    all_coordinates = []
    for placemark in root.findall(".//kml:Placemark", namespaces):
        for coord in placemark.findall(".//kml:coordinates", namespaces):
            coord_text = coord.text.strip()
            coord_list = coord_text.split()
            # Collect all coordinates in the required format
            for c in coord_list:
                lon, lat, *_        = map(float, c.split(','))
                map_lon, map_lat    = map_to_screen(lon, lat, mapper)
                # Format with four digits of precision
                formatted_lon = f"{map_lon:.2f}"
                formatted_lat = f"{map_lat:.2f}"

                points[0].append(map_lon)
                points[1].append(map_lat)

                all_coordinates.append(f"{formatted_lon},{formatted_lat}")

    # Save to CSV
    with open(output_csv_path, mode='w', newline='') as csvfile:
        csvfile.write(" ".join(all_coordinates))  # Write all coordinates as a single line


def automate_kml_to_csv_conversion(path_kml_data, path_csv_data):
    """
    Convert all .kml files in a directory to .csv files in another directory.

    Args:
        path_kml_data (str): Path to the directory containing .kml files.
        path_csv_data (str): Path to the directory where .csv files will be saved.
    """
    # Ensure the output directory exists
    os.makedirs(path_csv_data, exist_ok=True)
    
    points     = [list(), list()]
    # Iterate through all .kml files in the source directory
    for kml_filename in os.listdir(path_kml_data):
        if kml_filename.endswith(".kml"):
            kml_file_path = os.path.join(path_kml_data, kml_filename)
            csv_filename = os.path.splitext(kml_filename)[0] + ".csv"
            csv_file_path = os.path.join(path_csv_data, csv_filename)

            # Convert and save the .csv file
            save_coordinates_to_csv(points, kml_file_path, csv_file_path)
            print(f"Converted {kml_file_path} to {csv_file_path}")

    minx    = min(points[0])
    maxx    = max(points[0])
    miny    = min(points[1])
    maxy    = max(points[1])

    print( f'range of data: x({minx:.4f} - {maxx:.4f}={(maxx-minx):.4f}) y({miny:.4f} - {maxy:.4f}={(maxy-miny):.4f}) ')

# Paths to the KML and CSV directories
path_kml_data = "kml"
path_csv_data = "csv"

# Automate the process
automate_kml_to_csv_conversion(path_kml_data, path_csv_data)
