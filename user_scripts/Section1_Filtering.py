url = "C:/Users/alexa/Documents/Python/PYQGIS/One/world_airports.gpkg|layername=world_airports"
uri = "C:/Users/alexa/Documents/Python/PYQGIS/One/world_countries.gpkg|layername=world_countries"
worldCountries = iface.addVectorLayer(uri, "countries", "ogr")
iface.showAttributeTable(worldCountries)
worldAirports = iface.addVectorLayer(url, "name", "ogr")

for field in worldCountries.fields():
    print(field.name())
    
#worldCountries.setSubsetString("ADMIN like 'A%'")
#for feature in worldCountries.getFeatures():
    #print(feature["ADMIN"], feature["POP_EST"])

for feature in worldCountries.getFeatures():
    print("{} million people live in {}".format(feature["POP_EST"]/1000000, feature["ADMIN"]))

    
    

    
    

    
    
    