"""tools for creating and view spectrograms with pyplot"""
import numpy as np
import numpy.fft as fft
import matplotlib.pyplot as plt

def get_spect(wave, window_length):
    """creates a spectrogram with the window places to exactly undo the
    transformation done with reverse_spectrogram"""
    wave_length = wave.shape[0]
    n_window = int(np.floor(wave_length/window_length))
    image_scaled_array = np.zeros([window_length/2+1, n_window])

    for ii in range(n_window):
        cur_window = wave[range(ii*window_length, (ii+1)*window_length)]
        cur_spect_col = fft.rfft(cur_window)
        image_scaled_array[:, ii] = cur_spect_col

    return image_scaled_array

def get_spect_walking(wave, window_length, window_step):
    """creates a more standard spectrogram with the windows moving a
    smaller step than the window size. This leads to some artifacts if
    used to view the spectrogpram from a wave created by reverse_spectrogram"""
    wave_length = wave.shape[0]
    n_window = int(np.floor((wave_length-window_length)/window_step))
    image_scaled_array = np.zeros([window_length/2+1, n_window])
    ham = np.hamming(window_length)

    for ii in range(n_window):
        cur_window = wave[range(ii*window_step, ii*window_step+window_length)]*ham
        cur_spect_col = fft.rfft(cur_window).real
        image_scaled_array[:, ii] = cur_spect_col

        if np.mod(ii, 100) == 0:
            print(ii, ' of ', n_window)

    return image_scaled_array

def plot_spect(image_scaled_array):
    """plots a scaled array from one of the above functions"""
    plt.pcolormesh(1-image_scaled_array, cmap='gray')

















