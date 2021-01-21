from flask import Flask
from flask import request

from OSMPythonTools.nominatim import Nominatim
from OSMPythonTools.overpass import overpassQueryBuilder, Overpass

import sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def extractNameAndSearch():
    regionName = request.get_json()["name"]
    return search(regionName)

def search(regionName):
    # Create a Nominatim Query Object
    nominatimQuery = Nominatim().query(regionName)

    # Create a query from the Nominatim Query object
    query = overpassQueryBuilder(area=nominatimQuery.areaId(), elementType=['way', 'relation'], selector='"boundary"="administrative"', includeGeometry=True)

    #Perform the query:
    result = Overpass().query(query)

    #Then from the results print the geometry:
    geoJson = result.elements()[0].geometry()
    print(geoJson)
    return geoJson
