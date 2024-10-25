import cv2
import numpy as np


image=cv2.imread('img/image.png')
gamma=2
gammaImage=np.power(image,gamma)
cv2.imshow("gammaa",gammaImage)