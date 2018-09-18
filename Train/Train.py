#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 15:59:49 2018

@author: kanagarw
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib
import pandas as pd

from sklearn import preprocessing

clf = RandomForestClassifier(max_depth=5, random_state=0)

data = pd.read_csv("Train_with_target.csv", index_col = "Unnamed: 0")
columns = data.columns.tolist()

std_scale = preprocessing.StandardScaler().fit(data[['Annual_Deposit_Amount', 'Home_value', 'Years_with_the_bank', 'Loan_held', 'Wealth_portfolio_held', 'Automated_menu']])
joblib.dump(std_scale, 'Scaler.pkl')

data_std = std_scale.transform(data[['Annual_Deposit_Amount', 'Home_value', 'Years_with_the_bank', 'Loan_held', 'Wealth_portfolio_held', 'Automated_menu']])
#data_std = pd.DataFrame(data_std)
#X = data_std[['Annual_Deposit_Amount', 'Home_value',
#       'Years_with_the_bank', 'Loan_held', 'Wealth_portfolio_held',
#       'Automated_menu']]

X = data_std
y = data['Priority']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

clf.fit(X_train, y_train)

#Persisting the model
joblib.dump(clf, 'Classifier.pkl')


#Accuracy
from sklearn.metrics import accuracy_score
y_test_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_test_pred)
#0.9693







