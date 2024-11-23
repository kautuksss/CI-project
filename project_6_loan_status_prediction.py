# -*- coding: utf-8 -*-
"""Project 6. Loan Status Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11Fs72ZP-vX36UnfbJrmXoKxNGdaid4wN

Importing the Dependencies
"""

import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

"""Data Collection and Processing"""

# loading the dataset to pandas DataFrame
loan_dataset = pd.read_csv('/absolute/path/to/train_u6lujuX_CVtuZ9i (1).csv')

type(loan_dataset)

# printing the first 5 rows of the dataframe
loan_dataset.head()

# number of rows and columns
loan_dataset.shape

# statistical measures
loan_dataset.describe()

# number of missing values in each column
loan_dataset.isnull().sum()

# dropping the missing values
loan_dataset = loan_dataset.dropna()

# number of missing values in each column
loan_dataset.isnull().sum()

# label encoding
loan_dataset.replace({"Loan_Status":{'N':0,'Y':1}},inplace=True)

# printing the first 5 rows of the dataframe
loan_dataset.head()

# Dependent column values
loan_dataset['Dependents'].value_counts()

# replacing the value of 3+ to 4
loan_dataset = loan_dataset.replace(to_replace='3+', value=4)

# dependent values
loan_dataset['Dependents'].value_counts()

"""Data Visualization"""

# education & Loan Status
sns.countplot(x='Education',hue='Loan_Status',data=loan_dataset)

# marital status & Loan Status
sns.countplot(x='Married',hue='Loan_Status',data=loan_dataset)

# convert categorical columns to numerical values
loan_dataset.replace({'Married':{'No':0,'Yes':1},'Gender':{'Male':1,'Female':0},'Self_Employed':{'No':0,'Yes':1},
                      'Property_Area':{'Rural':0,'Semiurban':1,'Urban':2},'Education':{'Graduate':1,'Not Graduate':0}},inplace=True)

loan_dataset.head()

# separating the data and label
X = loan_dataset.drop(columns=['Loan_ID','Loan_Status'],axis=1)
Y = loan_dataset['Loan_Status']

print(X)
print(Y)

"""Train Test Split"""

X_train, X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.1,stratify=Y,random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""Training the model:

