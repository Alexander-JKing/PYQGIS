url = "C:/Users/alexa/Documents/Python/PYQGIS/One/GRAY_50M_SR_W/GRAY.tif"
rlayer = iface.addRasterLayer(url, "my raster", "gdal")

if rlayer.isValid():
    print("This is a valid raster Layer!")
else:
    print("This is not a valid raster layer, please input a different file")
    
print("Width:{}px".format(rlayer.width()))
print("Height:{}px".format(rlayer.height()))
print("Extent:{}".format(rlayer.extent().toString()))

stats = rlayer.dataProvider().bandStatistics(1)
print("Min value:{}".format(stats.minimumValue))
print("Max value:{}".format(stats.maximumValue))
