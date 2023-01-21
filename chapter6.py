#joining images in horizontal and vertical stack
import cv2
import numpy as np

img = cv2.imread("resources/boat.png")

horizontal = np.hstack((img,img))
vertical = np.vstack((img,img))

cv2.imshow("horizontal", horizontal)
cv2.imshow("vertical", vertical)

cv2.waitKey(0)