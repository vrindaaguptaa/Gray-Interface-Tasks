# -*- coding: utf-8 -*-
"""sonu_task_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17qnwIdJhNjl5oXsqg4K5GQZPAMYyyC6e
"""


import pandas as pd

import numpy as np

df = pd.read_csv("sonu_2347015_tasks\cereal.csv")

print(df.head)

df.shape

df.columns

df.info()

df.drop(['name','mfr','type'], axis=1, inplace=True)

df.shape

df2=df.to_numpy() #converting df to array

#question 1
arr1=np.empty_like(df2)
print(arr1)

#question 1
arr2=np.full_like(df2, fill_value=5)
print(arr2)

#question 2
arr3=np.zeros_like(df2)
print(arr3)

#question 3
arr4=np.ones_like(df2)
print(arr4)

df2

#question 4
df2[df2>70]=12
print(f"new array is \n {df2}")

#question 5
print(np.max(df2))  #shows 70 as we converted all numbers above 70 as 12

#creating new array to find max value
df3=df.to_numpy()
print(np.max(df3))

