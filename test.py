from flask import Flask, render_template, request, url_for, redirect, send_from_directory
from opensky.opensky_api import OpenSkyApi

from geojson import Point, Feature, FeatureCollection, dump

import time

data = []
features = []

def generate_geojson():
    username = "elrbos2"
    password = "2uwfkhsa"

    api = OpenSkyApi(username=username, password=password)
    states = api.get_states()

    
    for s in states.states:
        if (s.latitude == None) or (s.longitude == None) or (s.callsign == ""):
            pass
        else:
            point = Point((s.longitude, s.latitude))
            features.append(Feature(geometry=point, properties={"title": s.callsign}))
            planes = (s.callsign, s.longitude, s.latitude)
            data.append(planes)

    feature_collection = FeatureCollection(features)


    with open('static/planes.geojson', 'w') as f:
        dump(feature_collection, f)
    f.close()

def clear_geojson():
    open('static/planes.geojson', 'w').close()


while True:
    clear_geojson()
    generate_geojson()
    time.sleep(10)