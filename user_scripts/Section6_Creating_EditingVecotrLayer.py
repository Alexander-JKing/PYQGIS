
vl = QgsVectorLayer("Point", "temp", "memory")

from qgis.PyQt.QtCore import QVariant
pr = vl.dataProvider()
pr.addAttributes([QgsField("name", QVariant.String), QgsField("age", QVariant.Int), QgsField("size", QVariant.Double)])
vl.updateFields()

f = QgsFeature()
f.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(-7, 53)))
f.setAttributes(["Alex K.", 24, 0.5])
pr.addFeature(f)
vl.updateExtents()
QgsProject.instance().addMapLayer(vl)

print("Number of Fields:", len(pr.fields()))
print("Number of features:", pr.featureCount())
e = vl.extent()
print("Extent", e.xMinimum(), e.yMinimum(), e.xMaximum(), e.yMaximum())

for f in vl.getFeatures():
    print("Features", f.id(), f.attributes(), f.geometry().asPoint())

vl.startEditing()
newField = "Mr.Robot"
vl.addAttribute(QgsField(newField, QVariant.String))
vl.updateFields()

for f in vl.getFeatures():
    print("Feature:", f.id(), f.attributes(), f.geometry().asPoint())
    
newValue = "Hello World, we are fSociety!"

for f in vl.getFeatures():
    f[newField] = newValue
    vl.updateFeature(f)

vl.commitChanges()

for f in vl.getFeatures():
    print("Feature:", f.id(), f.attributes(), f.geometry().asPoint())

iface.vectorLayerTools().stopEditing(vl)

newField2 = "The Witcher"
newValue2 = "Toss a coin to you Witcher, O' Valley of Plenty"

with edit(vl):
    vl.addAttribute(QgsField(newField2, QVariant.String))
    for f in vl.getFeatures():
        f[newField2] = newValue2
        vl.updateFeature(f)
    