import cv2
import numpy as np
img = cv2.imread("rx100.jpeg")
cv2.imshow("rx100", img)
height = img.shape[0]
width = img.shape[1]
print("img-dimensions:", height, width)
M = np.float32([[1, 0, 80], [0, 1, 40]])
img2 = cv2.warpAffine(img, M, (width, height))
cv2.imshow("Translated Image", img2)
scale_percent = 50
new_width = int(img.shape[1] * scale_percent / 100)
new_height = int(img.shape[0] * scale_percent / 100)
dim = (new_height, new_width)
scaled_img = cv2.resize(img, dim)
cv2.imshow("Scaled Image", scaled_img)
cv2.waitKey(0)