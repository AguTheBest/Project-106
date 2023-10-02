import cv2


# Create our body classifier
face_cascade = cv2.CascadeClassifier("haarcascade_fullbody.xml")

# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')

# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = cap.read()

    #Convert Each Frame into Grayscale
    grayframe = cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
    # Pass frame to our body classifier
    faces = face_cascade.detectMultiScale(grayframe,1.7,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
    
    # Extract bounding boxes for any bodies identified
    cv2.imshow("webcam",frame)

    if cv2.waitKey(1) == 32: #32 is the Space Key
        break

cap.release()
cv2.destroyAllWindows()
