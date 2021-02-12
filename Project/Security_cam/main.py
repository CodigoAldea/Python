import cv2
import winsound
import datetime

x = str(datetime.datetime.now())
cam = cv2.VideoCapture(0)
# video recording module 
fourcc = cv2.VideoWriter_fourcc('X','V', 'I', 'D')
out = 'C:/Python/Project/Security_cam/recording.avi'
out = cv2.VideoWriter(x+out,fourcc, 20,(370,720),False)

while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()q
    diff = cv2.absdiff(frame1, frame2)
    grey = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(grey, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    out.write(frame1)
    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    for c in contours:
        if cv2.contourArea(c) < 2000:
            continue
        x, y , w, h =cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # winsound.Beep(500, 200)
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('cam', frame1)
