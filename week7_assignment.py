#Nia Thompson | March 01 2025 | Data 300
#week 7 assignment: exercise model building (linear regression)

#imports
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import matplotlib.pyplot as plt

#PART 1: LR1: Dataset: kc_house_data.csv (from the multiple regression tutorial)

#loading the data
LR1_data = pd.read_csv ('kc_house_data.csv')

#selecting features and target variable
x = LR1_data[['sqft_living']]
y = LR1_data ['price']

#splitting the data into training and test sets
x_train, x_test, y_train, y_test = train_test_split (x, y, test_size= 0.8, random_state= 50)

#creating the linear regression model
LR1_model = LinearRegression()

#training the model
LR1_model.fit (x_train, y_train)

#printing the intercept and coefficient
print (f'LR1 Intercept: {LR1_model.intercept_}')
print (f'LR1 Coefficient: {LR1_model.coef_}')

#printing the accuracy
y_pred = LR1_model.predict (x_test)
r_squared = metrics.r2_score (y_test, y_pred)
print (f'LR1 R-Sqaured: {r_squared}')

#scatterplot visualization
plt.scatter (x, y)
plt.xlabel ('sqft_living')
plt.ylabel ('price')
plt.title ('Scatterplot of sqft_living vs price')
plt.show()

#actual vs predicted values visualization
plt.scatter (y_test, y_pred)
plt.xlabel ('Actual Prices')
plt.ylabel ('Predicted Prices')
plt.title ('Actual vs Predicted Prices')
plt.show()

#error plot visualizatiom
plt.hist (y_test - y_pred, bins = 30)
plt.xlabel ('Error')
plt.ylabel ('Frequency')
plt.title ('Distribution of Prediction Errors')
plt.show()

#PART 2: LR2: Dataset: student_scores.csv

#loading in the data
LR2_data = pd.read_csv ('student_scores.csv')

#selecting features and target variable
X = LR2_data[['Hours']]
Y= LR2_data ['Scores']

#splitting the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split (X, Y, test_size = 0.8, random_state = 50)

#screating the linear regression model
LR2_model = LinearRegression()

#fitting and training the model
LR2_model.fit (X_train, Y_train)

#printing the intercept and coefficient
print (f'LR2 Intercept: {LR2_model.intercept_}')
print (f'LR2 Coefficient: {LR2_model.coef_}')

#printing the accuracy
Y_pred = LR2_model.predict (X_test)
r_squared = metrics.r2_score (Y_test, Y_pred)
print (f'LR2 R-Squared: {r_squared}')

#scatterplot visualization
plt.scatter (X, Y)
plt.xlabel ('Hours')
plt.ylabel ('Scores')
plt.title ('Scatterplot of Hours vs Scores')
plt.show()

#actual vs predicted values visualization
plt.scatter (Y_test, Y_pred)
plt.xlabel ('Actual Scores')
plt.ylabel ('Predicted Scores')
plt.title ('Actual vs Predicted Scores')
plt.show()

#error plot visualizatiom
plt.hist (Y_test - Y_pred, bins = 30)
plt.xlabel ('Error')
plt.ylabel ('Frequency')
plt.title ('Distribution of Prediction Errors')
plt.show()