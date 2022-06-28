# from predict_parkinsons import predict_image
import sys
import os
import uuid
from flask import Flask, render_template, flash, request, redirect,session


from werkzeug.utils import secure_filename
app = Flask(__name__)
# # paths to different models
# spiralModel = os.path.join("models/", "random_forest_spiral_model.pkl")
# waveModel = os.path.join("models/", "random_forest_wave_model.pkl")

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods = ['POST'])
def upload_image():
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No image selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #print('upload_image filename: ' + filename)
            flash('Image successfully uploaded and displayed below')
            return render_template('index.html', filename=filename)
        else:
            flash('Allowed image types are - png, jpg, jpeg, gif')
            return redirect(request.url)





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
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'

# def upload_file():
#    if request.method == 'POST':
#       f = request.files['file']
#       f.save(secure_filename(f.filename))
#       return 'file uploaded successfully'


if __name__ == "__main__":
    #  app.secret_key = 'super secret key'
    #  app.config['SESSION_TYPE'] = 'filesystem'

    #  session.init_app(app)
     app.run(debug = True)
