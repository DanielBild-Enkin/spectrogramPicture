 
import numpy as np
import spectrographPicture.data as spd
import numpy.fft as fft
import scipy.io.wavfile as wavf

def getWave(im):
    
    scaledArray = spd.makeScaledArray(im)
    comp = scaledArray 
    
    shp = comp.shape    
    subWaveLength = 2*shp[0];
    wave = np.zeros(subWaveLength*shp[1])
    ham = np.hamming(shp[0])    
    
    for ii in range(shp[1]):
        
        col = comp[:,ii]
        
        subWaveFull = fft.irfft(col)
        subWave = np.zeros(subWaveLength)
        subWave[range(subWaveFull.shape[0])]=subWaveFull 
              
        
        #print(subWave.shape[0])
        wave[range(ii*subWaveLength,(ii+1)*subWaveLength-1)] = subWave
        
    wave = wave/np.max(wave)
                       
    return wave

def writeWav(waveFile,wave):
    
    wavf.write(waveFile, 44100, wave)