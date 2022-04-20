url = QgsVectorLayer("C:/Users/alexa/Documents/Python/PYQGIS/One/Populated_Places/Populated_Places.gpkg|layername=Populated_Places")
# url is a QgsVectorLayer instance
url = iface.activeLayer()
features = url.getFeatures()

for feature in features:
    # retrieve every feature with its geometry and attributes
    print('Feature ID', feature.id())
    # fetch geometry
    # show some information about the feature geometry
    geom = feature.geometry()
    geomSingleType = QgsWkbTypes.isSingleType(geom.wkbType())
    if geom.type() == QgsWkbTypes.PointGeometry:
    # (QgsWkbTypes = Handles storage of information regarding WKB tpyes and their properties)
    # (WKB = Well-Known_Binary, a format for representing geogrpahical and geometrical data).
        if geomSingleType:
            # The geometry can be of single or multi type
            x = geom.asPoint()
            print('Point: ', x)
        else:
            x = geom.asMultiPoint()
            print('Point: ', x)
            
    elif geom.type() == QgsWkbTypes.LineGeometry:
        if geomSingleType:
            x = geom.asPolyline()
            print('Line: ', x, 'Length: ', geom.length())
        else:
            x = geom.asMultiPolyline()
            print('Line: ', x, 'Length: ', geom.length())
                
    elif geom.type() == QgsWkbTypes.PolygonGeometry:
        if geomSingleType:
            x = geom.asPolygon()
            print('Polygon: ', x, 'Area: ', geom.area())
        else:
            x = geom.asMultiPolygon()
            print('Polygon: ', x, 'Area: ', geom.area())
            
    else:
        print('Unkown/Invlaid geometry')
    
    # fetch attributes
    attrs = feature.attributes
    # attrs is a list. It contains all the attribute values of this feature
    print(attrs)
    # for this test only print the first feature
    break
    