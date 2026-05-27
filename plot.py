import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy import *

from scipy.ndimage import rotate

img1 = mpimg.imread('image1.png')
img2 = mpimg.imread('image2.png')
img3 = mpimg.imread('image3.png')
img4 = mpimg.imread('image4.png')

### Display images
fig,ax= plt.subplots(1,4)
ax[0].imshow(img1)
ax[1].imshow(img2)
ax[2].imshow(img3)
ax[3].imshow(img4)
plt.axis('off')
