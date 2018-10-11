import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
'''s=pd.Series([1,3,5,6,8])
print(s)'''
'''
df=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/voting-records/house-votes-84.data')
print(df)
#print(df.head(10))#if you not pass and value it will default show 5 records.
#print(df)
#print(df.tail(3))#this will show the n number of rows from bottom
#print(df)
#print(df.index)#it will show the starting index=0, stop=434 and step=1(that the increment by 1)
#print(df.columns)# it will showl all the header
#print(df.describe())#it will show four parameter (count,unique,top,fre)values
#print(df.T)#Transposing your data
print(df.sort_index(axis=1,ascending=True))#Sorting by an axis
'''
url='https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'
df=pd.read_csv(url)
print(df)
path='C:/Users/Chanda Kumari/Documents/Data_python/auto.csv'
df.to_csv(path)
