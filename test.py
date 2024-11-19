import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Camera failed to open.")
else:
    while True:
        success, img = cap.read()
        if not success:
            break
        cv2.imshow("Test", img)
        if cv2.waitKey(1) & 0xFF == 27:  # Exit on an ESC key
            break
cap.release()
cv2.destroyAllWindows()
