"""takes a scaled array from spectropgraphPicture and converts it into a
.wav file whose spectrogram is the image"""
import numpy as np
import numpy.fft as fft
import scipy.io.wavfile as wavf

import spectrographPicture.data as spd

def get_wave(img):
    """creates the sample array to be written as a .wav file"""
    scaled_array = spd.make_scaled_array(img)

    shp = scaled_array.shape
    sub_wave_length = 2*shp[0]-2
    wave = np.zeros(sub_wave_length*shp[1])

    for ii in range(shp[1]):
        col = scaled_array[:, ii]
        sub_wave = fft.irfft(col)
        wave[range(ii*sub_wave_length, (ii+1)*sub_wave_length-1)] = sub_wave

    wave = wave/np.max(wave)
    return wave

def write_wav(wave_file, wave):
    """writes sample array as a .wav file"""
    wavf.write(wave_file, 44100, wave)
