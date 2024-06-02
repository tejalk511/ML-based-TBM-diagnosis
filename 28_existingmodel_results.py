# -*- coding: utf-8 -*-
"""28.ExistingModel_results.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IOsS5uDj1sritXp4BAFQnVy88iJDLOQL

# **METHOD 1 - VALIDATION**

**Task -**
(Note - data used is regenerated according to latest standard , 15k rows.)

Model 1.1 - TLC using Random Forest

Model 1.2 -  TLC using grad Boosting

Model 2.1 - Protein using Random Forest

Model 2.2 - Protein using GB

Model 3.1 - Sugar using Random Forest

Model 3.2 - Sugar using GB

Ensemble model - Majority voting

Take User input -

O/p 1 - Disease Name

O/p 2 - Graph
"""

#Librarires required
import pandas as pd
from sklearn.ensemble import VotingClassifier #used in esembling model
import numpy as np
import matplotlib.pyplot as plt #for graph
from sklearn.model_selection import StratifiedKFold #For k fold
from sklearn.ensemble import RandomForestClassifier #for random forest classifier
from sklearn.ensemble import GradientBoostingClassifier #FOR G.B. classifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report #for accuracy and classification report
from mpl_toolkits import mplot3d #For 3d plots
import keras

#Loading dataset

df = pd.read_csv("Final2.csv")
df.head()

print(df.shape)

"""Model 1.1 - TLC using Random Forest"""

#Altering dataset -
df1 = df.drop(['Protein', 'Sugar'], axis=1)

#dividing dataset -
x = df1.drop(['Condition'], axis = 1)
y = df1.Condition

skf = StratifiedKFold(n_splits = 10)
model1_1 = RandomForestClassifier(n_estimators=10,  max_features = 'sqrt')

def training(train, test, fold_no):
  x_train = train.drop(['Condition'],axis=1)
  y_train = train.Condition
  x_test = test.drop(['Condition'],axis=1)
  y_test = test.Condition
  model1_1.fit(x_train, y_train)
  score = model1_1.score(x_test,y_test)
  #print('For Fold {} the test accuracy is {}'.format(str(fold_no),score))
  score1 = model1_1.score(x_train,y_train)
  print('For Fold {} the Train accuracy is {} and Test accuracy is: {}.'.format(str(fold_no),score1,score))
  y_pred_test = model1_1.predict(x_test)
  print(confusion_matrix(y_test, y_pred_test))
  print(classification_report(y_test, y_pred_test))

fold_no = 1
for train_index,test_index in skf.split(x, y):
  train = df1.iloc[train_index,:]
  test = df1.iloc[test_index,:]
  training(train, test, fold_no)
  fold_no += 1

"""Model 1.2 -  TLC using grad Boosting"""

skf = StratifiedKFold(n_splits = 10)
model1_2 = GradientBoostingClassifier(n_estimators=20, learning_rate=0.1, max_features=2, max_depth=2, random_state=0)

def training(train, test, fold_no):
  x_train = train.drop(['Condition'],axis=1)
  y_train = train.Condition
  x_test = test.drop(['Condition'],axis=1)
  y_test = test.Condition
  model1_2.fit(x_train, y_train)
  score = model1_2.score(x_test,y_test)
  #print('For Fold {} the test accuracy is {}'.format(str(fold_no),score))
  score1 = model1_2.score(x_train,y_train)
  print('For Fold {} the Train accuracy is {} and Test accuracy is: {}.'.format(str(fold_no),score1,score))
  y_pred_test = model1_2.predict(x_test)
  print(confusion_matrix(y_test, y_pred_test))
  print(classification_report(y_test, y_pred_test))

fold_no = 1
for train_index,test_index in skf.split(x, y):
  train = df1.iloc[train_index,:]
  test = df1.iloc[test_index,:]
  training(train, test, fold_no)
  fold_no += 1

"""Model 2.1 - Protein using Random Forest"""

#Altering dataset -
df2 = df.drop(['TLC', 'Sugar'], axis=1)
#dividing dataset -
x = df2.drop('Condition', axis = 1)
y = df2.Condition

skf = StratifiedKFold(n_splits = 10)
model2_1 = RandomForestClassifier(n_estimators=10,  max_features = 'sqrt')

