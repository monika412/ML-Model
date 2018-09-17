#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 15:59:49 2018

@author: kanagarw
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib

clf = RandomForestClassifier(max_depth=5, random_state=0)

data = pd.read_csv("Train_with_target.csv", index_col = "Unnamed: 0")

X = data[['Annual_Deposit_Amount', 'Home_value',
       'Years_with_the_bank', 'Loan_held', 'Wealth_portfolio_held',
       'Automated_menu']]
y = data['Priority']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

clf.fit(X, y)

#Persisting the model
joblib.dump(clf, 'Classifier.pkl') 





clf2= joblib.load('Classifier.pkl') 


y_test_pred = clf2.predict(X_test)

compare= pd.DataFrame({'actual':y_test,'predicted':y_test_pred})