 
import spectrographPicture.data as spd

z = spd.loadImage("test/line.bmp")
zAr = spd.makeScaledArray(z)
for ii in range(100):
    spd.getReal(zAr)
         