# import the opencv library 
import cv2 
import numpy as np
cascade=cv2.CascadeClassifier('D:\\PROJECT\\Face detection live\\haarcascade_frontalface_default.xml')
  
# define a video capture object 
vid = cv2.VideoCapture(0)
vid_cod = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter("D:\\PROJECT\\Face detection live\\cam_video.mp4", vid_cod, 20.0, (640,480))
while(True): 
      
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read() 
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    eyes=cascade.detectMultiScale(gray,1.3,5)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(0,0,255),3)
    # Display the resulting frame 
    cv2.imshow('frame', frame) 
    output.write(frame)  
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 

