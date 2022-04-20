url = "C:/Users/alexa/Documents/Python/PYQGIS/One/world_countries.gpkg|layername=world_countries"
#vlayer = iface.addVectorLayer(url, "countries", "ogr")
#iface.showAttributeTable(vlayer)
result = processing.run("native:buffer", 
    {'INPUT':url, 'DISTANCE':4, 'SEGMENTS':5, 
    'END_CAP_STYLE':0, 'JOIN_STYLE':0, 'MITER_LIMIT':2, 
    'DISSOLVE':False, 'OUTPUT':'memory:'})

# When using the processing function to access QGIS Tools, there are two parameters to fill:
# The first is the name of the processing tool you are using. (Make sure the name is correct by checking the 
# information in the processing history tab.
# The second are the algorithim settings, stored here in a dictionary.

QgsProject.instance().addMapLayer(result['OUTPUT'])
# The .instance() function allows us to access the current QGIS object.
# Allows us to add and remove layers from/to the canvas.
# In the dictionary above (Stored as a parameter in the variable 'result'), 
# we have saved the processing tool layer under the value 'memory', in the key 'OUTPUT'.
# We can then slice this when referencing the .instance() function.

processing.algorithmHelp("native:buffer")

processing.runAndLoadResults("native:buffer", 
    {'INPUT':url, 'DISTANCE':1, 'SEGMENTS':5, 
    'END_CAP_STYLE':0, 'JOIN_STYLE':0, 'MITER_LIMIT':2, 
    'DISSOLVE':False, 'OUTPUT':'memory:'})