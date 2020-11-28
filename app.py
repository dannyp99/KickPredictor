from flask import Flask, render_template
import numpy as np
import pickle

#initialize app and load model
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
encoder = pickle.load(open('encoder.pkl', 'rb'))

#routes
@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
	int_features = [int(x) for x in request.form.values()]
	#data translate here
	final_features = [np.array(int_features)]
	prediction = model.predict(final_features)
	return render_template('index.html', prediction_text='Your kickstarter project is likely to: {}'.format(prediction[0]))

#start the server and run on localhost:5000
if __name__ == '__main__':
	app.run(debug=True)