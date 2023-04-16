import cv2
import os
from cvzone import HandTrackingModule, overlayPNG
import numpy as np

# Read images from a folder
folderpath = 'frames'
mylist = os.listdir(folderpath)
graphic = [cv2.imread(f'{folderpath}/{inpath}') for inpath in mylist]
intro = graphic[0];  # Read frames\img 1 in the intro variable
kill = graphic[1];  # Read frames\img 2 in the kill variable
winner = graphic[2];  # Read frames\img 3 in the winner variable

# Read the camera
cam = cv2.VideoCapture(0)
detector = HandTrackingModule.HandDetector(maxHands=1, detectionCon=0.77)
# Sets the minimum confidence threshold for the detection

# Initializing game components
folderpath2 = 'img'
mylist2 = os.listdir(folderpath2)
graphic2 = [cv2.imread(f'{folderpath2}/{inpath2}') for inpath2 in mylist2]
sqr_img = graphic2[1];  # Read img\sqr (1) in the sqr_img variable
mlsa = graphic2[0];  # Read img\mlsa in the mlsa variable

# INTRO SCREEN WILL STAY UNTIL Q IS PRESSED
cv2.imshow('Cookie Cutter', cv2.resize(intro, (0, 0), fx=0.67, fy=0.67))
cv2.waitKey(1)
while True:
    cv2.imshow('Cookie Cutter', cv2.resize(intro, (0, 0), fx=0.67, fy=0.67))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# GAME LOGIC UPTO THE TEAMS
# -


gameOver = False
NotWon = True
while not gameOver:
    continue

if NotWon:
    # LOSS SCREEN
    for i in range(10):
        cv.imshow('Cookie Cutter', cv2.resize(kill, (0, 0), fx=0.67, fy=0.67))
    while True:
        cv.imshow('Cookie Cutter', cv2.resize(kill, (0, 0), fx=0.67, fy=0.67))
        if cv.waitKey(10) & 0xFF == ord('q'):
            break
    # Show the loss screen from the kill image read before and end it after we press q
else:
    # WIN SCREEN
    cv.imshow('Cookie Cutter', cv2.resize(winner, (0, 0), fx=0.67, fy=0.67))
    cv.waitKey(125)
    # Show the win screen from the winner image read before
    while True:
        cv.imshow('Cookie Cutter', cv2.resize(winner, (0, 0), fx=0.67, fy=0.67))
        if cv.waitKey(10) & 0xFF == ord('q'):
            break
        # End it after we press q

# Destroy all the windows
cv.destroyAllWindows()