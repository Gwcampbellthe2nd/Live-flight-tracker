import imp
from flask import Flask, render_template, request, url_for, redirect, send_from_directory
from opensky.opensky_api import OpenSkyApi

from geojson import Point, Feature, FeatureCollection, dump


headings = ("Call Sign", "Longitude", "Latitude")



app = Flask(__name__, static_url_path='/static')

# code for flight info
# https://opensky-network.org/api/states/all?




@app.route('/',  methods=['GET', 'POST'])
def index():
    
    mapbox_access_token = 'pk.eyJ1IjoiY2FtcGJlbGxnMiIsImEiOiJjanVhbXV0eG8wNGY2NGRueTQxb2JlYzYzIn0.uvKKRqeOvsn9PtDUxWKCog'

    return render_template('index.html', headings=headings, mapbox_access_token=mapbox_access_token)

@app.route('/sidebar',)
def sidebar():    

    return render_template('sidebar.html')


@app.route('/planes.geojson',)
def geojson():
    feature_collection = ""
    data = []
    features = []
    # api = OpenSkyApi()
    api = OpenSkyApi()
    states = api.get_states()

    
    for s in states.states:
        if (s.latitude == None) or (s.longitude == None) or (s.callsign == ""):
            pass
        else:
            point = Point((s.longitude, s.latitude))
            features.append(Feature(geometry=point, properties={"title": s.callsign, 'degree': s.true_track,"altitude": s.geo_altitude, "velocity": s.velocity, "vRate": s.vertical_rate, "long": s.longitude, "lat": s.latitude}))
            planes = (s.callsign, s.longitude, s.latitude)
            data.append(planes)

    feature_collection = FeatureCollection(features)
    

    return feature_collection



if __name__ == "__main__":
    app.run(debug=True)

