import processing

url = "C:/Users/alexa/Documents/Python/PYQGIS/One/World_Countries/world_countries.gpkg|layername=world_countries"
countries = iface.addVectorLayer(url, "", "ogr")

countries.setName("Countries")
buffer_Distance = 0.5

processing.runAndLoadResults("native:buffer",
    {"INPUT":url, "DISTANCE":buffer_Distance, "SEGMENTS":5, "END_CAP_STYLE":0, "JOIN_STYLE":0,
    "MITER_LIMIT":2, "DISSOLVE":False, "OUTPUT":"memory:"})

project = QgsProject.instance()
print(project.mapLayers())

for id, layer in project.mapLayers().items():
    print(layer.name())
    
bufferRenamed = project.mapLayersByName("Buffered")[0]
bufferRenamed.setName("Buffer_Python")

Countries_deleted = project.mapLayersByName("Countries")[0]
project.removeMapLayer(Countries_deleted.id())