def training(train, test, fold_no):
  x_train = train.drop(['Condition'],axis=1)
  y_train = train.Condition
  x_test = test.drop(['Condition'],axis=1)
  y_test = test.Condition
  model2_1.fit(x_train, y_train)
  score = model2_1.score(x_test,y_test)
  #print('For Fold {} the test accuracy is {}'.format(str(fold_no),score))
  score1 = model2_1.score(x_train,y_train)
  print('For Fold {} the Train accuracy is {} and Test accuracy is: {}.'.format(str(fold_no),score1,score))
  y_pred_test = model2_1.predict(x_test)
  print(confusion_matrix(y_test, y_pred_test))
  print(classification_report(y_test, y_pred_test))

fold_no = 1
for train_index,test_index in skf.split(x, y):
  train = df2.iloc[train_index,:]
  test = df2.iloc[test_index,:]
  training(train, test, fold_no)
  fold_no += 1

"""Model 2.2 - Protein using GB"""

skf = StratifiedKFold(n_splits = 10)
model2_2 = GradientBoostingClassifier(n_estimators=20, learning_rate=0.1, max_features=2, max_depth=2, random_state=0)

def training(train, test, fold_no):
  x_train = train.drop(['Condition'],axis=1)
  y_train = train.Condition
  x_test = test.drop(['Condition'],axis=1)
  y_test = test.Condition
  model2_2.fit(x_train, y_train)
  score = model2_2.score(x_test,y_test)
  #print('For Fold {} the test accuracy is {}'.format(str(fold_no),score))
  score1 = model2_2.score(x_train,y_train)
  print('For Fold {} the Train accuracy is {} and Test accuracy is: {}.'.format(str(fold_no),score1,score))
  y_pred_test = model2_2.predict(x_test)
  print(confusion_matrix(y_test, y_pred_test))
  print(classification_report(y_test, y_pred_test))

fold_no = 1
for train_index,test_index in skf.split(x, y):
  train = df2.iloc[train_index,:]
  test = df2.iloc[test_index,:]
  training(train, test, fold_no)
  fold_no += 1

"""Model 3.1 - Sugar using Random Forest"""

#Altering dataset -
df3 = df.drop(['TLC', 'Protein'], axis=1)
#dividing dataset -
x = df3.drop('Condition', axis = 1)
y = df3.Condition

skf = StratifiedKFold(n_splits = 10)
model3_1 = RandomForestClassifier(n_estimators=10,  max_features = 'sqrt')

def training(train, test, fold_no):
  x_train = train.drop(['Condition'],axis=1)
  y_train = train.Condition
  x_test = test.drop(['Condition'],axis=1)
  y_test = test.Condition
  model3_1.fit(x_train, y_train)
  score = model3_1.score(x_test,y_test)
  #print('For Fold {} the test accuracy is {}'.format(str(fold_no),score))
  score1 = model3_1.score(x_train,y_train)
  print('For Fold {} the Train accuracy is {} and Test accuracy is: {}.'.format(str(fold_no),score1,score))
  y_pred_test = model3_1.predict(x_test)
  print(confusion_matrix(y_test, y_pred_test))
  print(classification_report(y_test, y_pred_test))

fold_no = 1
for train_index,test_index in skf.split(x, y):
  train = df3.iloc[train_index,:]
  test = df3.iloc[test_index,:]
  training(train, test, fold_no)
  fold_no += 1

"""Model 3.2 - Sugar using GB"""

skf = StratifiedKFold(n_splits = 10)
model3_2 = GradientBoostingClassifier(n_estimators=20, learning_rate=0.1, max_features=2, max_depth=2, random_state=0)

def training(train, test, fold_no):
  x_train = train.drop(['Condition'],axis=1)
  y_train = train.Condition
  x_test = test.drop(['Condition'],axis=1)
  y_test = test.Condition
  model3_2.fit(x_train, y_train)
  score = model3_2.score(x_test,y_test)
  #print('For Fold {} the test accuracy is {}'.format(str(fold_no),score))
  score1 = model3_2.score(x_train,y_train)
  print('For Fold {} the Train accuracy is {} and Test accuracy is: {}.'.format(str(fold_no),score1,score))
  y_pred_test = model3_2.predict(x_test)
  print(confusion_matrix(y_test, y_pred_test))
  print(classification_report(y_test, y_pred_test))

fold_no = 1
for train_index,test_index in skf.split(x, y):
  train = df3.iloc[train_index,:]
  test = df3.iloc[test_index,:]
  training(train, test, fold_no)
  fold_no += 1

"""Ensemble Model -"""

