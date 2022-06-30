
import sys
import os
import uuid
from flask import Flask, render_template, flash, request, redirect,session
from preprocess import process_image
import tensorflow as tf
import numpy as np
import cv2

from werkzeug.utils import secure_filename
app = Flask(__name__)



# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


app.config["IMAGE_UPLOADS"] = "./uploads"

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/canva',methods=['POST'])
def draw():
    import canva.py
    return canva



@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
    if request.files:
      img = request.files['image']
      image_url=os.path.join(app.config["IMAGE_UPLOADS"],img.filename)
      img.save(image_url)
      img = process_image(image_url)
      cv2.imwrite('upload.jpg',img)

      img = cv2.imread('upload.jpg')
      resize = tf.image.resize(img, (256,256))
      
      json_file = open('models/model_structure.json','r')
      model_structure = json_file.read()
      json_file.close()
      model = tf.keras.models.model_from_json(model_structure)
      model.load_weights('models/model_weights.h5')
      pred = model.predict(np.expand_dims(resize/255, 0))
      p=str(pred)
      print(p)

    #   print(result)
    #   image_path = "uploads/" + img.filename
      return render_template("index.html")
   
   return render_template("index.html")


if __name__ == "__main__":
     app.run(debug = True)