Support Vector Machine Model
"""

classifier = svm.SVC(kernel='linear')

#training the support Vector Macine model
classifier.fit(X_train,Y_train)

"""Model Evaluation"""

# accuracy score on training data
X_train_prediction = classifier.predict(X_train)
training_data_accuray = accuracy_score(X_train_prediction,Y_train)

print('Accuracy on training data : ', training_data_accuray)

# accuracy score on training data
X_test_prediction = classifier.predict(X_test)
test_data_accuray = accuracy_score(X_test_prediction,Y_test)

print('Accuracy on test data : ', test_data_accuray)

"""Making a predictive system"""

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

# Evaluate the model on the training dataset
X_train_pred = classifier.predict(X_train)

# Calculate training metrics
training_data_accuracy = accuracy_score(Y_train, X_train_pred)
training_data_precision = precision_score(Y_train, X_train_pred, average='binary')  # Adjust average if multiclass
training_data_recall = recall_score(Y_train, X_train_pred, average='binary')
training_data_f1 = f1_score(Y_train, X_train_pred, average='binary')

# Print training metrics
print("Training Data Metrics:")
print(f"Accuracy: {training_data_accuracy:.2f}")
print(f"Precision: {training_data_precision:.2f}")
print(f"Recall: {training_data_recall:.2f}")
print(f"F1 Score: {training_data_f1:.2f}")
print("\nDetailed Training Classification Report:")
print(classification_report(Y_train, X_train_pred))

# Evaluate the model on the testing dataset
X_test_pred = classifier.predict(X_test)

# Calculate testing metrics
test_data_accuracy = accuracy_score(Y_test, X_test_pred)
test_data_precision = precision_score(Y_test, X_test_pred, average='binary')  # Adjust average if multiclass
test_data_recall = recall_score(Y_test, X_test_pred, average='binary')
test_data_f1 = f1_score(Y_test, X_test_pred, average='binary')

# Print testing metrics
print("\nTesting Data Metrics:")
print(f"Accuracy: {test_data_accuracy:.2f}")
print(f"Precision: {test_data_precision:.2f}")
print(f"Recall: {test_data_recall:.2f}")
print(f"F1 Score: {test_data_f1:.2f}")
print("\nDetailed Testing Classification Report:")
print(classification_report(Y_test, X_test_pred))

# Document model performance
print("\nPerformance Summary:")
print(f"Training Accuracy: {training_data_accuracy:.2f}, Testing Accuracy: {test_data_accuracy:.2f}")
print("Observations:")
if training_data_accuracy > test_data_accuracy:
    print("The model might be overfitting as it performs better on training data than testing data.")
elif training_data_accuracy < test_data_accuracy:
    print("The model might be underfitting or over-generalizing.")
else:
    print("The model shows consistent performance across training and testing datasets.")

import pickle

filename = 'loan_status_model.pkl'
pickle.dump(classifier, open(filename, 'wb'))

# Import necessary libraries
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Train the Random Forest Classifier
classifier = RandomForestClassifier(random_state=2)
classifier.fit(X_train, Y_train)

# Evaluate model on training data
X_train_pred = classifier.predict(X_train)
X_training_data_accuracy = accuracy_score(Y_train, X_train_pred)
print(f"Random Forest - Training Data Accuracy: {X_training_data_accuracy:.2f}")

# Evaluate model on testing data
X_test_pred = classifier.predict(X_test)
X_test_data_accuracy = accuracy_score(Y_test, X_test_pred)
print(f"Random Forest - Test Data Accuracy: {X_test_data_accuracy:.2f}")

# Save the trained Random Forest model using pickle
model_filename = 'loan_status_rf_model.pkl'
with open(model_filename, 'wb') as file:
    pickle.dump(classifier, file)

print(f"Model saved as {model_filename}")

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

# Evaluate the model on the training dataset
X_train_pred = classifier.predict(X_train)

# Calculate training metrics
training_data_accuracy = accuracy_score(Y_train, X_train_pred)
training_data_precision = precision_score(Y_train, X_train_pred, average='binary')  # Adjust average for multiclass
training_data_recall = recall_score(Y_train, X_train_pred, average='binary')
training_data_f1 = f1_score(Y_train, X_train_pred, average='binary')

# Print training metrics
print("Training Data Metrics:")
print(f"Accuracy: {training_data_accuracy:.2f}")
print(f"Precision: {training_data_precision:.2f}")
print(f"Recall: {training_data_recall:.2f}")
print(f"F1 Score: {training_data_f1:.2f}")
print("\nDetailed Training Classification Report:")
print(classification_report(Y_train, X_train_pred))

# Evaluate the model on the testing dataset
X_test_pred = classifier.predict(X_test)

# Calculate testing metrics
test_data_accuracy = accuracy_score(Y_test, X_test_pred)
test_data_precision = precision_score(Y_test, X_test_pred, average='binary')  # Adjust average for multiclass
test_data_recall = recall_score(Y_test, X_test_pred, average='binary')
test_data_f1 = f1_score(Y_test, X_test_pred, average='binary')

# Print testing metrics
print("\nTesting Data Metrics:")
print(f"Accuracy: {test_data_accuracy:.2f}")
print(f"Precision: {test_data_precision:.2f}")
print(f"Recall: {test_data_recall:.2f}")
print(f"F1 Score: {test_data_f1:.2f}")
print("\nDetailed Testing Classification Report:")
print(classification_report(Y_test, X_test_pred))

# Document model performance
print("\nPerformance Summary:")
print(f"Training Accuracy: {training_data_accuracy:.2f}, Testing Accuracy: {test_data_accuracy:.2f}")
print("Observations:")
if training_data_accuracy > test_data_accuracy:
    print("The model might be overfitting as it performs better on training data than testing data.")
elif training_data_accuracy < test_data_accuracy:
    print("The model might be underfitting or over-generalizing.")
else:
    print("The model shows consistent performance across training and testing datasets.")

from xgboost import XGBClassifier
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import pickle
classifier.fit(X_train, Y_train)
# Initialize the XGBoost classifier with support for categorical dat
# Fit the model
# XGBoost Accuracy
X_train_pred = classifier.predict(X_train)
X_training_data_accuracy = accuracy_score(X_train_pred, Y_train)
print(f"XGBoost- Training Data Accuracy: {X_training_data_accuracy}")
X_test_pred = classifier.predict(X_test)
X_test_data_accuracy = accuracy_score(X_test_pred, Y_test)
print(f"XGBoost- Test Data Accuracy: {X_test_data_accuracy}")
# Save XGBoost Model
xgb_filename = 'loan_status_xgb_model.pkl'
pickle.dump(classifier, open(xgb_filename, 'wb'))

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

# Evaluate the model on the training dataset
X_train_pred = classifier.predict(X_train)

# Calculate training metrics
training_data_accuracy = accuracy_score(Y_train, X_train_pred)
training_data_precision = precision_score(Y_train, X_train_pred, average='binary')  # Adjust average for multiclass
training_data_recall = recall_score(Y_train, X_train_pred, average='binary')
training_data_f1 = f1_score(Y_train, X_train_pred, average='binary')

# Print training metrics
print("Training Data Metrics:")
print(f"Accuracy: {training_data_accuracy:.2f}")
print(f"Precision: {training_data_precision:.2f}")
print(f"Recall: {training_data_recall:.2f}")
print(f"F1 Score: {training_data_f1:.2f}")
print("\nDetailed Training Classification Report:")
print(classification_report(Y_train, X_train_pred))

# Evaluate the model on the testing dataset
X_test_pred = classifier.predict(X_test)

# Calculate testing metrics
test_data_accuracy = accuracy_score(Y_test, X_test_pred)
test_data_precision = precision_score(Y_test, X_test_pred, average='binary')  # Adjust average for multiclass
test_data_recall = recall_score(Y_test, X_test_pred, average='binary')
test_data_f1 = f1_score(Y_test, X_test_pred, average='binary')

# Print testing metrics
print("\nTesting Data Metrics:")
print(f"Accuracy: {test_data_accuracy:.2f}")
print(f"Precision: {test_data_precision:.2f}")
print(f"Recall: {test_data_recall:.2f}")
print(f"F1 Score: {test_data_f1:.2f}")
print("\nDetailed Testing Classification Report:")
print(classification_report(Y_test, X_test_pred))

# Document model performance
print("\nPerformance Summary:")
print(f"Training Accuracy: {training_data_accuracy:.2f}, Testing Accuracy: {test_data_accuracy:.2f}")
print("Observations:")
if training_data_accuracy > test_data_accuracy:
    print("The model might be overfitting as it performs better on training data than testing data.")
elif training_data_accuracy < test_data_accuracy:
    print("The model might be underfitting or over-generalizing.")
else:
    print("The model shows consistent performance across training and testing datasets.")

# Import necessary libraries
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pickle

# Initialize and train the Decision Tree model
classifier = DecisionTreeClassifier(random_state=2)
classifier.fit(X_train, Y_train)

# Evaluate model on training data
X_train_pred = classifier.predict(X_train)
X_training_data_accuracy = accuracy_score(Y_train, X_train_pred)
print(f"Decision Tree - Training Data Accuracy: {X_training_data_accuracy:.2f}")

# Evaluate model on testing data
X_test_pred = classifier.predict(X_test)
X_test_data_accuracy = accuracy_score(Y_test, X_test_pred)
print(f"Decision Tree - Test Data Accuracy: {X_test_data_accuracy:.2f}")

# Save the trained Decision Tree model using pickle
dt_filename = 'loan_status_dt_model.pkl'
with open(dt_filename, 'wb') as file:
    pickle.dump(classifier, file)

print(f"Decision Tree model saved as {dt_filename}")

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

# Evaluate the model on the training dataset
X_train_pred = classifier.predict(X_train)
training_data_accuracy = accuracy_score(Y_train, X_train_pred)
training_data_precision = precision_score(Y_train, X_train_pred, average='binary')  # Adjust for binary classification
training_data_recall = recall_score(Y_train, X_train_pred, average='binary')
training_data_f1 = f1_score(Y_train, X_train_pred, average='binary')

# Print training metrics
print("Training Data Metrics:")
print(f"Accuracy: {training_data_accuracy:.2f}")
print(f"Precision: {training_data_precision:.2f}")
print(f"Recall: {training_data_recall:.2f}")
print(f"F1 Score: {training_data_f1:.2f}")
print("\nDetailed Training Classification Report:")
print(classification_report(Y_train, X_train_pred))

# Evaluate the model on the testing dataset
X_test_pred = classifier.predict(X_test)
test_data_accuracy = accuracy_score(Y_test, X_test_pred)
test_data_precision = precision_score(Y_test, X_test_pred, average='binary')  # Adjust for binary classification
test_data_recall = recall_score(Y_test, X_test_pred, average='binary')
test_data_f1 = f1_score(Y_test, X_test_pred, average='binary')

# Print testing metrics
print("\nTesting Data Metrics:")
print(f"Accuracy: {test_data_accuracy:.2f}")
print(f"Precision: {test_data_precision:.2f}")
print(f"Recall: {test_data_recall:.2f}")
print(f"F1 Score: {test_data_f1:.2f}")
print("\nDetailed Testing Classification Report:")
print(classification_report(Y_test, X_test_pred))

# Document model performance
print("\nPerformance Summary:")
print(f"Training Accuracy: {training_data_accuracy:.2f}, Testing Accuracy: {test_data_accuracy:.2f}")
print("Observations:")
if training_data_accuracy > test_data_accuracy:
    print("The model might be overfitting as it performs better on training data than testing data.")
elif training_data_accuracy < test_data_accuracy:
    print("The model might be underfitting or over-generalizing.")
else:
    print("The model shows consistent performance across training and testing datasets.")

# Import necessary libraries
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
import pickle

# Initialize and train the AdaBoost model
classifier = AdaBoostClassifier(random_state=2)
classifier.fit(X_train, Y_train)

# Evaluate the model on training data
X_train_pred = classifier.predict(X_train)
X_training_data_accuracy = accuracy_score(Y_train, X_train_pred)
print(f"AdaBoost - Training Data Accuracy: {X_training_data_accuracy:.2f}")

# Evaluate the model on testing data
X_test_pred = classifier.predict(X_test)
X_test_data_accuracy = accuracy_score(Y_test, X_test_pred)
print(f"AdaBoost - Test Data Accuracy: {X_test_data_accuracy:.2f}")

# Save the trained AdaBoost model
ab_filename = 'loan_status_ab_model.pkl'
with open(ab_filename, 'wb') as file:
    pickle.dump(classifier, file)

print(f"AdaBoost model saved as {ab_filename}")

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

# Evaluate the model on the training dataset
X_train_pred = classifier.predict(X_train)
training_data_accuracy = accuracy_score(Y_train, X_train_pred)
training_data_precision = precision_score(Y_train, X_train_pred, average='binary')  # Binary classification
training_data_recall = recall_score(Y_train, X_train_pred, average='binary')
training_data_f1 = f1_score(Y_train, X_train_pred, average='binary')

# Print training metrics
print("Training Data Metrics:")
print(f"Accuracy: {training_data_accuracy:.2f}")
print(f"Precision: {training_data_precision:.2f}")
print(f"Recall: {training_data_recall:.2f}")
print(f"F1 Score: {training_data_f1:.2f}")
print("\nDetailed Training Classification Report:")
print(classification_report(Y_train, X_train_pred))

# Evaluate the model on the testing dataset
X_test_pred = classifier.predict(X_test)
test_data_accuracy = accuracy_score(Y_test, X_test_pred)
test_data_precision = precision_score(Y_test, X_test_pred, average='binary')  # Binary classification
test_data_recall = recall_score(Y_test, X_test_pred, average='binary')
test_data_f1 = f1_score(Y_test, X_test_pred, average='binary')

# Print testing metrics
print("\nTesting Data Metrics:")
print(f"Accuracy: {test_data_accuracy:.2f}")
print(f"Precision: {test_data_precision:.2f}")
print(f"Recall: {test_data_recall:.2f}")
print(f"F1 Score: {test_data_f1:.2f}")
print("\nDetailed Testing Classification Report:")
print(classification_report(Y_test, X_test_pred))

# Document model performance
print("\nPerformance Summary:")
print(f"Training Accuracy: {training_data_accuracy:.2f}, Testing Accuracy: {test_data_accuracy:.2f}")
print("Observations:")
if training_data_accuracy > test_data_accuracy:
    print("The model might be overfitting as it performs better on training data than testing data.")
elif training_data_accuracy < test_data_accuracy:
    print("The model might be underfitting or over-generalizing.")
else:
    print("The model shows consistent performance across training and testing datasets.")
