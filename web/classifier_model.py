import keras
from keras_preprocessing.text import tokenizer_from_json
import os
import json
from sklearn.preprocessing import normalize
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

#text = ["Довожу до Вашего сведения, что (дата) на горячую линию обратилась клиент (ФИО, тел.) "
#        "с жалобой на правила предоставления услуги «Выезд на дом». Клиент оформила услугу "
#        "«Выезд на дом медицинской сестры» на (дата) Клиент недовольна тем, что ожидать медсестру необходимо с 7:00 до 12:00.  Клиент не смогла дождаться медицинской сестры по причине приема лекарственных препаратов по беременности и отменила вызов.  Клиент просит разобраться и принять меры.   Ждет звонка администрации"]

model = ''
tokenizer = ''

CUR_DIR = os.path.abspath(os.curdir)
MODEL_FOLDER = CUR_DIR + '/nnmodel'
TOKENIZER_PATH = CUR_DIR + '/tokenizer.json'


def load_model_and_tokenizer():
    global model
    global tokenizer
    model = keras.models.load_model(MODEL_FOLDER)
    with open(TOKENIZER_PATH) as f:
        data = json.load(f)
        tokenizer = tokenizer_from_json(data)


def classify(text: str) -> bool:
    matrix = tokenizer.texts_to_matrix(text, 'freq')
    X = normalize(matrix)

    result = model.predict(X)
    return result[0] >= 0.5

#print(classify(text))