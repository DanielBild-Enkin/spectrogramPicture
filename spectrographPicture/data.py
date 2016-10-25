

from PIL import Image
import numpy as np

def loadImage(path):
    return Image.open(path)

 
def makeScaledArray(im):
    
    intArray = np.array(im)
    flatIntArray = np.sum(intArray,2)
    scaledArray = np.flipud(1-(flatIntArray/382.5-1))
    #scaledArray = scaledArray-np.mean(scaledArray)
    return scaledArray

def getImag(scaledArray):
    
    shp = scaledArray.shape
    imag = np.zeros(shp)    
    
    for ii in range(shp[1]):
        reloa
        col = scaledArray[:,ii]
        imag[:,ii] = (col - np.flipud(col))/2.
        
    return imag

def getReal(scaledArray):
    
    shp = scaledArray.shape
    real = np.zeros(shp)
    
    for ii in range(shp[1]):
        
        col = scaledArray[:,ii]
        real[:,ii] = (col + np.flipud(col))/2.
        
    return real
    
def getComplex(scaledArray):

    comp = getReal(scaledArray) + 1j* getImag(scaledArray)
    
    return comp