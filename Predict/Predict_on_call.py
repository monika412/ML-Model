#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:04:41 2018

@author: kanagarw
"""

import numpy as np
from sklearn.externals import joblib

#Predictions on the model(to be used in the prediction pipeline)

#1. From ID get row in form of dictionary, 
dict1 = { "ID" : 11, "Annual_Deposit_Amount" : 38304, "Home_value" : 29614, "Years_with_the_bank" : 3, "Loan_held" : 1, 
         "Wealth_portfolio_held" : 1, "Automated_menu" : 3, "Priority" : 1}
#2. Convert to an array of shape (1,6) lets call it 'arr'
arr= list(dict1.values())
arr= np.array(arr[1:-1]).reshape(1,6)

#3. Scale the array using Scaler.pkl
scaler = joblib.load('Scaler.pkl') 
data_point = scaler.transform(arr)

#4. Get predictionsreplacing the X_test below 
clf = joblib.load('Classifier.pkl') 

y_test_pred = clf.predict(data_point)


