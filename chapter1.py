import cv2
print("package imported")


# --------How to Read an Image----------
# img = cv2.imread("resources/bee.png")

# cv2.imshow("Output", img)
# cv2.waitKey(0)



# ----------How to read a video-----------
# cap = cv2.VideoCapture("resources/video.mp4")
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break



# ----------How to open webcam----------
cap = cv2.VideoCapture(0) #0 means the default camera
cap.set(3,640) #setting height of camera
cap.set(4,480) #setting width of camera
cap.set(10,100) #setting the brightness of the webcam

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF ==ord('q'): #this means that pressing 'q' will quit
        break

