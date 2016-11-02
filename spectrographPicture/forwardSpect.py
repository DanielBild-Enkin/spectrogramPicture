 
import numpy as np
import spectrographPicture.data as spd
import numpy.fft as fft
import scipy.io.wavfile as wavf
import matplotlib.pyplot as plt


def getSpect(wave,windowLength):
    
    n = wave.shape[0]
    nWindow = int(np.floor(n/windowLength))    
    imageScaledArray = np.zeros([windowLength/2+1,nWindow])   
    
    for ii in range(nWindow):
        
        curWindow = wave[range(ii*windowLength,(ii+1)*windowLength)]   
        
        curSpectCol = fft.rfft(curWindow)        
        imageScaledArray[:,ii] = curSpectCol
        
    return imageScaledArray

def getSpectWalking(wave,windowLength,windowStep):
    
    n = wave.shape[0]
    nWindow = int(np.floor((n-windowLength)/windowStep))    
    imageScaledArray = np.zeros([windowLength/2+1,nWindow])
    ham = np.hamming(windowLength)
    
    for ii in range(nWindow):
        
        curWindow = wave[range(ii*windowStep,ii*windowStep+windowLength)]*ham         
                
        curSpectCol = fft.rfft(curWindow).real   
        imageScaledArray[:,ii] = curSpectCol
        
        
        if np.mod(ii,100) ==0:
            print(ii,' of ',nWindow)
        
    return imageScaledArray

def plotSpect(imageScaledArray):    
    
    
    plt.pcolormesh(-imageScaledArray, cmap='gray')
   
   
   
   
   
   
   

   
   
   
   
   
   
   
   
   
