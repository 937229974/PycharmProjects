import cv2
import face_recognition
import sys
import numpy as np


face_image = face_recognition.load_image_file("E://pics/2.jpg")
face_encodings = face_recognition.face_encodings(face_image)
face_locations = face_recognition.face_locations(face_image)
n = len(face_encodings)
if n>2 :
	print("3")
	sys.exit()
try:
	face1 = face_encodings[0]
	face2 = face_encodings[1]
except :
	print("2")
	sys.exit()

results = face_recognition.compare_faces([face1], face2, tolerance=0.5)

if results == [True]:
	print("0")
	name = "PASS"
else:
	print("1")
	name = "DENIED"
for i in range(len(face_encodings)):
	face_encoding = face_encodings[(i-1)]
	face_location = face_locations[(i-1)]
	top, right, bottom, left = face_location
	cv2.rectangle(face_image, (left, top), (right, bottom), (0, 255, 0), 2)
	
	cv2.putText(face_image, name, (left-10, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

face_image_rgb = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)
cv2.imshow("Output", face_image_rgb)
cv2.imwrite('E://pics/2_2.jpg',face_image_rgb,[int(cv2.IMWRITE_JPEG_QUALITY),100])
cv2.waitKey(0)


