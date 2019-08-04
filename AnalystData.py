# craw tu 7/4/2006 den ngay hom nay
# -*- coding: utf-8 -*-
import sys
sys.path.insert(1, '/home/kl/projects/perdator')
from datetime import tzinfo, timedelta, datetime
from bs4 import BeautifulSoup
from urllib import request
import threading
import logging
import concurrent.futures
import re
from configuration.DBConnection import DBConnection
from entities.KqxsEntity import KqxsEntity
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
import pandas as pd
conn = DBConnection()
import matplotlib.pyplot as plt
import math
def convertPlaceToNumber(place):
    if place == 'Nam Định':
        return 1
    if place == 'Miền Bắc':
        return 2
    if place == 'Thái Bình':
        return 3
    if place == 'Hải Phòng':
        return 4
    if place == 'Hà Nội':
        return 5
    if place == 'Bắc Ninh':
        return 6
    if place == 'Quảng Ninh':
        return 7
    else:
        return 2
def euclideanDistance(instance1, instance2):
    distance = 0
    length = len(instance1)
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)
# print('Distance: ' + repr(distance))
# test = KqxsEntity.query.filter_by().first()
query = conn.session.query(KqxsEntity).order_by(KqxsEntity.date.desc())
df = pd.read_sql(query.statement, query.session.bind)
df['label'] = df['db'].apply(lambda x: x[-2:])
df['place'] = df['place'].apply(lambda x: convertPlaceToNumber(x))
df = df.drop(columns=['tail1'])
df = df.drop(columns=['tail2'])
df = df.drop(columns=['tail3'])
df = df.drop(columns=['tail4'])
df = df.drop(columns=['tail5'])
df = df.drop(columns=['tail6'])
df = df.drop(columns=['tail7'])
df = df.drop(columns=['tail8'])
df = df.drop(columns=['tail9'])
df = df.drop(columns=['date'])
# df['tail1'] = df['tail1'].apply(lambda x: np.array(x.split(',')))
# df['tail2'] = df['tail2'].apply(lambda x: np.array(x.split(',')))
# df['tail3'] = df['tail3'].apply(lambda x: np.array(x.split(',')))
# df['tail4'] = df['tail4'].apply(lambda x: np.array(x.split(',')))
# df['tail5'] = df['tail5'].apply(lambda x: np.array(x.split(',')))
# df['tail6'] = df['tail6'].apply(lambda x: np.array(x.split(',')))
# df['tail7'] = df['tail7'].apply(lambda x: np.array(x.split(',')))
# df['tail8'] = df['tail8'].apply(lambda x: np.array(x.split(',')))
# df['tail9'] = df['tail9'].apply(lambda x: np.array(x.split(',')))
# df['date'] = df ['date'].apply(lambda x: time.mktime(datetime.strptime(x,'%Y-%m-%d')).timetuple())
# print(df['db'].apply(lambda x: x[-2:])[1])
for i in range(1,df['db'].count(),1):
    df['label'][i] = df['db'][i-1][-2:]
X = df.drop(columns=['label'])
y = df['label'].values
from sklearn.model_selection import train_test_split#split dataset into train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1, stratify=y)
# Create KNN classifier
knn = KNeighborsClassifier(n_neighbors = 2, algorithm='ball_tree')# Fit the classifier to the data
knn.fit(X_train,y_train)
#show first 5 model predictions on the test data
print(knn.predict(X_test)[0:5])
#check accuracy of our model on the test data

print(knn.score(X_test, y_test))

# test_X = X.iloc[0]
# test_y = y[0]
# training_X = X.iloc[1:]
# training_y = y.iloc[1:]
# df.set_index('label',inplace=True)
# df.plot(figsize=(18,5))
# plt.show()
print(df.shape)
print(df.iloc[:3])
# print(type(df.iloc[0]['date']))
# print(df)
# for test in tests:
# print(tests.__dict__)
# print(len(tests))
# le = preprocessing.LabelEncoder()
# kqEncoded = le.fit_transform(tests)
# print(kqEncoded)
# conn.session.
