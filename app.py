from flask import Flask, render_template
import pickle

#initialize app and load model
app = Flask(__name__)
#model = pickle.load(open('model.pkl', 'rb')) #uncomment when pkl file is created

#routes
@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
	print('predict Not Implemented')
	return None

#start the server and run on localhost:5000
if __name__ == '__main__':
	app.run(debug=True)