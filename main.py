import cv2 as cv2
import numpy as np



if __name__ == "__main__":
    cap = cv2.VideoCapture("/Users/MattSparks/Documents/ImageRecognition/Video/Fruit.mov")
    if (cap.isOpened()== False): 
        print("Error opening video stream or file")
 
# Read until video is completed
    while(cap.isOpened()):
      # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
     
        # Display the resulting frame
            cv2.imshow('Frame',frame)
     
        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
     
      # Break the loop
        else: 
            breakpoint
 
    # When everything done, release the video capture object
    cap.release()
     
    # Closes all the frames
    cv2.destroyAllWindows()
    print("Finished Processing")