# Making the final model using voting classifier
model = VotingClassifier( estimators=[('m1_1', model1_1), ('m1_2', model1_2), ('m2_1', model2_1), ('m2_2', model2_2), ('m3_1', model3_1), ('m3_2', model3_2)], voting='hard')

import seaborn as sns

skf = StratifiedKFold(n_splits = 10)

#class_names = ["TBM", "PM", "Normal"]

import tensorflow as tf
from tensorflow import keras

def training(train, test, fold_no):
  x_train = train.drop(['Condition'],axis=1)
  y_train = train.Condition
  x_test = test.drop(['Condition'],axis=1)
  y_test = test.Condition
  model.fit(x_train, y_train)
  '''
  #new code:
  model1 = keras.Sequential()
  model1.compile(optimizer='adam',
  loss='mse',
  metrics=['accuracy'])
  history = model1.fit(x_train, y_train, epochs=10, batch_size=1, validation_data=(x_test, y_test))
  #ends here
  '''
  score = model.score(x_test,y_test)
  #print('For Fold {} the test accuracy is {}'.format(str(fold_no),score))
  score1 = model.score(x_train,y_train)
  print('For Fold {} the Train accuracy is {} and Test accuracy is: {}.'.format(str(fold_no),score1,score))
  y_pred_test = model.predict(x_test)
  print(confusion_matrix(y_test, y_pred_test))
  plt.figure(figsize = (18,8))
  sns.heatmap(confusion_matrix(y_test, y_pred_test), annot = True, cmap = 'summer')
  plt.xlabel('Predicted Labels')
  plt.ylabel('True Labels')
  plt.show()
  print(classification_report(y_test, y_pred_test))

fold_no = 1
for train_index,test_index in skf.split(x, y):
  train = df.iloc[train_index,:]
  test = df.iloc[test_index,:]
  training(train, test, fold_no)
  fold_no += 1

"""Take User input -"""

print("Enter values of parameters : ")
a = float(input("Enter TLC value: \n"))
#b = float(input("Enter Lymphocytes value: \n"))
#c = float(input("Enter Polymorphs value: \n"))
#d = float(input("Enter Monocytes value: \n"))
#e = float(input("Enter Eosinophiles value: \n"))
f = float(input("Enter Protein value: \n"))
g = float(input("Enter Sugar value: \n"))

print(" ****************************** ")
print("**** Results are : ********* ")
result = model.predict([[a,f,g]])
print(result)
print("\n")
print("\n")
print(" ****************************** ")
print("\n")
print("\n")


'''
tbm (Severe case) - 15, 80, 35
pm (mild case ) - 256,  676, 50
Normal - 2,12,65
'''

print(a)
print(f)
print(g)

"""Dislaying results -"""

#Loading dataset
df1 = pd.read_csv("Normal.csv")
df2 = pd.read_csv("TBM.csv")
df3 = pd.read_csv("PM.csv")

#graph for Normal

data = pd.DataFrame(df1, columns = ['TLC', 'Protein', 'Sugar'])
#creating axes instance
fig = plt.figure(figsize=(10,7))

#Creating Box plot
#bp = plt.boxplot(data,notch='True',patch_artist = True, labels = ['TLC', 'Protein', 'Sugar'], showmeans = True )
bp = plt.boxplot(data, notch='True', labels = ['TLC', 'Protein', 'Sugar'], showmeans = True )
#IMpt - when patch_artist = True --> ranges is giving error

#Ploting data points
#plt.plot(1 ,200) #{Here, ny default - tlc = 1, pro = 2, sugar = 3}
plt.scatter(x=1,y=a, label = 'Scatter', color ='r', marker = 's', s = 100)
plt.scatter(x=2,y=f, label = 'Scatter', color ='r', marker = 's', s = 100)
plt.scatter(x=3,y=g, label = 'Scatter', color ='r', marker = 's', s = 100)

#show plot
plt.show()
#plt.title("Normal Category")

#Stats for NORMAL CATEGORY -

#Getting each value of data -
medians_N = [round(item.get_ydata()[0], 1) for item in bp['medians']]
means_N = [round(item.get_ydata()[0],1) for item in bp['means']]

minimums_N = [round(item.get_ydata()[0], 1) for item in bp['caps']][::2]
maximums_N = [round(item.get_ydata()[0], 1) for item in bp['caps']][1::2]

q1_N = [round(min(item.get_ydata()), 1) for item in bp['boxes']]
q3_N = [round(max(item.get_ydata()), 1) for item in bp['boxes']]

