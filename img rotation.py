import cv2
img = cv2.imread("rx100.jpeg")
cv2.imshow("rx100", img)
CounterClockWise_90 = cv2.rotate(img,
cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("90_CounterClockWise", CounterClockWise_90)
ClockWise_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("90_ClockWise", ClockWise_90)
Rotated_Image_180 = cv2.rotate(img, cv2.ROTATE_180)
cv2.imshow("180_Image", Rotated_Image_180)
cv2.waitKey(0)