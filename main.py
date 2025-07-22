import cv2
import numpy as np
import face_recognition

imgZendaya = face_recognition.load_image_file('Images/Zendaya.jpg')
imgZendaya = cv2.cvtColor(imgZendaya, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('Images/Dwayne.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceLocation = face_recognition.face_locations(imgZendaya)[0]
encodeZendaya = face_recognition.face_encodings(imgZendaya)[0]
cv2.rectangle(imgZendaya,(faceLocation[3],faceLocation[0]),(faceLocation[1],faceLocation[2]),(255,0,0),2)

faceLocationTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocationTest[3],faceLocationTest[0]),(faceLocationTest[1],faceLocationTest[2]),(255,0,0),2)

results = face_recognition.compare_faces([encodeZendaya],encodeTest)
faceDistance = face_recognition.face_distance([encodeZendaya],encodeTest)
print(results, faceDistance)
cv2.putText(imgTest,f'{results} {round(faceDistance[0],2)}', (50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

cv2.imshow('Zendaya', imgZendaya)
cv2.imshow('Zendaya Test', imgTest)
cv2.waitKey(0)
