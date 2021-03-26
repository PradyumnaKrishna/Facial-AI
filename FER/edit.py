import cv2
import base64
import numpy as np
import matplotlib.pyplot as plt

from FER.predict import Model


# ----------------------------------------------------------------------------------
# Detect faces using OpenCV
# ----------------------------------------------------------------------------------
def detect_faces(img):
    """Detect face(s) in an image"""

    faces_list = []

    # Convert the image into gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Load OpenCV face detector (LBP is faster)
    face_cascade = cv2.CascadeClassifier(
        'FER/haarcascade_frontalface_default.xml')

    # Detect multiple faces (some images may be closer to camera than others)
    # result is a list of faces
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.2, minNeighbors=5)

    # If not face detected, return empty list
    if len(faces) == 0:
        return faces_list

    for i in range(0, len(faces)):
        faces_list.append(faces[i])

    # Return the face image area and the face rectangle
    return faces_list


# ----------------------------------------------------------------------------------
# Draw rectangle on image
# Write Emotion on Image
# according to given (x, y) coordinates and given width and height
# ----------------------------------------------------------------------------------
def edit_image(img, coords, preds=[]):
    """ Draw a rectangle(s) on the image and write their suitable emotions """
    (x, y, w, h) = coords

    # Load the Model
    predictor = Model("FER/model.json", "FER/model_weights.h5")

    # Text Modification
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_size = h/300 if h/300 > 0.6 else 0.6

    # Convert image into Grayscale
    gray_fr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Select only Face
    fc = gray_fr[y:y + h, x:x + w]

    # Convert image into 48x48 and predict Emotion
    roi = cv2.resize(fc, (48, 48))
    emotion, pred = predictor.predict_emotion(
        roi[np.newaxis, :, :, np.newaxis])
    preds.append(pred)

    # Draw Rectangle and Write Emotion
    cv2.putText(img, emotion, (x, y-2), font, font_size, (0, 255, 255), 2)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 165, 255), 2)


# ----------------------------------------------------------------------------------
# Plot the Graph for Analysis
# ----------------------------------------------------------------------------------
def plot(preds, width=0.8):
    """ plotting a bar chart of prediction probability """
    plt.switch_backend('Agg')
    emotions = Model.EMOTIONS_LIST

    n = len(preds)
    X = np.arange(len(emotions))

    # plot bar graph for 'n' faces
    bar = []
    for i in range(n):
        bar.append(plt.bar(X - width/2. + i/float(n)*width, preds[i],
                   tick_label=emotions, width=width/float(n), align="edge"))

    # y axis range
    plt.ylim(0, 1)

    # naming the axis
    plt.ylabel('Probability')
    plt.xlabel('Emotions')

    # Add title
    plt.title('Graphical Visualization')

    # Add Legend
    face_nos = [f'Face {i+1}' for i in range(len(bar))]
    plt.legend(bar, face_nos)

    # Save the image
    plt.savefig('plot.png')


# ----------------------------------------------------------------------------------
# Read and Write Process for image
# ----------------------------------------------------------------------------------
def rw_image(file):
    # Read image
    image = cv2.imdecode(np.fromstring(
        file.read(), np.uint8), cv2.IMREAD_UNCHANGED)

    # Resizing Factor
    f1, f2 = 1200 / image.shape[1], 600 / image.shape[0]
    f = min(f1, f2, 1)

    # Resize Image
    dim = (int(image.shape[1] * f), int(image.shape[0] * f))
    image = cv2.resize(image, dim)

    # Detect faces
    faces = detect_faces(image)

    # predictions
    preds = []

    # If no face detected return 0 and None
    if len(faces) == 0:
        return 0, None
    else:
        # Edit the image
        for coords in faces:
            # Call by value
            edit_image(image, coords, preds)
        plot(preds)

        # Save
        # cv2.imwrite(filename, image)

        # Process Image for Printing
        image_content = cv2.imencode('.jpg', image)[1].tostring()
        encoded_image = base64.encodebytes(image_content)
        to_send = 'data:image/jpg;base64, ' + str(encoded_image, 'utf-8')

        return len(faces), to_send
