from ntpath import join
from pickle import TRUE
from flask import(
    Flask, 
    render_template, 
    request, 
    url_for
)
from werkzeug.utils import secure_filename
from hashlib import md5
from time import time
from PIL import Image

#start flask app
app = Flask(__name__)
app.config["UPLOAD_FOLDER"]= './static/media/'

# start flask route

@app.route('/',methods=["GET","POST"])
def index():
    if request.method=="POST":
        FileObject = request.files['file']
        mimetype = FileObject.mimetype
        if FileObject.mimetype == "image/jpeg":
            filename = join(app.config["UPLOAD_FOLDER"],
            secure_filename(md5(str(time()).encode()).hexdigest()+'.png'))
            FileObject = Image.open(FileObject)
            FileObject.save(filename)
            return render_template('index.html',filename=filename)
        else:
            return render_template('index.html',mimetype=mimetype)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)