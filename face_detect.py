import cv2

img = cv2.imread("4f.jpg")

gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(gray)
print(faces)
i = 1 
for (x,y,w,h) in faces:
       roi = img[y:y+h,x:x+w]
       name = "face"+str(i)+".jpg"
       cv2.imwrite(name,roi)
       i = i+1
       cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
             
cv2.imshow('img',img)
cv2.waitKey(0)



