from OSMPythonTools.nominatim import Nominatim
from OSMPythonTools.overpass import overpassQueryBuilder, Overpass
import sys


regionName = sys.argv[1]
# Create a Nominatim Query Object
nominatimQuery = Nominatim().query(regionName)

# Create a query from the Nominatim Query object
query = overpassQueryBuilder(area=nominatimQuery.areaId(), elementType=['way', 'relation'], includeGeometry=True)

# Or this:
query = overpassQueryBuilder(area=nominatimQuery.areaId(), elementType=['way', 'relation'], selector='"boundary"="administrative"', includeGeometry=True)

#Perform the query:
result = Overpass().query(query)

#Then from the results print the geometry:
geoJson = result.elements()[0].geometry()
print(geoJson)
