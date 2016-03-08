import json, urllib.request
from shapely.geometry import shape, Point
import os.path, getopt, sys

__author__ = 'smbuthia'


class LocationProcessor:

    def find_location_county(long, lat):
        county = ''
        # load GeoJSON file containing sectors
        with open('C:\wamp\www\diss-proto\js\mapdata\countries\ke\kenya-counties.json', 'r') as f:
            js = json.load(f)
        # construct point based on lat/long returned by geocoder. => syntax: Point(long, lat)
        point = Point(long, lat)

        # check each polygon to see if it contains the point
        for feature in js['features']:
            polygon = shape(feature['geometry'])
            if polygon.contains(point):
                county = feature['properties']['name']
        return county

    def get_location_cordinates(location):
        file_name = 'C:\wamp\www\diss-proto\json\locations\%s.json' % location
        json_string = None
        location = location.replace(" ", "+")
        if os.path.isfile(file_name):
            f = open(file_name, 'r')
            json_string = f.read()
        else:
            # Create file using Google geo code
            url = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=AIzaSyDoS2frTqusjFyH_2Zlp8ATgwyWFXxQPZY" % location
            #print(url)
            #proxy = "172.16.30.6"
            #proxies = {"http":"http://%s" % proxy}
            #proxy_support = urllib.request.ProxyHandler(proxies)
            #opener = urllib.request.build_opener(proxy_support, urllib.request.HTTPHandler(debuglevel=1))
            opener = urllib.request.build_opener(urllib.request.HTTPHandler(debuglevel=1))
            urllib.request.install_opener(opener)
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers = {'User-Agent':user_agent}
            request = urllib.request.Request(url,None,headers)
            response = urllib.request.urlopen(request)
            json_string = response.read()
            json_string = json_string.decode('utf-8')
            f = open(file_name, 'w')
            f.write(json_string)

        if json_string is not None:
            json_object = json.loads(json_string)
            status = json_object['status']
            if(status == 'OK'):
                results = json_object['results']
                geometry = results[0]['geometry']
                location = geometry['location']
                # print(location['lat'])
                # print(location['lng'])
        return location

# TODO: get the long and lat coordinates of a location identified by the CoreNLP using Google geocoder
# Check if location file exists locally, if it doesn't create it using Google geocoder

try:
    opts, args = getopt.getopt(sys.argv[1:],"")
    for arg in args:
        loc = LocationProcessor.get_location_cordinates(arg)
        print(LocationProcessor.find_location_county(loc['lng'],loc['lat']))
except getopt.GetoptError as err:
    print(err)

