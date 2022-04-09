import os.path

import requests
from flask import Flask, request, Response
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = '/media/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'bmp'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        # тут нужно обработать file_path - путь к сохранённому файлу
        requests.post('django:8000', data={
            'author': None,
            'fio':
        })
