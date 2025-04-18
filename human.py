import cv2
import numpy as np
img = np.zeros((600, 600, 3), dtype=np.uint8)
center_coordinates = (300, 300)
radius = 200
color = (255, 255, 255)
thickness = 4
cv2.circle(img, center_coordinates, radius, color, thickness)
cv2.circle(img, (250, 250), 30, color, thickness)
cv2.circle(img, (350, 250), 30, color, thickness)
cv2.ellipse(img, center_coordinates, (100, 60), 0, 0, 180, color, thickness)
cv2.imshow("Human Face", img)
cv2.waitKey(0)
cv2.destroyAllWindows()