# Import the required Libraries
import numpy as np
import cv2

# Capture the video from location
path=r"E:\ved\python\sample_video1.mp4"

video = cv2.VideoCapture(path)

# It will return frames
while video.isOpened():
    ret, frame = video.read()

    if not ret:
        print("Video Completed")
        break
    
    # Convert the frames into Grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('video original', frame)
    
    # Show the Grayscale frames
    cv2.imshow("Black and white video",gray)
     
    # Press q to exit the video  
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
        
video.release()
cv2.destroyAllWindows()