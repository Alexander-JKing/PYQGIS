uri = "C:/Users/alexa/Documents/Python/PYQGIS/One/world_airports.gpkg|layername=world_airports"
worldAirports = iface.addVectorLayer(uri, "name", "ogr")
worldAirports.renderer().symbol().setSize(2)
worldAirports.triggerRepaint()

#.renderer() object = module allowing access to symbolise layers
#.symbol() object = Actual symbol object representing the symbology (Point, line, colour, etc.)
#.setSize() object = method allowing us to set the size of the symbo object.
#.triggerRepaint() = Function call that will enable code to return the result of the code

worldAirports.renderer().symbol().setColor(QColor("yellow"))

#The setColor function expects a QColor object as its parameter.
#This is why we create a new QColor object called QColor("blue")

worldAirports.renderer().symbol().symbolLayer(0).setShape(QgsSimpleMarkerSymbolLayerBase.Hexagon)
worldAirports.triggerRepaint()
iface.layerTreeView().refreshLayerSymbology(worldAirports.id())
#This is to update the symbol in the Layer's panel, not the canvas. This function call will return the correct symbol we had previously defined.


    
    
    
    
