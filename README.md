cd 
a spectrogram is a mehtod of analysising sounds that shows the fourier transform of a changing waveform at each point intime. This program takes an image as interprets it as a spectrogram, creating the  waveform that would have the image as a spectrogram.

to run:

import spectrographPicture.data as spd
import spectrographPicture.reverseSpect as rs
img = spd.loadImage("test/kd.jpg")
wave = rs.getWave(img)
rs.writeWav('kd.wav',wave)

The resulting .wav file can be loaded into Audacity and you can view the spectrogram as see that it is similar to the initial image.