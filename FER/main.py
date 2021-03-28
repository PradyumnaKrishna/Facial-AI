import imghdr
import requests

from flask import Blueprint, flash, jsonify, redirect, render_template, request

from FER.edit import edit_image, detect_faces, predict

fer = Blueprint('fer', __name__)

# Image file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
api_url = 'http://127.0.0.1:5000/FER/api/v1/'


# Check for the file uploaded is an image
def allowed_file(file):
    image_type = imghdr.what(None, file.read())
    return image_type in ALLOWED_EXTENSIONS


# Main Page
@fer.route("/")
def start_page():
    print("Start")
    return render_template('fer.html')


# Upload Image (Post Form)
@fer.route('/', methods=['POST'])
def upload_file():
    # Load the file
    file = request.files['image']

    # Check 'the file is uploaded?'
    if file.filename == '':
        flash('No image selected', 'danger')
        return redirect(request.url)

    # api call through requests
    r = requests.post(api_url, files={'image': file})

    message = r.json()['message']

    # if there is no data in response
    if 'data' not in r.json():
        # flash message and return response
        flash(message, 'danger')
        return redirect(request.url)

    # edit the image and create a graph
    image, graph = edit_image(file, r.json()['data'])

    # flash message and return response
    flash(message, 'success')
    return render_template('fer.html', image_to_show=image,
                           graph_to_show=graph)


@fer.route('/api/v1/', methods=['POST'])
def api():
    # Load the file
    if 'image' not in request.files:
        return jsonify({'message': 'no image added'}), 400

    file = request.files['image']

    # Check for the file uploaded and is an image
    if file and allowed_file(file):
        # Detect Faces and Get Processed Image
        faces, image = detect_faces(file)

        # If no faces
        if len(faces) == 0:
            return jsonify({'message': 'Sorry, No face detected'}), 200
        else:
            # updates the dict, via call by value
            predict(faces, image)

            # return json response
            return jsonify({'message': f'Yes! {len(faces)} face(s) detected!',
                            'data': faces}), 200

    # If not an image
    return jsonify({
        'message': 'Please upload a valid image, e.g. png, jpg or jpeg'}), 400


if __name__ == "__main__":
    # Only for debugging while developing
    fer.run(host='0.0.0.0', debug=True, port=5000)
