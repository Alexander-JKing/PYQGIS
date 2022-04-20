#uri = "C:/Users/alexa/Documents/Python/PYQGIS/One/world_countries.gpkg|layername=world_countries"
#worldCountries = iface.addVectorLayer(uri, "countries", "ogr")
url = "C:/Users/alexa/Documents/Python/PYQGIS/One/world_airports.gpkg|layername=world_airports"
worldAirports = iface.addVectorLayer(url, "name", "ogr")


heatmap = QgsHeatmapRenderer()
# Create a variable for your heatmap. Assign the QgsHeatmapRenderer object to it. Similar to a module.
ramp = QgsStyle().defaultStyle().colorRamp("Magma")
# Create another variable for the Colour of your heatmap. Assign the colour object to your variable.
heatmap.setColorRamp(ramp)
# Append the ramp variable to your heatmap variable.
heatmap.setRadius(5)
# Use the setRadius Method to set the radius of the heatmap.
worldAirports.setRenderer(heatmap)
# Append the heatmap variable to your Vector Layer object
worldAirports.triggerRepaint()
# Finally, call the function to return the object to the canvas.

print(QgsStyle().defaultStyle().colorRampNames())
# Prints a list of Color Ramp names available to use.
