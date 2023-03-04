import cv2

# Load the pre-trained human detection mode1
hog = cv2.HOGDescripter()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# create a video capture object
cap = cv2.VideoCapture(0)

while True:
    # Read the video frame by frame
    ret,frame = cap.read()

    # Run the human detection model on the current frame
    human_rects, _ = hog.detectMultiscale(frame)

    # Draw a rectangle around each detected human
    for (x, y, w, h) in human_rects:
        cv2.rectangle(frame,(x, y), (x+w, y+h), (0, 255, 0), 2)

    #isplay the frame with the detected humans
    cv2.imshow('Human Detection', frame)

    # stop the program when 'q' is pressed
    if cv2.waitkey(1) == ord('q'):

# Released the video capture object andclose all windows
cap.release()
cv2.destroyAllWindows()
