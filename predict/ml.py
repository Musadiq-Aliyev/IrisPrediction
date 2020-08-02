# Load modules
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pandas as pd

# Load dataset
df = pd.read_csv(r'C:\Users\003560\Desktop\IrisPrediction\predict\iris.csv')

# Split into training data and test data
X = df[['sepal_length','sepal_width','petal_length','petal_width']]
y = df['classification']


X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.20, random_state=1)


model = SVC(gamma='auto')
model.fit(X_train, Y_train)


predictions = model.predict(X_test)


# Pickle model
pd.to_pickle(model,r'C:\Users\003560\Desktop\IrisPrediction\predict\new_model.pickle')
