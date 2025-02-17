import cv2
#Code for enabling webcam
# video_cap = cv2.VideoCapture(0)
# while True:
#     ret , video_data = video_cap.read()
#     cv2.imshow("video_live",video_data)
#     if cv2.waitKey(10) == ord("a"):
#         break
# video_cap.release()
# face_cap = cv2.CascadeClassifier("C:/Users/jesicca.nayak/AppData/Local/Programs/Python/Python311/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
# video_cap = cv2.VideoCapture(0)
# while True:
#     ret , video_data = video_cap.read()
#     col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
#     faces = face_cap.detectMultiScale(
#         col,
#         scaleFactor=1.1,
#         minNeighbors=5,
#         minSize=(30,30),
#         flags=cv2.CASCADE_SCALE_IMAGE
#     )
#     for(x,y,w,h) in faces:
#         cv2.rectangle(video_data, (x,y), (x+w,y+h),(255,0,0),2)
#     cv2.imshow("video_live",video_data)
#     if cv2.waitKey(10) == ord("a"):
#         break
# video_cap.release()
#Loading The Cascade File

#Loading The Cascade File
face_cascade = cv2.CascadeClassifier('C:/Users/jesicca.nayak/AppData/Local/Programs/Python/Python311/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

#Reading the Input Image
# image= cv2.imread('Oia.jpeg')
image= cv2.imread('Multiple.png')

#Resizing the Image
img = cv2.resize(image,None,fx=0.3,fy=0.3)

#Converting the image into grayscale image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detecting The Faces
faces = face_cascade.detectMultiScale(imgGray, 1.2, 5)

#Pointing The Faces
for (x,y,w,h) in faces:
	cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)

#Displaying The Output Image
cv2.imshow('img', img)
cv2.waitKey()