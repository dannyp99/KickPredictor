import calendar
import pickle as pkl
import pandas as pd
import numpy as np
import random
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.metrics import accuracy_score

seed = 42
random.seed(seed)
np.random.seed(seed)
#load datafile and create pickle file.
df = pd.read_csv('./kickstarter.csv')
file1 = open("model.pkl", "wb")
file2 = open("encoder.pkl", "wb")
file3 = open("scaler.pkl", "wb")

#convert months and days to a numeric equivalent.
months = list(calendar.month_name)
days = list(calendar.day_name)
df['month'] = df['month'].map(lambda x: months.index(x))
df['day'] = df['day'].map(lambda x: days.index(x))

#declare encoder for the non-numeric fields to be a binary.
encoder = OneHotEncoder(handle_unknown="ignore", sparse=False)
encoder.fit(df[['category', 'subcategory', 'month', 'day', 'hour', 'state']])

#Create the min max scalar and apply it to our parameters. Drop all uneeded columns and store the column to be predicted as our y.
X = df.drop(columns=['Unnamed: 0', 'id', 'title', 'category', 'subcategory', 'blurb', 'launch', 'deadline', 'state', 'city', 'backers', 'pledged', 'ongoing', 'location', 'success'])
columns = X.columns
X = pd.DataFrame(X, columns=columns)
y = df['success']

#separate training and testing data for the model.
kf = KFold(n_splits=10)
scaler = MinMaxScaler()
scaler.fit(X)
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=seed)
#Create model, train it, and test it.
model = HistGradientBoostingClassifier()#learning_rate=0.1, loss='binary_crossentropy', max_bins=255, max_depth=3, max_iter=100, max_leaf_nodes=31, min_samples_leaf=10)
#hyperparameters had slightly lower results of 71.96 average accuracy
model.fit(X,y)
pipeline = Pipeline([('scaler', scaler), ('HGB Classifier', model)])
score = cross_val_score(pipeline, X, y, cv=kf, scoring='accuracy').mean()
print(score)

#pickle the model for future use
pkl.dump(model, file1)
pkl.dump(encoder, file2)
pkl.dump(scaler, file3)
file1.close()
file2.close()
file3.close()