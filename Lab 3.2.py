import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('HK.png')
bgr_img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
blur = cv.GaussianBlur(bgr_img, (5, 5), 0)

plt.subplot(121), plt.imshow(bgr_img), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()