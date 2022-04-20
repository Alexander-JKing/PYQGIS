uri = "C:/Users/alexa/Documents/PYQGIS/One/world_countries.gpkg|layername=world_countries"
#vlayer = iface.addVectorLayer(uri, "countries", "ogr")
#iface.showAttributeTable(vlayer)

#for field in vlayer.fields():
    #print(field.name())

#for feature in vlayer.getFeatures():
    #print(feature["ADMIN"])
    
#vlayer.setSubsetString("ADMIN LIKE 'A%'")
#for feature in vlayer.getFeatures():
    #print(feature["ADMIN"])

#vlayer.setSubsetString()
#for feature in vlayer.getFeatures():
    #print(feature["ADMIN"])

my_char = "A"
vlayer.setSubsetString("ADMIN LIKE '"+my_char+"%'")
print("The following country names start with {}:".format(my_char))
for feature in vlayer.getFeatures():
    print(feature["ADMIN"]) 
#This is a correct way to set a filter to countries begginning with the letter A
    
for feature in vlayer.getFeatures():
        print("{pop:2f} million people line in {name}".format(name=feature["ADMIN"], pop=feature["POP_EST"]/1000000))
# This is a way to display the population of the countries to two decimal places.



    
    

    
    

    
    
    