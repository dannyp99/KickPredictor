import calendar
import pickle as pkl
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.model_selection import train_test_split
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
X = df.drop(columns=['Unnamed: 0', 'id', 'title', 'category', 'subcategory', 'blurb', 'launch', 'deadline', 'state', 'city', 'backers', 'pledged', 'ongoing', 'success'])
columns = X.columns
X = pd.DataFrame(scaler.fit_transform(X), columns=columns)
y = df['success']
#separate training and testing data for the model.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Create model, train it, test it, and pickle it.
model = HistGradientBoostingClassifier() #note parameters need to be added
model.fit(X_train,y_train)
y_predict = model.predict(X_test)
score = accuracy_score(y_predict,y_test)
print("Accuracy Score:", score)
pkl.dump(encoder, file)
file.close()