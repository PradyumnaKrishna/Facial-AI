import base64
import cv2
import io

import matplotlib.pyplot as plt
import numpy as np

from FER.predict import Model


# ----------------------------------------------------------------------------------
# Basic Processing/Conversions of image
# ----------------------------------------------------------------------------------
def process_image(file):
    # because imghdr.what() reads file to end, must set file's position 0.
    # some other function also reads the file to end
    file.seek(0)

    # Read Image
    image = cv2.imdecode(np.fromstring(
        file.read(), np.uint8), cv2.IMREAD_UNCHANGED)

    # Resizing Factor
    f1, f2 = 1200 / image.shape[1], 600 / image.shape[0]
    f = min(f1, f2, 1)

    # Resize Image
    dim = (int(image.shape[1] * f), int(image.shape[0] * f))
    image = cv2.resize(image, dim)

    # Return Image
    return image


# ----------------------------------------------------------------------------------
# Detect faces using OpenCV
# ----------------------------------------------------------------------------------
def detect_faces(file):
    """Detect face(s) in an image"""

    faces_dict = {}

    # Read image
    image = process_image(file)

    # Convert the image into gray scale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load OpenCV face detector (LBP is faster)
    face_cascade = cv2.CascadeClassifier(
        'FER/haarcascade_frontalface_default.xml')

    # Detect multiple faces (some images may be closer to camera than others)
    # result is a list of faces
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.2, minNeighbors=5)

    # If not face detected, return empty list
    if len(faces) == 0:
        return faces, gray

    coords = ['x', 'y', 'w', 'h']

    for i in range(0, len(faces)):
        faces_dict[i] = {'coordinates': dict(zip(coords, faces[i].tolist()))}

    # Return the face image area and the face rectangle
    return faces_dict, gray


# ----------------------------------------------------------------------------------
# Plot the Graph for Analysis
# ----------------------------------------------------------------------------------
def plot(probs, width=0.8):
    """ plotting a bar chart of prediction probability """
    plt.switch_backend('Agg')

    # Emotion List
    emotions = Model.EMOTIONS_LIST

    # no of Probabilities
    n = len(probs)
    # numpy array as long as no of emotions
    X = np.arange(len(emotions))
    # width of a bar
    width = width/n

    # plot bar graph for 'n' faces
    for i in range(n):
        plt.bar(X + (i*width), probs[i], width=width, label=f'Face {i}')

    # place the x ticks
    plt.xticks(X + (n-1)*width/2, emotions)

    # y axis range
    plt.ylim(0, 1)

    # naming the axis
    plt.ylabel('Probability')
    plt.xlabel('Emotions')

    # Add Legend
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.17),
               fancybox=True, shadow=True, ncol=5)

    # Convert Graph into Numpy Array
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    graph_arr = np.frombuffer(buf.getvalue(), dtype=np.uint8)
    buf.close()

    # Encode the graph into base64
    graph = base64.encodebytes(graph_arr)
    graph = 'data:image/png;base64, ' + str(graph, 'utf-8')
    return graph


# ----------------------------------------------------------------------------------
# Predict Emotion for face(s)
# ----------------------------------------------------------------------------------
def predict(faces_dict, img):
    """ Draw a rectangle(s) on the image and write their suitable emotions """
    # Load the Model
    predictor = Model("FER/model.json", "FER/model_weights.h5")
    emotions = predictor.EMOTIONS_LIST

    for f, detail in faces_dict.items():
        # decalaring face coordiantes as variables
        (x, y, w, h) = detail['coordinates'].values()

        # Select only Face
        fc = img[y:y + h, x:x + w]

        # Convert image into 48x48 and predict Emotion
        roi = cv2.resize(fc, (48, 48))
        emotion, prob = predictor.predict_emotion(
            roi[np.newaxis, :, :, np.newaxis])

        # add emotion and probability to faces_dict
        faces_dict[f]['emotion'] = emotion
        faces_dict[f]['probability'] = dict(zip(emotions, prob.tolist()))


# ----------------------------------------------------------------------------------
# Draw rectangle on image
# Write Emotion on Image
# according to given (x, y) coordinates and given width and height
# ----------------------------------------------------------------------------------
def edit_image(file, data):
    """ Draw a rectangle(s) on the image and write their suitable emotions """
    # Process Image
    image = process_image(file)

    probabilities = []

    # Font type
    font = cv2.FONT_HERSHEY_SIMPLEX

    for i, detail in data.items():
        # Variable Declaration
        (h, w, x, y) = detail['coordinates'].values()
        emotion = detail['emotion']

        # Text Modification
        font_size = h/300 if h/300 > 0.6 else 0.6

        # Draw Rectangle and Write Text
        cv2.putText(image, emotion, (x, y-4), font, font_size, (0, 255, 255), 2)
        cv2.putText(image, i, (x+2, y+h-4), font, font_size, (237, 162, 0), 2)
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 165, 255), 2)

        # append probabilities
        probabilities.append(detail['probability'].values())

    # Convert Image into base64
    image_content = cv2.imencode('.jpg', image)[1].tostring()
    encoded_image = base64.encodebytes(image_content)
    image = 'data:image/jpg;base64, ' + str(encoded_image, 'utf-8')

    # Plot Graph
    graph = plot(probabilities)

    # Return Image and Graph
    return image, graph
