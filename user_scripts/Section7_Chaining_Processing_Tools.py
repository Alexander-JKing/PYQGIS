rivers = "C:/Users/alexa/Documents/Python/PYQGIS/One/Rivers_Lakes/Rivers_And_Lakes_Centerlines.gpkg|layername=Rivers_And_Lakes_Centerlines"
places = "C:/Users/alexa/Documents/Python/PYQGIS/One/Populated_Places/Populated_Places.gpkg|layername=Populated_Places"

expression = "name_alt = 'Danube'"
danube = processing.run("native:extractbyexpression",
    {'INPUT':rivers, 'EXPRESSION':expression, 'OUTPUT':'memory:'})['OUTPUT']

buffer_distance = 0.1 #Degrees
buffered_danube = processing.run("native:buffer",
     {'INPUT':danube, 'DISTANCE':buffer_distance, 'SEGMENTS': 5, 'END_CAP_STYLE':0, 
     'JOIN_STYLE':0, 'MITER_LIMIT':2, 'DISSOLVE':False, 'OUTPUT':'memory:'})['OUTPUT']

places_along_danube = processing.run("native:extractbylocation",
    {'INPUT':places, 'PREDICATE':[0], 'INTERSECT':buffered_danube, 'OUTPUT':'memory:'})['OUTPUT']

QgsProject.instance().addMapLayer(places_along_danube)

for feature in places_along_danube.getFeatures():
    print(feature['name'])
    
    