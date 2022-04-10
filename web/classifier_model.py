import keras
from keras_preprocessing.text import tokenizer_from_json
import os
import json
from sklearn.preprocessing import normalize
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

text = ["Довожу до Вашего сведения, что (дата) на горячую линию обратилась клиент (ФИО, тел.) "
        "с жалобой на правила предоставления услуги «Выезд на дом». Клиент оформила услугу "
        "«Выезд на дом медицинской сестры» на (дата) Клиент недовольна тем, что ожидать медсестру необходимо с 7:00 до 12:00.  Клиент не смогла дождаться медицинской сестры по причине приема лекарственных препаратов по беременности и отменила вызов.  Клиент просит разобраться и принять меры.   Ждет звонка администрации"]


def classify(text: str) -> bool:

    model = keras.models.load_model('../backend/classifier/nnmodel')

    with open('tokenizer.json') as f:
        data = json.load(f)
        tokenizer = tokenizer_from_json(data)
        matrix = tokenizer.texts_to_matrix(text, 'freq')

        X = normalize(matrix)

    result = model.predict(matrix)
    return result[0] >= 0.5


print(classify(text))