import time,cv2

face_cas = cv2.CascadeClassifier('C:\\Users\\Himank Jerolia\\Downloads\\opencv\\haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(0)

check, frame = video.read()
if check == True:
    print("Face has been detected.")
else:
    print("Face Not detected.")

gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

faces = face_cas.detectMultiScale(gray_image, scaleFactor=1.05, minNeighbors=5)

for x, y, w, h in faces:
    frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)

print(check)

time.sleep(3)

cv2.imshow("Capture", frame)

cv2.waitKey(0)

cv2.destroyAllWindows()

video.release()