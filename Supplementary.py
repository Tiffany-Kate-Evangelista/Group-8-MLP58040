import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('HK.png')
bgr_img = cv.cvtColor(img, cv.COLOR_RGB2BGR)

blur = cv.blur(bgr_img, (5, 5))
gaussian_blur = cv.GaussianBlur(bgr_img, (5, 5), 0)
median_blur = cv.medianBlur(bgr_img, 5)
bilateral_filter = cv.bilateralFilter(bgr_img, 9, 75, 75)

text = ['Original', 'Blur', 'Gaussian Blur', 'Median Blur', 'Bilateral Filter']
text_positions = [(20, 40), (20, 40), (20, 40), (20, 40), (20, 40)]

for i, (img, txt, pos) in enumerate(zip([bgr_img, blur, gaussian_blur, median_blur, bilateral_filter], text, text_positions), 1):
    cv.putText(img, txt, pos, cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

plt.figure(figsize=(12, 8))

plt.subplot(232), plt.imshow(bgr_img)
plt.xticks([]), plt.yticks([])

plt.subplot(231), plt.imshow(blur)
plt.xticks([]), plt.yticks([])

plt.subplot(233), plt.imshow(gaussian_blur)
plt.xticks([]), plt.yticks([])

plt.subplot(234), plt.imshow(median_blur)
plt.xticks([]), plt.yticks([])

plt.subplot(236), plt.imshow(bilateral_filter)
plt.xticks([]), plt.yticks([])

plt.tight_layout()
plt.show()
