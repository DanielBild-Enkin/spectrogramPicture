# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
import numpy as np
import matplotlib.pyplot as plt

import spectrographPicture.data as spd
import spectrographPicture.reverse_spect as rs
import spectrographPicture.forward_spect as fs
#%%


img = spd.load_image("test/kd.jpg")
wave = rs.getWave(img)
rs.writeWav('kd.wav',wave)

#%%
sa = fs.getSpect(wave,img.size[1]*2-2)
fs.plotSpect(sa)

#%%

saw = fs.getSpectWalking(wave,2048,512)
fs.plotSpect(saw)