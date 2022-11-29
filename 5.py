# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 11:48:29 2022

@author: lenovo
"""

#plot--> hist,boxplot,line,sactter,barplot,pie
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("C:\Users\lenovo\Downloads\titanic.csv")
plt.hst(df['PassengerId'])
plt.bar(df['']),df['gmat']
plt.plot(df['workex']),df['gmat']
plt.boxplot(['workex'])

x=[1,2,3,4,5]
y=["ai","python","ml","ds","iot"]
plt.pie(x,labels=y)
