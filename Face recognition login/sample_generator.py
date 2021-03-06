import cv2
import numpy as np


def main_function():
    face_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
    samples = []

    def sample_collector(img):    
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    
        if faces is ():
            return None
    
    # Crop all faces found
        for (x,y,w,h) in faces:
            cropped_face = img[y:y+h, x:x+w]

        return cropped_face

    cap = cv2.VideoCapture(0)
    count = 0

# Collect 100 samples of your face from webcam input
    while True:

        ret, frame = cap.read()
        if sample_collector(frame) is not None:
            count += 1
            face = cv2.resize(sample_collector(frame), (200, 200))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            samples.append(face)

            #rint(face)

        # Put count on images and display live count
            cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            cv2.imshow('Face', face)
         
        else:
        #print("Face not found")
            pass

        if cv2.waitKey(1) == 13 or count == 100: 
            break
        
        #print(samples)

    cap.release()
    cv2.destroyAllWindows()      
    print("Collecting Samples Complete")

    #print(samples)
    return samples

