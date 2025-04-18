import cv2
img =cv2.imread("rx100.jpeg")
cv2.imshow("rx100.jpg", img)
cv2.imwrite("rx100.png", img)
cv2.imwrite("rx100.tiff", img)
cv2.imshow("rx100.png", img)
cv2.imshow("rx100.tiff", img)
cv2.waitKey(0)