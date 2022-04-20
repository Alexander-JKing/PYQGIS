from qgis.core import (QgsProcessing, 
    QgsProcessingAlgorithm,
    QgsProcessingParameterFeatureSource, 
    QgsProcessingParameterVectorDestination
    )

import processing


class ExampleAlgo(QgsProcessingAlgorithm):
    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'
    
    def __init__(self):
        super().__init__()
        # Calling the constructor of our class using the 
        # super() function so that all objects work in the
        # same way as QgsProcessingAlgorithm
    
    def name(self):
        return "exalgo_processing_run"
        # Returns the algorithm name
        
    def displayName(self):
        return "Example Processing.run()script"
        # Returns the algorithm name to be displayed in the 
        # Processing Toolbox
        
    def createInstance(self):
        return type(self)()
        # Must return a new copy of the algorithm 
    
    def initAlgorithm(self, config=None):
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                'Input layer'
                [QgsProcessing.TypeVectorAnyGeometry]
            )
        )
        
        self.addParameter(
            QgsProcessingParameterVectorDestination(
                self.OUTPUT,
                'Output layer'
            )
        )
    
    def processAlgorithm(self, parameters, context, feedback):
        outputFile = self.parameterAsOutputLayer(parameters, self.OUTPUT, context)
        
        buffered_layer = processing.run("native:buffer",
            {
            'INPUT':parameters['INPUT'],
            'DISTANCE':2,
            'SEGMENTS':5,
            'END_CAP_STLYE':0,
            'JOIN_STYLE':0,
            'MITER':2,
            'DISSOLVE':False,
            'OUTPUT':outputFile
            },
            is_child_algorithm = True,
            context=context,
            feedback=feedback
            )['OUTPUT']
            
        return {self.OUTPUT:buffered_layer}
        
        