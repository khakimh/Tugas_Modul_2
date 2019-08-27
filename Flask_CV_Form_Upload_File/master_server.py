from flask import Flask, render_template, abort, redirect, jsonify, request, send_from_directory
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './file'

@app.errorhandler(404)
def not_found(x):
    return render_template('error.html')

@app.route('/file/<path:path>')
def aksesFile(path):
    return send_from_directory ('file', path)

@app.route('/')
def landing_page():
    return render_template('index.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/uploads')
def uploads():
    return render_template('upload.html')

@app.route('/forms')
def forms():
    return render_template('form.html')

@app.route('/form', methods = ['POST'])
def form():
    data = request.form
    return render_template ('result.html',data=data)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
	myFile = request.files['file']
	fn = secure_filename(myFile.filename)
	myFile.save(os.path.join(app.config['UPLOAD_FOLDER'], fn))
	return render_template ('success.html',data=fn)

if __name__ == '__main__':
    app.run(
        debug=True
    )