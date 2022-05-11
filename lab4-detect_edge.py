import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('test.png')
bw = img.mean(axis = 2)

Hx = np.array ([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1],
], Dtype = np.float32)

Hy = Hx.T

Gx = convolve2d(bw, Hx)
plt.imshow(Gx, cmap = 'gray')
plt.show()

Gy = convolve2d(bw, Hy)
plt.imshow(Gy, cmap = 'gray')
plt.show()

G = np.sqrt(Gx * Gx + Gy * Gy)
plt.imshow(G, cmap = 'gray')
plt.show()

theta = np.arctan2(Gy, Gx)
plt.imshow(theta, cmap = 'gray')
plt.show()
