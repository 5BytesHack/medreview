import requests
import urllib
import easyocr
import PIL
import urllib.request
# url = 'https://avatars.mds.yandex.net/get-zen_doc/927575/pub_5ae4d1d6c3321b1f23ef2094_5ae4d2739e29a23794d8eab0/
# scale_1200'
# img = urllib.request.urlopen(url).read()
# out = open("img.jpg", "wb")
# out.write(img)
# out.close

# import library


# specify shortform of language you want to extract,
# I am using Hindi(hi) and English(en) here by list of language ids

reader = 'null'


def init_img_recognition_model():
    global reader
    reader = easyocr.Reader(['ru', 'en'])


# Read Image


# Doing OCR. Get bounding boxes.

def img_recognize_text(image_path):
    im = PIL.Image.open(image_path)  # provide your image path
    bounds = reader.readtext(image_path, detail=0)
    res = " ".join(bounds)
    return res
