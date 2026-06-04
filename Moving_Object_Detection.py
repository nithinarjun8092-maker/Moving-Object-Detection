import cv2 #openCV
import time #delay
import imutils #resize

cam=cv2.VideoCapture(0) #Cam Integration
time.sleep(1)

firstframe=None
area=500

while True:
    _,img = cam.read() #read from camera
    text = "Normal"
    img = imutils.resize(img,width=1000) #resize
    grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #colour to grayscale image
    gaussianimg = cv2.GaussianBlur(grayimg,(21,21),0) #smoothened
    if firstframe is None:
        firstframe = gaussianimg #Capturing the first frame
        continue
    imgdiff = cv2.absdiff(firstframe,gaussianimg) #absolute difference
    treshimg = cv2.threshold(imgdiff,25,255, cv2.THRESH_BINARY)[1]
    treshimg = cv2.dilate(treshimg,None,iterations=20) #left over - erotion or dilation
    cnts = cv2.findContours(treshimg.copy(), cv2.RETR_EXTERNAL, #make complete contours
                         cv2.CHAIN_APPROX_SIMPLE )
    cnts = imutils.grab_contours(cnts)
    for c in cnts:
        if cv2.contourArea(c) < area: #make full area
            continue
        (x,y,w,h)=cv2.boundingRect(c)
        cv2.rectangle(img,(x,y),(x+w,y+h),(1,255,0),2)
        text = "Moving Object Detected"
    print(text)
    cv2.putText(img,text,(10,20),
                cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
    cv2.imshow("Camera Feed",img)
    key=cv2.waitKey(1) & 0xFF
    if key == ord ("q"):
        break
cam.release()
cv2.destroyAllWindows()
