#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 10:23:51 2018

@author: kanagarw
"""

import pandas as pd
import numpy as np
from numpy import random
import math
import matplotlib

columns = ["Annual_Deposit_Amount", "Home_value", "Years_with_the_bank", "Loan_held", "Wealth_portfolio_held", "Automated_menu", "Priority"]

Dataset = pd.DataFrame(columns=columns)
l=10000

#random_l1 = random.choice(range(99999), l, replace=False).tolist()

Setup a regular payment (rank 3)
Change address (rank 4)
Take out a loan (rank 1)
Open a Wealth account (rank 2)

Annual Deposit Amount (higher the better)
Home value (higher the better)
Years with the bank (higher the better)
Loan held (Y/N. Yes is better)
Wealth portfolio held  (Y/N. Yes is better)

Annual Deposit Amount
#
#
#s = np.random.normal(mu, sigma, l)
#desc= pd.DataFrame(s).describe()          
#s.min()
#import matplotlib.pyplot as plt
#count, bins, ignored = plt.hist(s, 30, normed=True)
#plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ),linewidth=2, color='r')
#plt.show()
#
#creditdf= pd.read_csv("creditcard.csv")
#corr=creditdf.corr()
#import matplotlib.pyplot as plt
#
#plt.matshow(corr)
#lst=[1 for i in range(5)]

Years_with_the_bank = np.random.normal(2.2, .7, l)
Years_with_the_bank_1 = [i+(random.choice([1,.5,.6,2,.2,1.1,4,2.3,2.6,1.4,1,1.5,.1,.2,.3,.2],1))[0] for i in Years_with_the_bank]
Years_with_the_bank_2=[math.floor(i/1.6) for i in Years_with_the_bank_1]
Years_with_the_bank=Years_with_the_bank_2

Loan_held_1=[random.choice([1 for i in range(i+1)]+[0,0],1)[0] for i in Years_with_the_bank]

Wealth_portfolio_held = [random.choice([1 for i in range(i-1)]+[0,0],1)[0] for i in Years_with_the_bank]
Wealth_portfolio_held_1 = [random.choice([i,i,i,i,i,0,1,0]) for i in Wealth_portfolio_held]
Wealth_portfolio_held = Wealth_portfolio_held_1
Loan_held = [random.choice([i,i,i,i,0,1],1)[0] for i in Loan_held_1]




mu, sigma = 25838, 510
Home_value_1 = np.random.normal(mu, sigma, l)

Dataset['Years_with_the_bank']=Years_with_the_bank
Dataset['Wealth_portfolio_held']=Wealth_portfolio_held
Dataset['Loan_held']=Loan_held
Dataset['Home_value']=Home_value_1


mu, sigma = 29384, 7609
Dataset['random_home_var'] = np.random.normal(mu, sigma, l)
mu, sigma = 6784, 909
Dataset['random_home_var_1'] = np.random.normal(mu, sigma, l)
mu, sigma = 6384, 809
Dataset['random_home_var_2'] = np.random.normal(mu, sigma, l)

Home_value_2 = []
for index, row in Dataset.iterrows():
   res = row['Home_value']+ row['random_home_var']*row['Loan_held']/3.2 - row['random_home_var_1']*row['Wealth_portfolio_held']/3.1 + row['random_home_var_2']*row['Wealth_portfolio_held']/3.6 - row['random_home_var_1']*row['Loan_held']/2.8
   Home_value_2.append(math.ceil(res))
   
Dataset['Home_value']=Home_value_2
mini=min(Dataset['Home_value'])

Dataset['Home_value_norm']=[(i-mini)/mini for i in Dataset['Home_value']]

Annual_Deposit_Amount=[]

for index, row in Dataset.iterrows():
   res = row['Home_value'] - row['random_home_var_2']*row['Loan_held'] - row['random_home_var_1']*row['Loan_held'] + row['random_home_var']*row['Wealth_portfolio_held']
   Annual_Deposit_Amount.append(math.ceil(res))
   
Annual_Deposit_Amount=[abs(i) for i  in Annual_Deposit_Amount]
Dataset['Annual_Deposit_Amount']=Annual_Deposit_Amount



Automated_menu=[random.choice([1,2,3,4],1)[0] for i in range(l)]

Dataset['Automated_menu']=Automated_menu

Dataset=Dataset[columns]
Dataset["Priority"]=0


Dataset.to_csv('Trainset.csv')
savedDs=Dataset

desc=Dataset.describe()

mini=min(Dataset["Annual_Deposit_Amount"])
Dataset["Annual_Deposit_Amount_scaled"]=[(i-mini)/mini for i in  Dataset["Annual_Deposit_Amount"]]

mini=min(Dataset["Home_value"])
Dataset["Home_value_scaled"]=[(i-mini)/mini for i in  Dataset["Home_value"]]

score1=[]
for index, row in Dataset.iterrows():
   res = row["Home_value_scaled"] * 4 + row["Annual_Deposit_Amount_scaled"] + row['Years_with_the_bank'] + row['Loan_held']*2 - row['Automated_menu']/2 +row['Wealth_portfolio_held']*7
   score1.append(math.ceil(res))
score1= [i+1 for i in score1]
mini=min(score1)
Dataset["Score1"]=[(i-mini)/mini for i in  score1]


score2=[]
for index, row in Dataset.iterrows():
   res = row["Home_value_scaled"]  + row["Annual_Deposit_Amount_scaled"] + row['Years_with_the_bank']*2 + row['Loan_held'] - row['Automated_menu']/3 +row['Wealth_portfolio_held']*2
   score2.append(math.ceil(res))
score2= [i+2 for i in score2]
mini=min(score2)
Dataset["Score2"]=[(i-mini)/mini for i in  score2]

Dataset["Score3"]=Dataset['Score1']*.7+Dataset['Score2']*.8
f=[1 for i in Dataset["Score3"] if i >= 10]
Dataset["Priority"]=[1 if i >= 10 else 0 for i in Dataset["Score3"]]

Dataset=Dataset[columns]

Dataset.to_csv("Train_with_target.csv")
