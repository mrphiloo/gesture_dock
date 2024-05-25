import urllib.request
import cv2

# Connect to camera (0 for internal, 1 for external)
cap = cv2.VideoCapture(0)

from cvzone.HandTrackingModule import HandDetector

# Initialize hand detector with a maximum of 1 hand and a minimum confidence threshold of 0.8
detector = HandDetector(maxHands=1, detectionCon=0.8)

while True:
    ret, photo = cap.read()  # Capture image and store status & image in a variable
    hand = detector.findHands(photo, draw=False)  # Find hand in the captured image
    hand = hand[0]
    
    if hand:
        detectHand = hand[0]  # imlist: imlist refers to a list containing information about the detected hand landmarks
        
        if detectHand:
            fingerUp = detector.fingersUp(detectHand)  # Based on the detected hand landmarks, find out which fingers are up
            
            # Thumb, Index finger, Middle finger, Ring finger, Pinky finger
            if fingerUp == [0, 1, 0, 0, 0]:
                request_lock = urllib.request.urlopen('https://mjckgm76ve.execute-api.ap-south-1.amazonaws.com/test/docker')
                print(request_lock.read())
                print(" + One Container Launched")
            
            elif fingerUp == [0, 1, 1, 0, 0]:
                for i in range(2):
                    request_lock = urllib.request.urlopen('https://mjckgm76ve.execute-api.ap-south-1.amazonaws.com/test/docker')
                    print(request_lock.read())
                print(" + Two Containers Launched")
            
            elif fingerUp == [0, 0, 1, 1, 1]:
                for i in range(3):
                    request_lock = urllib.request.urlopen('https://mjckgm76ve.execute-api.ap-south-1.amazonaws.com/test/docker')
                    print(request_lock.read())
                print(" + Three Containers Launched")
            
            elif fingerUp == [0, 1, 1, 1, 1]:
                for i in range(4):
                    request_lock = urllib.request.urlopen('https://mjckgm76ve.execute-api.ap-south-1.amazonaws.com/test/docker')
                    print(request_lock.read())
                print(" + Four Containers Launched")
            
            elif fingerUp == [1, 1, 1, 1, 1]:
                for i in range(5):
                    request_lock = urllib.request.urlopen('https://mjckgm76ve.execute-api.ap-south-1.amazonaws.com/test/docker')
                    print(request_lock.read())
                print(" + Five Containers Launched")

    cv2.imshow("pic", photo)  # Show image
    if cv2.waitKey(100) == 13:  # Keep the image for 100 milliseconds - stop if Enter key is pressed
        break
        
cv2.destroyAllWindows()  # Close all OpenCV windows
cap.release()  # Disconnect the camera
