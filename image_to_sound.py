from scipy.io.wavfile import write
import numpy as np
import os
import imageio
from scipy import misc
from skimage.color import rgb2gray
from skimage.util import invert

samplerate = 16000

path = '.'

image= imageio.imread(os.path.join(path,'input.bmp'))
gimage = rgb2gray(image)
iimage = invert(gimage)
i=1
data=np.array([])
for zeile in reversed(iimage):
    print("Zeile: "+str(i))
    sniplet=np.fft.irfft(zeile,len(zeile))
    for j in sniplet:
        data=np.append(data,np.real(32000.0*j))
    i=i+1

write("output.wav", samplerate, data.astype(np.int16))
