#resizing and cropping
import cv2
import numpy as np



img = cv2.imread("resources/bee.png")
print(img.shape)

imgResize = cv2.resize(img,(300,200)) #width comes first, then height
print(imgResize.shape)

imgCropped = img[0:200,200:500] #height comes first, then width

cv2.imshow("image",img)
cv2.imshow("image resize", imgResize)
cv2.imshow("image cropped", imgCropped)

cv2.waitKey(0)