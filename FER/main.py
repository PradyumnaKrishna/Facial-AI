from flask import Blueprint, render_template, request, flash, redirect

from FER.edit import rw_image

fer = Blueprint('fer', __name__)

# Image file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


# Check for the file uploaded is an image
def allowed_file(name):
    return '.' in name and name.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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

    # Check for the file uploaded and is an image
    # TODO: Improve file type check
    if file and allowed_file(file.filename):
        # Takes the No of faces and Edited Image
        num_faces, image, graph = rw_image(file)

        # If No of faces 0 then print 'No Face Detected'
        if num_faces == 0:
            flash('Sorry, No face detected', 'danger')
            return redirect(request.url)

        # Else Print No of Faces and the image
        else:
            flash('Yes! ' + str(num_faces) + ' face(s) detected!', 'success')
            return render_template('fer.html', image_to_show=image,
                                   graph_to_show=graph)

    # If not an image
    else:
        flash('Please upload supported formats, e.g. png, jpg or jpeg', 'danger')
        return redirect(request.url)

    # Save file
    # filename = 'static/' + file.filename
    # file.save(filename)


if __name__ == "__main__":
    # Only for debugging while developing
    fer.run(host='0.0.0.0', debug=True, poexrt=80)
