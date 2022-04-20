url = "C:/Users/alexa/Documents/Python/PYQGIS/One/GRAY_50M_SR_W/GRAY.tif"
#rlayer = iface.addRasterLayer(url, "my raster", "gdal")
manager = QgsProject.instance().layoutManager()
# Like in the last tutorial, the actual QGIS projec is being accessed here through the .instance() function.
# Previously we used the addMapLayer()function available in the instance class, but here we are using the .layoutManager() function.
print(manager.printLayouts())
# Prints out the Layout objects we have previously vonfigured, but unable to distinguish the returned objects from one another.
# We must get their names.

for layout in manager.printLayouts():
    print(layout.name())
# Use a 'for' loop to cycle through each layout we have already named and configured. Then we print the name of each one.

exporter = QgsLayoutExporter(layout)
# Need to use the QgsLayoutExporter to export our (layout).
exporter.exportToImage("C:/Users/alexa/Documents/Python/PYQGIS/Heatmap.tif", QgsLayoutExporter.ImageExportSettings())
# Call the exportToImage function on our exporter variablem, then fill in the two paramters.
# The first parameter will be the name for your layout, and the file directory you are exporting to.
# The second parameter, will be the QgsLayoutExporter followed by the chosen outputs export settings, in this case ImageExportSettings()