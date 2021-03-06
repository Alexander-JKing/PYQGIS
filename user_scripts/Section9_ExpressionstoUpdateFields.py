from qgis.PyQt.QtCore import QVariant

vl = QgsVectorLayer("Point", "Companies", "memory")

pr = vl.dataProvider()
pr.addAttributes([QgsField("Name", QVariant.String),
    QgsField("Employees", QVariant.Int),
    QgsField("Revenue", QVariant.Double),
    QgsField("Rev per employee", QVariant.Double),
    QgsField("Sum", QVariant.Double),
    QgsField("Fun", QVariant.Double)])
vl.updateFields()

my_data = [
    {'x':0, 'y':0, 'name':'ABC', 'emp':10, 'rev':100.1},
    {'x':1, 'y':1, 'name':'DEF', 'emp':2, 'rev':50.5},
    {'x':5, 'y':5, 'name':'GHI', 'emp':100, 'rev':725.9}
    ]

for rec in my_data:
    f = QgsFeature()
    pt = QgsPointXY(rec['x'], rec['y'])
    f.setGeometry(QgsGeometry.fromPointXY(pt))
    f.setAttributes([rec['name'], rec['emp'], rec['rev']])
    vl.updateExtents()
    QgsProject.instance().addMapLayer(vl)
 
expression1 = QgsExpression('Revenue/Employees')
expression2 = QgsExpression('Sum(Revenue)')
expression3 = QgsExpression('area(buffer($geometry, Employees))')

context = QgsExpressionContext()
context.appendScopes(QgsExpressionContextUtils.globalProjectLayerScopes(vl))

for field in vl.fields():
    print(field.name())
    
with edit(vl):
    for f in vl.getFeatures():
        context.setFeature(f)
        f['Rev per employee'] = expression1.evaluate(context)
        f['Sum'] = expression2.evaluate(context)
        f['Fun'] = expression3.evaluate(context)
        vl.updateFeature(f)

with edit(vl):
    for f in vl.getFeatures():
        f['Rev per employee'] = f['Revenue'] / f['Emplyees']
        vl.updateFeature(f)

