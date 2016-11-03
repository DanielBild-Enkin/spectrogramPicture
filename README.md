a spectrogram is a method of analysing sounds that shows the Fourier transform of a changing waveform at each point in time. This program takes an image as interprets it as a spectrogram, creating the  waveform that would have the image as a spectrogram.

to run: use the file script.py. It will work in general but it designed to be run in sections in a Spyder IDE.


import spectrographPicture.data as spd
import spectrographPicture.reverse_spect as rs
import spectrographPicture.forward_spect as fs


img = spd.load_image("test/kd.jpg")

wave = rs.getWave(img)

rs.writeWav('kd.wav',wave)

sa = fs.getSpect(wave,img.size[1]*2-2)

fs.plotSpect(sa)

saw = fs.getSpectWalking(wave,2048,512)

fs.plotSpect(saw)

The resulting .wav file can be loaded into Audacity and you can view the spectrogram and see that it is similar to the initial image. For optimal viewing (outside of the function provided) the settings should be 

window size 2048
maximum frequency 22000 Hz
grayscal true