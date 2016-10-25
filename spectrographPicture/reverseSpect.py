 
import numpy as np
import spectrographPicture.data as spd
import numpy.fft as fft
import scipy.io.wavfile as wavf

def getWave(im):
    
    scaledArray = spd.makeScaledArray(im)
    comp = scaledArray
    #comp = scaledArray[range(512),:]
    #comp = spd.getReal(scaledArray) + 1j*spd.getReal(scaledArray)    
    
    shp = comp.shape    
    subWaveLength = 2*shp[0]-2;
    wave = np.zeros(subWaveLength*shp[1])
    ham = np.hamming(shp[0])    
    
    for ii in range(shp[1]):
        
        col = comp[:,ii]
        
        #col = col*ham
        subWaveFull = fft.irfft(col)
        subWave = subWaveFull[range(subWaveLength)]
        
        #HAM = np.hamming(subWaveLength)               
        #subWave = subWave*HAM          
                              
        #if ii == 1:
        #    wave = subWaveFull
                              
                              
        #
        #print(subWave.shape[0])
        wave[range(ii*subWaveLength,(ii+1)*subWaveLength-1)] = subWave
        
    wave = wave/np.max(wave)
                       
    return wave

def writeWav(waveFile,wave):
    
    wavf.write(waveFile, 44100, wave)