fliers_N = [item.get_ydata() for item in bp['fliers']]
lower_outliers_N = []
upper_outliers_N = []
for i in range(len(fliers_N)):
    lower_outliers_by_box_N = []
    upper_outliers_by_box_N = []
    for outlier in fliers_N[i]:
        if outlier < q1_N[i]:
            lower_outliers_by_box_N.append(round(outlier, 1))
        else:
            upper_outliers_by_box_N.append(round(outlier, 1))
    lower_outliers_N.append(lower_outliers_by_box_N)
    upper_outliers_N.append(upper_outliers_by_box_N)

print(" ************************************ ")
print(" STATS FOR NORMAL CATEGORY ARE : ")
print(" ************************************ ")

#Declaring for further purpose of calculating scores -
N1_min = 0
N1_q1 = 0
N1_q3 = 0
N1_maximums_N = 0
N2_min = 0
N2_q1 = 0
N2_q3 = 0
N2_maximums_N = 0
N3_min = 0
N3_q1 = 0
N3_q3 = 0
N3_maximums_N = 0

#same as above code but combined
stats = [medians_N, means_N, minimums_N, maximums_N, q1_N, q3_N, lower_outliers_N, upper_outliers_N]
stats_names = ['Median', 'Mean', 'Minimum', 'Maximum', 'Q1', 'Q3', 'Lower outliers', 'Upper outliers']
categories = ['TLC', 'Protein', 'Sugar'] # to be updated
for i in range(len(categories)):
    print(f'\033[1m{categories[i]}\033[0m')
    for j in range(len(stats)):
        print(f'{stats_names[j]}: {stats[j][i]}')
        if(categories[i] == "TLC"):
          #print("1 runned")
          if (stats_names[j] == 'Minimum'):
            N1_min = stats[j][i]
          elif (stats_names[j] == 'Q1'):
            N1_q1 = stats[j][i]
          elif (stats_names[j] == 'Q3'):
            N1_q3 = stats[j][i]
          elif (stats_names[j] == 'Maximum'):
            N1_maximums_N = stats[j][i]
        if(categories[i] == 'Protein'):
          if (stats_names[j] == 'Minimum'):
            N2_min = stats[j][i]
          elif (stats_names[j] == 'Q1'):
            N2_q1 = stats[j][i]
          elif (stats_names[j] == 'Q3'):
            N2_q3 = stats[j][i]
          elif (stats_names[j] == 'Maximum'):
            N2_maximums_N = stats[j][i]
        if(categories[i] == 'Sugar'):
          if (stats_names[j] == 'Minimum'):
            N3_min = stats[j][i]
          elif (stats_names[j] == 'Q1'):
            N3_q1 = stats[j][i]
          elif (stats_names[j] == 'Q3'):
            N3_q3 = stats[j][i]
          elif (stats_names[j] == 'Maximum'):
            N3_maximums_N = stats[j][i]
    print('\n')

'''
print("Extracted values are - ")
print("N1_min  = ", N1_min)
print("N1_q1 = ", N1_q1)
print("N1_q3 = ", N1_q3)
print("N1_maximums_N = ", N1_maximums_N)
print("N2_min = ", N2_min)
print("N2_q1 = ",N2_q1)
print("N2_q3 = ", N2_q3)
print("N2_maximums_N = ", N2_maximums_N)
print("N3_min = ", N3_min)
print(" N3_q1 = ", N3_q1)
print("N3_q3 =", N3_q3)
print("N3_maximums_N = ", N3_maximums_N)
'''

#graph for TBM

data = pd.DataFrame(df2, columns = ['TLC', 'Protein', 'Sugar'])
#creating axes instance
fig = plt.figure(figsize=(10,7))

#Creating Box plot
#bp = plt.boxplot(data,notch='True',patch_artist = True, labels = ['TLC', 'Protein', 'Sugar'] )
bp = plt.boxplot(data, labels = ['TLC', 'Protein', 'Sugar'], showmeans = True )
#Ploting data points
#plt.plot(1 ,200) #{Here, ny default - tlc = 1, pro = 2, sugar = 3}
plt.scatter(x=1,y=a, label = 'Scatter', color ='r', marker = 's', s = 100)
plt.scatter(x=2,y=f, label = 'Scatter', color ='r', marker = 's', s = 100)
plt.scatter(x=3,y=g, label = 'Scatter', color ='r', marker = 's', s = 100)

#show plot
plt.show()
#plt.title("TBM Category")

#Stats for TBM CATEGORY -

