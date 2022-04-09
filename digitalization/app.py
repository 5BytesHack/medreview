import os.path
import json

import requests
from flask import Flask, request
from werkzeug.utils import secure_filename
from flask_cors import CORS

from digitalizer import init_img_recognition_model, img_recognize_text


UPLOAD_FOLDER = os.path.abspath(os.curdir) + '/media'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'bmp', 'webp'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
init_img_recognition_model()
CORS(app)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/upload/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['image']
        form = request.form
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        recognized = img_recognize_text(file_path)
        os.remove(file_path)
        requests.post('django:8000/createreview', data={
            'author': None,
            'fio': form['fio'],
            'mail': form['email'],
            'text': recognized
        })
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


app.run(debug=True, port=5000)
