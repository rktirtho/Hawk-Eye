import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, int(15))
fps = int(cap.get(5))
print("fps:", fps)

while(cap.isOpened()):

    ret,frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame', frame)

    k = cv2.waitKey(1)
    if k == 27:
        break