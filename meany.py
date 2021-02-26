from krita import *

application = Krita.instance()

i = 0
j = 0.0
while i < 50 :
    currentDoc = application.activeDocument()
    currentLayer = currentDoc.activeNode()

    meany = application.filter('mean removal')
    

    meany.apply(currentLayer, 0, 0, currentDoc.width(), currentDoc.height())
    currentDoc.setBatchmode(True)
    currentDoc.saveAs('/home/kunan/Documentos/magia/krita_scripts/img_'+str(i)+'.png')
    i += 1
    j += 0.001