from krita import *
import random
application = Krita.instance()

i = 0
j = 0.0
#edFilter = application.filter('edge detection')
#edFilterConfig = edFilter.configuration()
#edFilterConfig.setProperty('type','sobel')

#print(edFilterConfig.properties())
while i < 50 :
    currentDoc = application.activeDocument()
    currentLayer = currentDoc.activeNode()

    edFilter = application.filter('edge detection')
    edFilterConfig = edFilter.configuration()
    if i%3 == 0 :
        edFilterConfig.setProperty('lockAspect', False)
        edFilterConfig.setProperty('type','prewitt')
        edFilterConfig.setProperty('horizRadius',j)
        #if you are krakkin an upper layer and you want things
        #under it to show, set it to transparent.
        if random.choice([1,0])==1:
            edFilterConfig.setProperty('transparency',True)

    elif i%3 == 1 :
        edFilterConfig.setProperty('lockAspect', False)
        edFilterConfig.setProperty('type','simple')
        edFilterConfig.setProperty('horizRadius',j)
        if random.choice([1,0])==1:
            edFilterConfig.setProperty('transparency',True)

    else:
        edFilterConfig.setProperty('lockAspect', False)
        edFilterConfig.setProperty('horizRadius',j)
        edFilterConfig.setProperty('type','sobel')
        if random.choice([1,0])==1:
            edFilterConfig.setProperty('transparency',True)

    edFilter.setConfiguration(edFilterConfig)
    #print( edFilterConfig.property('level') )

    edFilter.apply(currentLayer, 0, 0, currentDoc.width(), currentDoc.height())
    currentDoc.setBatchmode(True)
    currentDoc.saveAs('/home/kunan/Documentos/magia/krita_scripts/random_'+str(i)+'.png')
    i += 1
    j += 0.01


