import cv2
image = cv2.imread('rx100.jpeg')
cv2.imshow('Original Image', image)
height = image.shape[0]
width = image.shape[1]
print("The Dimensions of the image are: ", height,
width)
new_width = 400
new_height = 300
resized_image = cv2.resize(image, (new_height,
new_width), interpolation=cv2.INTER_LINEAR)
cv2.imwrite('Resized_Image.jpg', resized_image)
cv2.imshow('Resized_Image', resized_image)
height = resized_image.shape[0]
width = resized_image.shape[1]
print("The Dimensions of the Resized Image are: ",
height, width)
cv2.waitKey(0)