#Getting each value of data -
medians_T = [round(item.get_ydata()[0], 1) for item in bp['medians']]
means_T = [round(item.get_ydata()[0],1) for item in bp['means']]

minimums_T = [round(item.get_ydata()[0], 1) for item in bp['caps']][::2]
maximums_T = [round(item.get_ydata()[0], 1) for item in bp['caps']][1::2]

q1_T = [round(min(item.get_ydata()), 1) for item in bp['boxes']]
q3_T = [round(max(item.get_ydata()), 1) for item in bp['boxes']]

fliers_T = [item.get_ydata() for item in bp['fliers']]
lower_outliers_T = []
upper_outliers_T = []
for i in range(len(fliers_T)):
    lower_outliers_by_box_T = []
    upper_outliers_by_box_T = []
    for outlier in fliers_T[i]:
        if outlier < q1_T[i]:
            lower_outliers_by_box_T.append(round(outlier, 1))
        else:
            upper_outliers_by_box_T.append(round(outlier, 1))
    lower_outliers_T.append(lower_outliers_by_box_T)
    upper_outliers_T.append(upper_outliers_by_box_T)


print(" ************************************ ")
print(" STATS FOR TBM CATEGORY ARE : ")
print(" ************************************ ")

#Declaring for further purpose of calculating scores -
T1_min = 0
T1_q1 = 0
T1_q3 = 0
T1_maximums_N = 0
T2_min = 0
T2_q1 = 0
T2_q3 = 0
T2_maximums_N = 0
T3_min = 0
T3_q1 = 0
T3_q3 = 0
T3_maximums_N = 0

#same as above code but combined
stats = [medians_T, means_T, minimums_T, maximums_T, q1_T, q3_T, lower_outliers_T, upper_outliers_T]
stats_names = ['Median', 'Mean', 'Minimum', 'Maximum', 'Q1', 'Q3', 'Lower outliers', 'Upper outliers']
categories = ['TLC', 'Protein', 'Sugar'] # to be updated
for i in range(len(categories)):
    print(f'\033[1m{categories[i]}\033[0m')
    for j in range(len(stats)):
        print(f'{stats_names[j]}: {stats[j][i]}')
        if(categories[i] == "TLC"):
          #print("1 runned")
          if (stats_names[j] == 'Minimum'):
            T1_min = stats[j][i]
          elif (stats_names[j] == 'Q1'):
            T1_q1 = stats[j][i]
          elif (stats_names[j] == 'Q3'):
            T1_q3 = stats[j][i]
          elif (stats_names[j] == 'Maximum'):
            T1_maximums_N = stats[j][i]
        if(categories[i] == 'Protein'):
          if (stats_names[j] == 'Minimum'):
            T2_min = stats[j][i]
          elif (stats_names[j] == 'Q1'):
            T2_q1 = stats[j][i]
          elif (stats_names[j] == 'Q3'):
            T2_q3 = stats[j][i]
          elif (stats_names[j] == 'Maximum'):
            T2_maximums_N = stats[j][i]
        if(categories[i] == 'Sugar'):
          if (stats_names[j] == 'Minimum'):
            T3_min = stats[j][i]
          elif (stats_names[j] == 'Q1'):
            T3_q1 = stats[j][i]
          elif (stats_names[j] == 'Q3'):
            T3_q3 = stats[j][i]
          elif (stats_names[j] == 'Maximum'):
            T3_maximums_N = stats[j][i]
    print('\n')

#graph for PM

data = pd.DataFrame(df3, columns = ['TLC', 'Protein', 'Sugar'])
#creating axes instance
fig = plt.figure(figsize=(10,7))

#Creating Box plot
#bp = plt.boxplot(data,notch='True',patch_artist = True, labels = ['TLC', 'Protein', 'Sugar'] )
bp = plt.boxplot(data, labels = ['TLC', 'Protein', 'Sugar'], showmeans = True )
#Ploting data points
#plt.plot(1 ,200) #{Here, ny default - tlc = 1, pro = 2, sugar = 3}
plt.scatter(x=1,y=a, label = 'Scatter', color ='r', marker = 's', s = 100)
plt.scatter(x=2,y=f, label = 'Scatter', color ='r', marker = 's', s = 100)
plt.scatter(x=3,y=g, label = 'Scatter', color ='r', marker = 's', s = 100)

#show plot
plt.show()
#plt.title("PM Category")

#Stats for PM CATEGORY -

