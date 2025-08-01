import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, f1_score
from sklearn.feature_selection import RFE
from sklearn import svm
import xgboost as xgb


url = "https://drive.google.com/uc?id=1KWE3J0uU_sFIJnZ74Id3FDBcejELI7FD"
df = pd.read_csv(url)
print(df.head())
print(df.info())

# Y = target attribute (Y) with values indicating 0 (unhappy) and 1 (happy) customers
# X1 = my order was delivered on time
# X2 = contents of my order was as I expected
# X3 = I ordered everything I wanted to order
# X4 = I paid a good price for my order
# X5 = I am satisfied with my courier
# X6 = the app makes ordering easy for me

# Pre-process Data
x = df[['X1', 'X2', 'X3', 'X4', 'X5', 'X6']]
y = df['Y']
# splitting data original
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# decision tree, K nearest, X boost

# Random Forest Classifier model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
# feature selection
rf_selector = RFE(estimator=rf_model, n_features_to_select=3)
# fit RFE
rf_selected = rf_selector.fit_transform(x, y)
# split the data
X_train, X_test, y_train, y_test = train_test_split(rf_selected, y, test_size = 0.3, random_state=42)
rf_model.fit(X_train, y_train)
rf_y_pred = rf_model.predict(X_test)

# Evaluate Random Forest Model
rf_accuracy = accuracy_score(y_test, rf_y_pred)
rf_f1_score = f1_score(y_test, rf_y_pred)
print("Random Forest Classifier Results:")
print(f"Accuracy: {rf_accuracy:.4f}")
print(f"F1 Score: {rf_f1_score:.4f}")
print('Classification Report:')
print(classification_report(y_test, rf_y_pred))

# Decision Tree Classifier
dt_model = DecisionTreeClassifier(random_state=42)
# feature selection
dt_selector = RFE(estimator=dt_model, n_features_to_select=3)
# fit RFE
dt_selected = dt_selector.fit_transform(x, y)
# split the data
X_train, X_test, y_train, y_test = train_test_split(dt_selected, y, test_size = 0.3, random_state=42)
dt_model.fit(X_train, y_train)
dt_y_pred = dt_model.predict(X_test)

# Evaluate Decision Tree
dt_accuracy = accuracy_score(y_test, dt_y_pred)
dt_f1_score = f1_score(y_test, dt_y_pred)
print("Decision Tree Results:")
print(f"Accuracy: {dt_accuracy:.4f}")
print(f"F1 Score: {dt_f1_score:.4f}")
print('Classification Report:')
print(classification_report(y_test, dt_y_pred))

# K-Nearest Neighbors Classifier
knn_model = KNeighborsClassifier()
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state=42)
knn_model.fit(X_train, y_train)
knn_y_pred = knn_model.predict(X_test)

# Evaluate KNN
knn_accuracy = accuracy_score(y_test, knn_y_pred)
knn_f1_score = f1_score(y_test, knn_y_pred)
print("K-Nearest Neighbors Results:")
print(f"Accuracy: {knn_accuracy:.4f}")
print(f"F1 Score: {knn_f1_score:.4f}")
print('Classification Report:')
print(classification_report(y_test, knn_y_pred))

# XGBoost Classifier
xgb_model = xgb.XGBClassifier()
# feature Selection
xg_selector = RFE(estimator=xgb_model, n_features_to_select=3)
# fit RFE
xg_selected = xg_selector.fit_transform(x, y)
# split the data
X_train, X_test, y_train, y_test = train_test_split(xg_selected, y, test_size = 0.3, random_state=42)
xgb_model.fit(X_train, y_train)
xgb_y_pred = xgb_model.predict(X_test)

# Evaluate XGBoost
xgb_accuracy = accuracy_score(y_test, xgb_y_pred)
xgb_f1_score = f1_score(y_test, xgb_y_pred)
print("XGBoost Results:")
print(f"Accuracy: {xgb_accuracy:.4f}")
print(f"F1 Score: {xgb_f1_score:.4f}")
print('Classification Report:')
print(classification_report(y_test, xgb_y_pred))

# svm
svm_model = svm.SVC()
# training the data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state=42)
svm_model.fit(X_train, y_train)
svm_y_pred = svm_model.predict(X_test)
# Evaluate SVM
svm_accuracy = accuracy_score(y_test, svm_y_pred)
svm_f1_score = f1_score(y_test, svm_y_pred)
print("SVM Results:")
print(f"Accuracy: {svm_accuracy:.4f}")
print(f"F1 Score: {svm_f1_score:.4f}")
print('Classification Report:')
print(classification_report(y_test, svm_y_pred))
