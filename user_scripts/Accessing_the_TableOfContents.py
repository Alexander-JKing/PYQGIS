# You can use different classes to access all the loaded layers in the TOC (Table of Contents),
# and use them to retrieve information.
# - i) QgsProject (class)
# - ii)QgsLayerTreeGroup

# QgsProject:
# You can use the QgsProject class to retrieve information about the TOC and all layers loaded.
# You have to create an 'instance' of QgsProject and use its methods to get the laoded layers.
# The main method is 'mapLayers()'. It will return a dictionary of the loaded layers.

layers = QgsProject.instance().mapLayers()
print(layers)

# The dictionary keys are the unique layer ids while the values are the related objects.
# It is now straightforward to obtain any other information about the layers:

# list of layer names using list comprehension
l = [layer.name() for layer in QgsProject.instance().mapLayers().values()]
# dictionary with key = layer name, and, value = layer object
layers_list ={}
for l in QgsProject.instance().mapLayers().values():
    layers_list[l.name()] = 1

print(layers_list)

# You can also query the TOC using the name of the layer:
country_layer = QgsProject.instance().mapLayersByName("countries")[0]
# A list with all the matching layers is returned, so we index with [0] to get the first layer with this name.

################################################
################################################
################################################

# QgsLayerTreeGroup class:
# The layer tree is a classical tree structure built of nodes.
# There are currently two types of nodes:
# i) Group nodes (QgsLayerTreeGroup)
# ii) layer nodes (QgsLayertreeLayer)

