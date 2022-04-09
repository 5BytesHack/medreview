import os.path

import requests
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

from digitalizer import init_img_recognition_model, img_recognize_text


UPLOAD_FOLDER = os.path.abspath(os.curdir) + '/media'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'bmp', 'webp'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
init_img_recognition_model()



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/fuck/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['image']
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        recognized = img_recognize_text(file_path)
        os.remove(file_path)
        # requests.post('django:8000', data={
        #     'author': None,
        #   #  'fio':
        # })
        return jsonify({'text': recognized})

app.run(debug=True)