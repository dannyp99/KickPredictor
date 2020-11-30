from flask import Flask, render_template, request
import numpy as np
import pickle
from flask_cors import CORS,cross_origin
import json
import pandas as pd


#initialize app and load model
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
encoder = pickle.load(open('encoder.pkl', 'rb'))

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

# @app.route('/pp', methods=['POST'])
# @cross_origin()
# def pp():
# 	print(request.data)
# 	return "leg"



@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
	req = json.loads(request.data)
	form = req['form']
	print(form)
	df = pd.DataFrame(form, index = [0])
	print(df)
	
	encoder.transform(df[['category', 'subcategory', 'month', 'day', 'hour', 'state']])
	
	# int_features = [int(x) for x in req['form'].values()]
	# #data translate here
	# final_features = [np.array(int_features)]
	# prediction = model.predict(final_features)
	# return render_template('index.html', prediction_text='Your kickstarter project is likely to: {}'.format(prediction[0]))
	



#start the server and run on localhost:5000
if __name__ == '__main__':
	app.run(debug=True)