#Getting each value of data -
medians_P = [round(item.get_ydata()[0], 1) for item in bp['medians']]
means_P = [round(item.get_ydata()[0],1) for item in bp['means']]

minimums_P = [round(item.get_ydata()[0], 1) for item in bp['caps']][::2]
maximums_P = [round(item.get_ydata()[0], 1) for item in bp['caps']][1::2]

q1_P = [round(min(item.get_ydata()), 1) for item in bp['boxes']]
q3_P = [round(max(item.get_ydata()), 1) for item in bp['boxes']]

fliers_P = [item.get_ydata() for item in bp['fliers']]
lower_outliers_P = []
upper_outliers_P = []
for i in range(len(fliers_P)):
    lower_outliers_by_box_P = []
    upper_outliers_by_box_P = []
    for outlier in fliers_P[i]:
        if outlier < q1_P[i]:
            lower_outliers_by_box_P.append(round(outlier, 1))
        else:
            upper_outliers_by_box_P.append(round(outlier, 1))
    lower_outliers_P.append(lower_outliers_by_box_P)
    upper_outliers_P.append(upper_outliers_by_box_P)

print(" ************************************ ")
print(" STATS FOR PM CATEGORY ARE : ")
print(" ************************************ ")

#Declaring for further purpose of calculating scores -
P1_min = 0
P1_q1 = 0
P1_q3 = 0
P1_maximums_N = 0
P2_min = 0
P2_q1 = 0
P2_q3 = 0
P2_maximums_N = 0
P3_min = 0
P3_q1 = 0
P3_q3 = 0
P3_maximums_N = 0

#same as above code but combined
stats = [medians_P, means_P, minimums_P, maximums_P, q1_P, q3_P, lower_outliers_P, upper_outliers_P]
stats_names = ['Median', 'Mean', 'Minimum', 'Maximum', 'Q1', 'Q3', 'Lower outliers', 'Upper outliers']
categories = ['TLC', 'Protein', 'Sugar'] # to be updated
for i in range(len(categories)):
    print(f'\033[1m{categories[i]}\033[0m')
    for j in range(len(stats)):
        print(f'{stats_names[j]}: {stats[j][i]}')
        if(categories[i] == "TLC"):
          #print("1 runned")
          if (stats_names[j] == 'Minimum'):
            P1_min = stats[j][i]
          elif (stats_names[j] == 'Q1'):
            P1_q1 = stats[j][i]
          elif (stats_names[j] == 'Q3'):
            P1_q3 = stats[j][i]
          elif (stats_names[j] == 'Maximum'):
            P1_maximums_N = stats[j][i]
        if(categories[i] == 'Protein'):
          if (stats_names[j] == 'Minimum'):
            P2_min = stats[j][i]
          elif (stats_names[j] == 'Q1'):
            P2_q1 = stats[j][i]
          elif (stats_names[j] == 'Q3'):
            P2_q3 = stats[j][i]
          elif (stats_names[j] == 'Maximum'):
            P2_maximums_N = stats[j][i]
        if(categories[i] == 'Sugar'):
          if (stats_names[j] == 'Minimum'):
            P3_min = stats[j][i]
          elif (stats_names[j] == 'Q1'):
            P3_q1 = stats[j][i]
          elif (stats_names[j] == 'Q3'):
            P3_q3 = stats[j][i]
          elif (stats_names[j] == 'Maximum'):
            P3_maximums_N = stats[j][i]
    print('\n')

"""Predicting intensities -
1. Low (1)
2. Medium (2)
3. High (3)
"""

#Predicting scores
#score1 = normal
#score2 = tbm
#score3 = pm


sn1 = 0
st1 = 0
sp1 = 0
sn2 = 0
st2 = 0
sp2 = 0
sn3 = 0
st3 = 0
sp3 = 0


# print(N1_min)
# print()
#********* For normal ************
#for TLC (Parameter 1 ):
if ( N1_min <= a <= N1_q1 ):
  sn1 = 1
elif ( N1_q1 < a <= N1_q3 ):
  sn1 = 2
elif( N1_q3 < a <= N1_maximums_N):
  sn1 = 3
#For Protein( parameter 2 ):
if ( N2_min <= f <= N2_q1 ):
  st1 = 1
elif ( N2_q1 < f <= N2_q3 ):
  st1 = 2
elif( N2_q3 < f <= N2_maximums_N):
  st1 = 3
#For Sugar ( parameter 3 ):
if ( N3_min <= g <= N3_q1 ):
  sp1 = 1
