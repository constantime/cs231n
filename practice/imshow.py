import numpy as np
from scipy.misc import imread, imshow, imresize
import matplotlib.pyplot as plt

img = imread('img/cat.jpg')
img_tinted = imread('img/cat_tinted.jpg')

# Show original image
plt.subplot(1,2,1)
plt.imshow(img)

# Show tinted imag
plt.subplot( 1,2,2)
plt.imshow( img_tinted)


plt.show()

