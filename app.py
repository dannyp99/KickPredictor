from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle
from flask_cors import CORS,cross_origin
import json
import pandas as pd


#initialize app and load model
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
encoder = pickle.load(open('encoder.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
sample = pd.read_csv('./sampleEntry.csv')
encoded_cols = ['category', 'subcategory', 'month', 'day', 'hour', 'state']
droplist = ['state', 'category', 'subcategory']

cors = CORS(app)


app.config['CORS_HEADERS'] = 'Content-Type'


#routes
@app.route('/')
@cross_origin()
def home():
	return render_template('index.html')


@app.after_request
def after_request(response):
	response.headers['Access-Control-Allow-Origin'] = '*'
	print("gjkhghjhkj",response.headers)
	return response

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
	req = json.loads(request.data)
	form = req['form']
	print(form)
	df = pd.DataFrame(form, index = [0])
	print(df)
	transformed_cols = encoder.transform(df[encoded_cols])
	for key in droplist:
		if key in form:
			del form[key]
	nontransformed = list(form.values())
	print(transformed_cols)
	nontransformed.extend(*transformed_cols)
	print(nontransformed)
	sampleData = scaler.transform(np.array(nontransformed).reshape(1,-1))
	prediction = model.predict(sampleData)
	print(prediction)
	return jsonify(str(prediction[0]))
	

#start the server and run on localhost:5000
if __name__ == '__main__':
	app.run(debug=True)