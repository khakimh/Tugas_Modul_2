from flask import Flask, render_template, request, send_from_directory
import os
from werkzeug.utils import secure_filename
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import plotly
import plotly.graph_objects as go 
# import chart_studio.plotly as py 
import json

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './file'

@app.route('/file/<path:path>')
def aksesFile(path):
    return send_from_directory ('file', path)

@app.route('/')
def home():
    return render_template ('home.html')

@app.route('/uploadmatplotlib', methods=['POST'])
def upload1():
	myFile = request.files['file']
	fn = secure_filename(myFile.filename)
	filex = str(np.random.rand(1)[0])[2:]
	if fn[-3:] == 'csv':
		df = pd.read_csv(myFile)
		plt.style.use('seaborn')
		plt.plot(list(df[df.columns[0]]), list(df[df.columns[1]]), 'b')
		plt.savefig('./file/{}.png'.format(filex))
		return render_template('result1.html', data='{}.png'.format(filex))
	else:
		return render_template ('error.html')

@app.route('/uploadplotly', methods=['POST'])
def upload2():
	myFile = request.files['file']
	fn = secure_filename(myFile.filename)
	if fn[-3:] == 'csv':
		df = pd.read_csv(myFile)
		plot = go.Scatter(x=list(df[df.columns[0]]), y=list(df[df.columns[1]]))
		plotJSON = json.dumps([plot],cls = plotly.utils.PlotlyJSONEncoder)
		return render_template ('result2.html', x = plotJSON)
	else:
		return render_template ('error.html')

if __name__ == '__main__':
    app.run(
        debug=True
    )