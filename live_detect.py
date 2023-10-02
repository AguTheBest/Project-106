# import the opencv library
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Define a video capture object
vid = cv2.VideoCapture(0)

while(True):
   
    # Capture the video frame by frame
    ret, frame = vid.read()
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayframe)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
    # Display the resulting frame
    cv2.imshow("Web cam", frame)
      
    # Quit Window by Spacebar Key
    if cv2.waitKey(25) == 27:
        break
  
# After the loop release the cap object
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()