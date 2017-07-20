import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)

width = cap.get(3)
height = cap.get(4)
frame_title = 'frame {0}x{1}'.format(width, height)
cv2.namedWindow(frame_title)

font = cv2.FONT_HERSHEY_SIMPLEX

num_frames = 30

print("Press q to quit")

fps = 0
quit = False
while(not quit):
    start = time.time()

    for i in xrange(0, num_frames):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Converts image to gray
        bigger = cv2.resize(frame,None,fx=1.5, fy=1.5, interpolation = cv2.INTER_CUBIC)
        imgray = cv2.cvtColor(bigger, cv2.COLOR_BGR2GRAY)
        ret,thresh = cv2.threshold(imgray,127,255,0)
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        img = imgray
        if len(contours) > 0:
            cv2.drawContours(img, contours, -1, (0,255,0), 1)

        cv2.putText(img,'{0} fps'.format(fps), (10, 50), font, 1, (0, 0, 0), 2)
        # Display the resulting frame
        cv2.imshow(frame_title, img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            quit = True
            break

    end = time.time()
    seconds = end - start
    fps = round(num_frames / seconds)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
