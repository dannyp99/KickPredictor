import calendar
import pickle as pkl
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import accuracy_score

#load datafile and create pickle file.
df = pd.read_csv('./kickstarter.csv')
file = open("model.pkl", "wb")

#declare encoder for the non-numeric fields to be a binary.
encoder = OneHotEncoder()
encoder.fit(df[['category', 'subcategory', 'month', 'day', 'hour', 'state']])

#convert months and days to a numeric equivalent.
months = list(calendar.month_name)
days = list(calendar.day_name)
df['month'] = df['month'].map(lambda x: months.index(x))
df['day'] = df['day'].map(lambda x: days.index(x))

#Create the min max scalar and apply it to our parameters. Drop all uneeded columns and store the column to be predicted as our y.
scaler = MinMaxScaler()
X = df.drop(columns=['Unnamed: 0', 'id', 'title', 'category', 'subcategory', 'blurb', 'launch', 'deadline', 'state', 'city', 'backers', 'pledged', 'ongoing', 'location', 'success'])
columns = X.columns
X = pd.DataFrame(scaler.fit_transform(X), columns=columns)
y = df['success']

#separate training and testing data for the model.
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#Create model, train it, and test it.
kf = KFold(n_splits=5)
kf.get_n_splits(X)
model = HistGradientBoostingClassifier()#learning_rate=0.1, loss='binary_crossentropy', max_bins=255, max_depth=3, max_iter=100, max_leaf_nodes=31, min_samples_leaf=10)
#hyperparameters had slightly lower results of 71.96 average accuracy
print(kf)
score_list = []
for train_index, test_index in kf.split(X):
	print("TRAIN:", train_index, "TEST:", test_index)
	X_train, X_test = X.loc[train_index], X.loc[test_index]
	y_train, y_test = y[train_index], y[test_index]
	model.fit(X_train,y_train)
	y_predict = model.predict(X_test)
	score = accuracy_score(y_predict,y_test)
	score_list.append(score)
	print("Accuracy Score:", score)
print("Score List:", score_list)
print("Average:", np.average(score_list))

#pickle the model for future use
pkl.dump(encoder, file)
file.close()