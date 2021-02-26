from krita import *

application = Krita.instance()
currentDoc = application.activeDocument()

Krita.instance().action('edit_undo').trigger()
currentDoc.refreshProjection()
#
i = 0
j = 0.0
#print(edFilterConfig.properties())
"""
while i < 5 :
    currentDoc = application.activeDocument()
    currentLayer = currentDoc.activeNode()

    edFilter = application.filter('edge detection')
    edFilterConfig = edFilter.configuration()
    edFilterConfig.setProperty('lockAspect', False)
    edFilterConfig.setProperty('type','prewitt')
    edFilterConfig.setProperty('horizRadius',j)

    edFilter.setConfiguration(edFilterConfig)
    #print( edFilterConfig.property('level') )

    edFilter.apply(currentLayer, 0, 0, currentDoc.width(), currentDoc.height())
    currentDoc.refreshProjection()
    Krita.instance().action('edit_undo').trigger()
    currentDoc.refreshProjection()

    #currentDoc.setBatchmode(True)
    #currentDoc.saveAs('/home/kunan/Documentos/magia/krita_scripts/img_'+str(i)+'.png')
    
    i += 1
    j += 0.01
    
"""