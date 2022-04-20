from osgeo import ogr
my_gpkg = "C:/Users/alexa/Documents/Python/PYQGIS/One/NaturalEarth_Physical_Vector/NaturalEarth_100mVectorData.gpkg"
gpkg_layers = [l.GetName() for l in ogr.Open(my_gpkg)]
print(gpkg_layers)

print('foo' in gpkg_layers)

my_layer = 'ne_110m_land'
if my_layer in gpkg_layers:
    iface.addVectorLayer(my_gpkg +"|layername=" + my_layer, my_layer, 'ogr')
else:
    print('Error: there is no layer named "{}" in {}'.format(my_layer, my_gpkg))
    
def add_gpkg_layer(my_gpkg, layer):
    layers = [l.GetName() for l in ogr.Open(my_gpkg)]
    if layer in layers:
        iface.addVectorLayer(my_gpkg + "|layername=" + my_layer, my_layer, 'ogr')
        print('This layer is included')
    else:
        print('Error: there is no layer named "{}" in {}'.format(my_layer, my_gpkg))

add_gpkg_layer(my_gpkg, 'ne_110m_land')

#Of course we can also create a function that laods multiple layers at once:

def add_layers_from_gpkg(my_gpkg, layers):
    for layer in layers:
        add_gpkg_layer(my_gpkg, layer)

add_layers_from_gpkg(my_gpkg, ['ne_110m_land', 'ne_110m_lakes'])

#Finally if we want to load all layers we can write:

def add_all_layers_from_gpkg(my_gpkg):
    layers = [l.GetName() for l in ogr.Open(my_gpkg)]
    add_layers_from_gpkg(my_gpkg, layers)
    
    
    
        
        