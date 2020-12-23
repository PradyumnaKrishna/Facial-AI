import cv2, base64
import numpy as np
from FER.predict import Model

# ----------------------------------------------------------------------------------
# Detect faces using OpenCV
# ----------------------------------------------------------------------------------
def detect_faces(img):
    '''Detect face(s) in an image'''

    faces_list = []

    # Convert the test image to gray scale (opencv face detector expects gray images)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Load OpenCV face detector (LBP is faster)
    face_cascade = cv2.CascadeClassifier('FER/haarcascade_frontalface_default.xml')

    # Detect multiscale images (some images may be closer to camera than others)
    # result is a list of faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);

    # If not face detected, return empty list
    if  len(faces) == 0:
        return faces_list

    for i in range(0, len(faces)):
        (x, y, w, h) = faces[i]
        face_dict = {}
        face_dict['face'] = gray[y:y + w, x:x + h]
        face_dict['rect'] = faces[i]
        faces_list.append(face_dict)

    # Return the face image area and the face rectangle
    return faces_list

# ----------------------------------------------------------------------------------
# Draw rectangle on image
# Write Emotion on Image
# according to given (x, y) coordinates and given width and height
# ----------------------------------------------------------------------------------
def edit_image(img, rect):
    '''Draw a rectangle(s) on the image and write their suitable emotions'''
    (x, y, w, h) = rect
    predictor = Model("FER/model.json", "FER/model_weights.h5")
    font = cv2.FONT_HERSHEY_SIMPLEX

    fr = img
    gray_fr = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)

    fc = gray_fr[y:y+h, x:x+w]

    roi = cv2.resize(fc, (48, 48))
    emotion = predictor.predict_emotion(roi[np.newaxis, :, :, np.newaxis])

    cv2.putText(img, emotion, (x, y), font, 1, (0, 255, 255), 2)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)

def rw_image(image, faces):
    # Edit the image
    for item in faces:
        edit_image(image, item['rect'])

    # Save
    #cv2.imwrite(filename, image)

    # In memory
    image_content = cv2.imencode('.jpg', image)[1].tostring()
    encoded_image = base64.encodestring(image_content)
    to_send = 'data:image/jpg;base64, ' + str(encoded_image, 'utf-8')

    return to_send