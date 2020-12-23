import os, cv2
import numpy as np
from flask import Blueprint, render_template, request, flash, redirect
from FER.edit import rw_image, detect_faces

fer = Blueprint('fer', __name__)
#UPLOAD_FOLDER = os.path.basename('uploads')
#fer.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@fer.route("/")
def start_page():
    print("Start")
    return render_template('fer.html')

@fer.route('/', methods=['POST'])
def upload_file():
    file = request.files['image']
    if file.filename == '':
        flash('No image selected', 'danger')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        # Read image
        image = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)

        # Detect faces
        faces = detect_faces(image)

        if len(faces) == 0:
            flash('Sorry, No face Detected', 'danger')
            return redirect(request.url)
        else:
            num_faces = len(faces)
            to_send = rw_image(image, faces)

        flash('Yes! '+str(num_faces)+' face(s) detected!', 'success')
        return render_template('fer.html', image_to_show=to_send)
    else:
        flash('Please upload supported formats, e.g. png, jpg or jpeg', 'danger')
        return redirect(request.url)

    # Save file
    #filename = 'static/' + file.filename
    #file.save(filename)

    

if __name__ == "__main__":
    # Only for debugging while developing
    fer.run(host='0.0.0.0', debug=True, port=80)