elif ( N3_q1 < g <= N3_q3 ):
  sp1 = 2
elif( N3_q3 < g <= N3_maximums_N):
  sp1 = 3
#calculating normal score
score1 = (sn1 + st1 + sp1)/3
print("**********************")
print("Score for Normal = ", score1)
print("**********************")


#********* For tbm ************
#for TLC (Parameter 1 ):
if ( T1_min <= a <= T1_q1 ):
  sn2 = 1
elif ( T1_q1 < a <= T1_q3 ):
  sn2 = 2
elif( T1_q3 < a <= T1_maximums_N):
  sn2 = 3
#For Protein( parameter 2 ):
if ( T2_min <= f <= T2_q1 ):
  st2 = 1
elif ( T2_q1 < f <= T2_q3 ):
  st2 = 2
elif( T2_q3 < f <= T2_maximums_N):
  st2 = 3
#For Sugar ( parameter 3 ):
if ( T3_min <= g <= T3_q1 ):
  sp2 = 1
elif ( T3_q1 < g <= T3_q3 ):
  sp2 = 2
elif( T3_q3 < g <= T3_maximums_N):
  sp2 = 3
#calculating tbm score
score2 = (sn2 + st2 + sp2)/3
print("**********************")
print("Score for TBM = ", score2)
print("**********************")


#********* For pm ************
#for TLC ( Parameter 1 ):
if ( P1_min <= a  <= P1_q1 ):
  sn3 = 1
elif ( P1_q1 < a <= P1_q3 ):
  sn3 = 2
elif( P1_q3 < a <= P1_maximums_N):
  sn3 = 3
#For Protein( parameter 2 ):
if ( P2_min <= f <= P2_q1 ):
  st3 = 1
elif ( P2_q1 < f <= P2_q3 ):
  st3 = 2
elif( P2_q3 < f <= P2_maximums_N):
  st3 = 3
#For Sugar ( parameter 3 ):
if ( P3_min <= g <= P3_q1 ):
  sp3 = 1
elif ( P3_q1 < g <= P3_q3 ):
  sp3 = 2
elif( P3_q3 < g <= P3_maximums_N):
  sp3 = 3
#calculating normal score
score3 = (sn3 + st3 + sp3)/3
print("**********************")
print("Score for PM = ", score3)
print("**********************")

#CALCULTING INTENSITIES OF EACH DISEASE -
#Plotting graph too.
import matplotlib.pyplot as plt #for graph

'''
## First Ranges
1 - 1.5
1.5 - 2.5
2.5 - 3

## Editing Ranges1 :
1 - 1.6
1.6 - 2.3
2.3 - 3

#Editing Ranges2 -
0.5 - 1.6
1.6 - 2.3
2.3 - 3
'''

#making graph
plt.figure(figsize = (8,8))
plt.xlim(-10,10) #x axis limit
plt.ylim(-10,10) # y axis limit
axis = plt.gca() #get current axes

#plotting labels for graph
plt.text(x = -9 , y = 9 , s = " TUBERCULOSIS MENINGITIS ", fontdict=dict(color='black',size=10), bbox=dict(facecolor='paleturquoise',alpha=0.8)) #plotting txt - TBM
plt.text(x = 2 , y = 9, s = " PYOGENIC MENINGITIS ", fontdict=dict(color='black',size=10), bbox=dict(facecolor='paleturquoise',alpha=0.8)) #plotting txt - PM
plt.text(x = -1.5, y = -1 , s = " NORMAL ", fontdict=dict(color='black',size=10), bbox=dict(facecolor='paleturquoise',alpha=0.8)) #plotting txt - NORMAL

#plotting points
print("***************************")
print("Intensity of NORMAL - ")
if (0.5 <= score1 <= 3):
  plt.text(x = -2, y = -5 ,s = " COMPLETELY NORMAL ", fontdict=dict(color='white',size=9), bbox=dict(facecolor='green',alpha=0.8)) #plotting txt
  print("Asymptotic")

