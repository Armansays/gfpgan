import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import replicate


UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000


@app.route("/")
def index():
    return render_template("index.html")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route("/", methods = ["post"])
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return "erorr"
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            return "eror"
        
        if file and allowed_file(file.filename):
            file = request.files['file']
            filename = secure_filename(file.filename)
            full_filename =  "." + url_for("static", filename= "images"+ filename)
            file.save(full_filename)
            redirect(url_for('static', filename='uploads/' + filename), code=301)
            return render_template("index.html")
   

        
if __name__ == "__main__":
    app.run(debug=True)