# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 12:07:28 2022

@author: lenovo
"""

#importing the dataset

import pandas as pd
ad=pd.read_csv(":\\")
#seeing the structure of data
str(ad)
#checking null values column wise
ad.isna().sum()
#dropping null value

df=ad.dropna()
df
df.isna().sum()

#dealing with categorical type of data
df.columns
cat=[ 'workclass', 'education', 'status'
       'occupation', 'relationship', 'race', 'sex',
       'native country', 'salary']
 
from sklearn.preprocessing import labelencoder
lb=labelencoder()
 
for i in cat:
     df[i]=lb.fit_transform(df[i])
     
#dealingnwith continous type of data
con=['age', 'fnlwgt', 'education_no', 'capital_loss', 'hours_perweek',]

from sklearn.preprocessing import MinMaxScaler
 mm=minmaxscaler()
for i in con:
    df[i]=MM.fit_transform(df[i].value.reshape(-1,1))
    
#spliting into train and test
from sklearn.model_selection import train_test_split
train,test=train_test_split(df,test_size=0.2) 
    
    