'''
if (0.5 <= score1 <= 1.6 ):
  plt.scatter(x = 2, y = 2, label = 'Scatter', color ='gold', marker = 'o', s = 100 )
  plt.text(x = 2, y = 2.7 ,s = " Mild Meningitis ", fontdict=dict(color='purple',size=10), bbox=dict(facecolor='papayawhip',alpha=0.5)) #Plotting text
  print("Low")
elif (1.6 < score1 <= 2.3):
  plt.scatter(x = 4.6, y = 4.6, label = s'Scatter', color ='darkorange', marker = 'o', s = 200 )
  plt.text(x = 4.9, y = 5.3 ,s = " Severe Meningitis ", fontdict=dict(color='darkblue',size=10), bbox=dict(facecolor='antiquewhite',alpha=0.5)) #plotting txt
  print("Medium")
elif (2.3 < score1 <= 3):
  plt.scatter(x = 7, y = 7, label = 'Scatter', color ='red', marker = 'o', s = 300 )
  plt.text(x = 7, y = 7.8 ,s = " Highly severe Meningitis ", fontdict=dict(color='maroon',size=10), bbox=dict(facecolor='cornsilk',alpha=0.5)) #plotting txt
  print("High")
else:
  plt.text(x = -2, y = -5 ,s = " Asymptomatic ", fontdict=dict(color='white',size=9), bbox=dict(facecolor='green',alpha=0.8)) #plotting txt
  print("Asymptotic")
'''


print("***************************")
print("Intensity of TBM - ")
if (0.5 <= score2 <= 1.6 ):
  plt.scatter(x = -2, y = 2, label = 'Scatter', color ='gold', marker = 'o', s = 100 )
  plt.text(x = -2, y = 2.7 ,s = " Mild Meningitis ", fontdict=dict(color='purple',size=10), bbox=dict(facecolor='papayawhip',alpha=0.5)) #Plotting text
  print("Low")
elif (1.6 < score2 <= 2.3):
  plt.scatter(x = -4.6, y = 4.6, label = 'Scatter', color ='darkorange', marker = 'o', s = 200 )
  plt.text(x = -4.9, y = 5.3 ,s = " Severe Meningitis ", fontdict=dict(color='darkblue',size=10), bbox=dict(facecolor='antiquewhite',alpha=0.5)) #plotting txt
  print("Medium")
elif (2.3 < score2 <= 3):
  plt.scatter(x = -7, y = 7, label = 'Scatter', color ='red', marker = 'o', s = 300 )
  plt.text(x = -7, y = 7.8 ,s = " Highly severe Meningitis ", fontdict=dict(color='maroon',size=10), bbox=dict(facecolor='cornsilk',alpha=0.5)) #plotting txt
  print("High")
else:
  plt.text(x = -7, y = 5 ,s = " Asymptomatic ", fontdict=dict(color='white',size=9), bbox=dict(facecolor='green',alpha=0.8)) #plotting txt
  print("Asymptotic")


print("***************************")
print("Intensity of PM - ")
if (0.5 <= score3 <= 1.6 ):
  plt.scatter(x = 2, y = 2, label = 'Scatter', color ='gold', marker = 'o', s = 100 )
  plt.text(x = 2, y = 2.7 ,s = " Mild Meningitis ", fontdict=dict(color='purple',size=10), bbox=dict(facecolor='papayawhip',alpha=0.5)) #Plotting text
  print("Low")
elif (1.6 < score3 <= 2.3):
  plt.scatter(x = 4.6, y = 4.6, label = 'Scatter', color ='darkorange', marker = 'o', s = 200 )
  plt.text(x = 4.9, y = 5.3 ,s = " Severe Meningitis ", fontdict=dict(color='darkblue',size=10), bbox=dict(facecolor='antiquewhite',alpha=0.5)) #plotting txt
  print("Medium")
elif (2.3 < score3 <= 3):
  plt.scatter(x = 7, y = 7, label = 'Scatter', color ='red', marker = 'o', s = 300 )
  plt.text(x = 7, y = 7.8 ,s = " Highly severe Meningitis ", fontdict=dict(color='maroon',size=10), bbox=dict(facecolor='cornsilk',alpha=0.5)) #plotting txt
  print("High")
else:
  plt.text(x = 3, y = 5 ,s = " Asymptomatic ", fontdict=dict(color='white',size=9), bbox=dict(facecolor='green',alpha=0.8)) #plotting txt for asym
  print("Asymptotic")


plt.plot(axis.get_xlim(), [0,0], 'k--')  #x axis plot line across
#plt.plot([0,0],axis.get_xlim(), 'k--')   #y axis plot line across
plt.vlines(x=0, ymin=0, ymax=10, color='k', linestyle='--')
plt.ylabel('Y - axis')
plt.xlabel('X - axis')
plt.title(" Intensity of Meningitis ")
#plt.grid()
#plt.legend()
plt.show()