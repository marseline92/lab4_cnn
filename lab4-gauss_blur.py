import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('test.png')
plt.imshow(img)
plt.show()

bw = img.mean(axis = 2)
plt.imshow(bw, cmap = 'gray')
plt.show()

W = np.zeros((20, 20))
for i in xrange(20):
    for j in xrange(20):
        dist = (i - 9.5) ** 2 + (j - 9.5) ** 2
        W [i, j] = np.exp (-dist / 50)
plt.imshow(W, cmap = 'gray')
plt.show()

out = convolve2d(bw, W)
plt.imshow(out, cmap = 'gray')
plt.show()

out.shape()

out = convolve2d(bw, W, mode = 'same')
plt.imshow(out, cmap = 'gray')
plt.show()

out.shape()
bw.shape()

out3 = np.zeros(img.shape)
for i in xrange(3):
    out3[:,:,i] = convolve2d(img[:,:,i], W, mode='same')
plt.imshow(out3)
plt.show()