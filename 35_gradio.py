# -*- coding: utf-8 -*-
"""35.Gradio.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11kCLblTRPz0yZ5pvfmHyPgWKzeHrZjXX
"""

# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn

# Import necessary modules
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt

# Keras specific
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical

#Importing libraries
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from sklearn.metrics import accuracy_score
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier, VotingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

df = pd.read_csv('Final2.csv')
print(df.shape)
#df.describe()

df.head()

target_column = ['Condition']
predictors = list(set(list(df.columns))-set(target_column))
# df[predictors] = df[predictors]/df[predictors].max()
df.describe()

X = df[predictors].values
y = df[target_column].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=40)
print(X_train.shape); print(X_test.shape)

# define the base models
gb_model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=10)
rf_model = RandomForestClassifier(n_estimators=100, max_depth=10)
knn_model = KNeighborsClassifier(n_neighbors=5)
svm_model = SVC(C=1.0, kernel='linear')

# train the base models on the training set
gb_model.fit(X_train, y_train)

# train the base models on the training set
rf_model.fit(X_train, y_train)

# train the base models on the training set
knn_model.fit(X_train, y_train)

# train the base models on the training set
svm_model.fit(X_train, y_train)

# Making the final model using voting classifier
model = VotingClassifier( estimators=[('m1_1', gb_model), ('m1_2', rf_model), ('m2_2', svm_model)], voting='hard')
#hard -> Majority
#soft -> average

model.fit(X_train, y_train)

#make prediciton
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

from sklearn.metrics import precision_recall_fscore_support
#Training set performance
#score = model.score(X_test,y_test)

model_train_acc = accuracy_score(y_train, y_train_pred)
model_test_acc = accuracy_score(y_test, y_test_pred)

# Calculate accuracy scores
train_error = 1 - accuracy_score(y_train, y_train_pred)
test_error = 1 - accuracy_score(y_test, y_test_pred)

precision, recall, f1score, support = precision_recall_fscore_support(y_test, y_test_pred, average='weighted')

print("PERFORMANCE MEASURE - ")
print("")
print("Training Accuracy: ", model_train_acc)
print("Train error:", train_error)
print("")
print("Testing Accuracy: ", model_test_acc)
print("Test error:", test_error)
print("")
print("Precision:", precision)
print("Recall:", recall)
print("F1 score:", f1score)

"""Predicting Intensities -
(Optimized code )


Detailed code => 28.ExistingModel_results.ipynb
"""

# #Taking input -
# print("Enter values of parameters : ")
# tlc = float(input("Enter TLC value: \n"))
# lym = float(input("Enter Lymphocytes value: \n"))
# poly = float(input("Enter Polymorphs value: \n"))
# mono = float(input("Enter Monocytes value: \n"))
# eosino = float(input("Enter Eosinophiles value: \n"))
# protein = float(input("Enter Protein value: \n"))
# sugar = float(input("Enter Sugar value: \n"))

# var = model.predict([[100,40,50]])

# print("***********************")
# print("The Disease is : ", var)

#converting array to string

# print(var)
# if(var == ['TBM']):
#   cond = 'tbm'
# elif(var == ['PM']):
#   cond = 'pm'
# else:
#   cond = 'normal'

# print(cond)

#t1(tlc)
#t2(pro)
#t3(sug)

#score1 = 0
#result =""
#value = ""

def intensity_pred(tlc, lym, poly, mono, eosino, protein, sugar):
  var = model.predict([[tlc, protein, sugar]])
  # if(var == ['TBM']):
  #   value = 'tbm'
  # elif(var == ['PM']):
  #   value = 'pm'
  # else:
  #   value = 'normal'
  #*****************************
  #If disease ==> PM **********
  if(var == ['PM']):
    if(80 <= tlc <= 287): #checking tlc
      tlc_score = 1
    elif( 287 < tlc <= 649):
      tlc_score = 2
    elif( 649 < tlc <= 958 ):
      tlc_score = 3
    else:
      tlc_score = 0
    if(74 <= protein <= 330): #checking pro
      protein_score = 1
    elif( 330 < protein <= 804):
      protein_score = 2
    elif( 804 < protein <= 1199 ):
      protein_score = 3
    else:
      protein_score = 0
    if(1 <= sugar <= 9): #checking sugar
      sugar_score = 1
    elif( 9 < sugar <= 23):
      sugar_score = 2
    elif( 23 < tlc <= 35 ):
      sugar_score = 3
    else:
      sugar_score = 0
    if(lym < poly):
      dlc_score = 1
    else:
      dlc_score = 0
    return [(tlc_score + protein_score + sugar_score + dlc_score)/3, 'PM'] # 0 - 3.3
  #*****************************
  #If disease ==> TBM ***********
  elif(var == ['TBM']):
    if(4 <= tlc <= 28): #checking tlc
      tlc_score = 1
    elif( 28 < tlc <= 79 ):
      tlc_score = 2
    elif( 79 < tlc <= 119 ):
      tlc_score = 3
    else:
      tlc_score = 0
    if(46 <= protein <= 65): #checking pro
      protein_score = 1
    elif( 65 < protein <= 84):
      protein_score = 2
    elif( 84 < protein <= 107 ):
      protein_score = 3
    else:
      protein_score = 0
    if(16 <= sugar <= 26): #checking sugar
      sugar_score = 1
    elif( 26 < sugar <= 39):
      sugar_score = 2
    elif( 39 < sugar <= 53 ):
      sugar_score = 3
    else:
      sugar_score = 0
    if(lym > poly):
      dlc_score = 1
    else:
      dlc_score = 0
    return [(tlc_score + protein_score + sugar_score + dlc_score)/3, 'TBM']
    #print("TBM score: ", score)
  #*******************************
  #If disease ==> NORMAL *********
  elif(var == ['Normal']): #checking for normal cases:
    return [10, 'Normal']
  else:
    return [-1,'Enter Correct Output']


# if __name__ == '__main__':
#   # score1, cond = intensity(531,90,10,0,0,160,625)
#   # print("Enter values of parameters : ")
#   tlc = float(input("Enter TLC value: \n"))
#   lym = float(input("Enter Lymphocytes value: \n"))
#   poly = float(input("Enter Polymorphs value: \n"))
#   mono = float(input("Enter Monocytes value: \n"))
#   eosino = float(input("Enter Eosinophiles value: \n"))
#   protein = float(input("Enter Protein value: \n"))
#   sugar = float(input("Enter Sugar value: \n"))
#   score1, cond = intensity(tlc, lym, poly, mono, eosino, protein, sugar)
#   #Calculating Intensities
#   # print("Condition is : ", cond)
#   if(score1 == -1):
#     result = 'Enter Correct Input'
#   elif(score1 == 10):
#     result = 'Completely_Normal'
#   elif(0.5 <= score1 <= 1.6):
#     result = cond + '_low'
#   elif(1.6 < score1 <= 2.3):
#     result = cond + '_med'
#   elif(2.3 < score1 <= 3.3):
#     result = cond + '_high'
#   print("***************************")
#   print("The Score is : ", score1)
#   print("The Intensity is : ", result)

"""Gradio now onwards"""

!pip install gradio

pip install --upgrade gradio

import gradio as gr
import numpy as np
import plotly.graph_objects as go

def intensity_pred(tlc, lym, poly, mono, eosino, protein, sugar):
  var = model.predict([[tlc, protein, sugar]])
  # if(var == ['TBM']):
  #   value = 'tbm'
  # elif(var == ['PM']):
  #   value = 'pm'
  # else:
  #   value = 'normal'
  #*****************************
  #If disease ==> PM **********
  if(var == ['PM']):
    if(80 <= tlc <= 287): #checking tlc
      tlc_score = 1
    elif( 287 < tlc <= 649):
      tlc_score = 2
    elif( 649 < tlc <= 958 ):
      tlc_score = 3
    else:
      tlc_score = 0
    if(74 <= protein <= 330): #checking pro
      protein_score = 1
    elif( 330 < protein <= 804):
      protein_score = 2
    elif( 804 < protein <= 1199 ):
      protein_score = 3
    else:
      protein_score = 0
    if(1 <= sugar <= 9): #checking sugar
      sugar_score = 1
    elif( 9 < sugar <= 23):
      sugar_score = 2
    elif( 23 < tlc <= 35 ):
      sugar_score = 3
    else:
      sugar_score = 0
    if(lym > poly):
      dlc_score = 1
    else:
      dlc_score = 0
    return [(tlc_score + protein_score + sugar_score + dlc_score)/3, 'PM']
  #*****************************
  #If disease ==> TBM ***********
  elif(var == ['TBM']):
    if(4 <= tlc <= 28): #checking tlc
      tlc_score = 1
    elif( 28 < tlc <= 79 ):
      tlc_score = 2
    elif( 79 < tlc <= 119 ):
      tlc_score = 3
    else:
      tlc_score = 0
    if(46 <= protein <= 65): #checking pro
      protein_score = 1
    elif( 65 < protein <= 84):
      protein_score = 2
    elif( 84 < protein <= 107 ):
      protein_score = 3
    else:
      protein_score = 0
    if(16 <= sugar <= 26): #checking sugar
      sugar_score = 1
    elif( 26 < sugar <= 39):
      sugar_score = 2
    elif( 39 < sugar <= 53 ):
      sugar_score = 3
    else:
      sugar_score = 0
    if(lym < poly):
      dlc_score = 1
    else:
      dlc_score = 0
    return [(tlc_score + protein_score + sugar_score + dlc_score)/3, 'TBM']
    #print("TBM score: ", score)
  #*******************************
  #If disease ==> NORMAL *********
  elif(var == ['Normal']): #checking for normal cases:
    return [10, 'Normal']
  else:
    return [-1,'Enter Correct Output']

def pred_disease(TLC,Lymphocytes,Polymorphs,Monocytes,Eosinophiles,Protein,Sugar):
  tlc1 = float(TLC)
  lym1 = float(Lymphocytes)
  poly1 = float(Polymorphs)
  mono1 = float(Monocytes)
  eosino1 = float(Eosinophiles)
  pro1 = float(Protein)
  sugar1 = float(Sugar)
  score1, cond = intensity_pred(tlc1,lym1,poly1,mono1,eosino1,pro1,sugar1)
  #Calculating Intensities
  if(score1 == -1):
    result = 'Enter Correct Input'
  elif(score1 == 10):
    result = 'Completely_Normal'
  elif(0.5 <= score1 <= 1.6):
    result = cond + '_Mild_Meningitis'
  elif(1.6 < score1 <= 2.3):
    result = cond + '_Severe_Meningitis'
  elif(2.3 < score1 <= 3.3):
    result = cond + '_Highly_Severe_Meningitis'
  fig1 = graph_plot(result)
  return [result,fig1]

#Inputs
# tbm low => 500,90,10,0,0,96,35

#function to plot graphs

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
import matplotlib.pyplot as plt

def graph_plot(result):
  #making graph
  fig = plt.figure(figsize = (6.5,6.5))
  plt.xlim(-10,10) #x axis limit
  plt.ylim(-10,10) # y axis limit
  axis = plt.gca() #get current axes

  #plotting labels for graph
  plt.text(x = -9 , y = 9 , s = " TUBERCULOSIS MENINGITIS ", fontdict=dict(color='black',size=10), bbox=dict(facecolor='paleturquoise',alpha=0.8)) #plotting txt - TBM
  plt.text(x = 2 , y = 9, s = " PYOGENIC MENINGITIS ", fontdict=dict(color='black',size=10), bbox=dict(facecolor='paleturquoise',alpha=0.8)) #plotting txt - PM
  plt.text(x = -1.5, y = -1 , s = " NORMAL ", fontdict=dict(color='black',size=10), bbox=dict(facecolor='paleturquoise',alpha=0.8)) #plotting txt - NORMAL

  #plotting points
  if(result == 'TBM_Mild_Meningitis'):
    plt.scatter(x = -2, y = 2, label = 'Scatter', color ='gold', marker = 'o', s = 100 )
    plt.text(x = -2, y = 2.7 ,s = " Mild Meningitis ", fontdict=dict(color='purple',size=10), bbox=dict(facecolor='papayawhip',alpha=0.5)) #Plotting text
    plt.text(x = 3, y = 5 ,s = " Asymptomatic ", fontdict=dict(color='white',size=9), bbox=dict(facecolor='green',alpha=0.8)) #plotting txt for asym for pm
    print("Asymptotic")
  elif(result == 'TBM_Severe_Meningitis'):
    plt.scatter(x = -4.6, y = 4.6, label = 'Scatter', color ='darkorange', marker = 'o', s = 200 )
    plt.text(x = -4.9, y = 5.3 ,s = " Severe Meningitis ", fontdict=dict(color='darkblue',size=10), bbox=dict(facecolor='antiquewhite',alpha=0.5)) #plotting txt
    plt.text(x = 3, y = 5 ,s = " Asymptomatic ", fontdict=dict(color='white',size=9), bbox=dict(facecolor='green',alpha=0.8)) #plotting txt for asym
    print("Asymptotic")
  elif(result == 'TBM_Highly_Severe_Meningitis'):
    plt.scatter(x = -7, y = 7, label = 'Scatter', color ='red', marker = 'o', s = 300 )
    plt.text(x = -7, y = 7.8 ,s = " Highly severe Meningitis ", fontdict=dict(color='maroon',size=10), bbox=dict(facecolor='cornsilk',alpha=0.5)) #plotting txt
    plt.text(x = 3, y = 5 ,s = " Asymptomatic ", fontdict=dict(color='white',size=9), bbox=dict(facecolor='green',alpha=0.8)) #plotting txt for asym
    print("Asymptotic")
  elif(result == 'PM_Mild_Meningitis'):
    plt.scatter(x = 2, y = 2, label = 'Scatter', color ='gold', marker = 'o', s = 100 )
    plt.text(x = 2, y = 2.7 ,s = " Mild Meningitis ", fontdict=dict(color='purple',size=10), bbox=dict(facecolor='papayawhip',alpha=0.5)) #Plotting text
    plt.text(x = -7, y = 5 ,s = " Asymptomatic ", fontdict=dict(color='white',size=9), bbox=dict(facecolor='green',alpha=0.8)) #plotting txt for tbm
    print("Asymptotic")
  elif(result == 'PM_Severe_Meningitis'):
    plt.scatter(x = 4.6, y = 4.6, label = 'Scatter', color ='darkorange', marker = 'o', s = 200 )
    plt.text(x = 4.9, y = 5.3 ,s = " Severe Meningitis ", fontdict=dict(color='darkblue',size=10), bbox=dict(facecolor='antiquewhite',alpha=0.5)) #plotting txt
    plt.text(x = -7, y = 5 ,s = " Asymptomatic ", fontdict=dict(color='white',size=9), bbox=dict(facecolor='green',alpha=0.8)) #plotting txt
    print("Asymptotic")
  elif(result == 'PM_Highly_Severe_Meningitis'):
    plt.scatter(x = 7, y = 7, label = 'Scatter', color ='red', marker = 'o', s = 300 )
    plt.text(x = 7, y = 7.8 ,s = " Highly severe Meningitis ", fontdict=dict(color='maroon',size=10), bbox=dict(facecolor='cornsilk',alpha=0.5)) #plotting txt
    plt.text(x = -7, y = 5 ,s = " Asymptomatic ", fontdict=dict(color='white',size=9), bbox=dict(facecolor='green',alpha=0.8)) #plotting txt
    print("Asymptotic")
  elif(result == 'Completely_Normal'):
    plt.text(x = -2, y = -5 ,s = " COMPLETELY NORMAL ", fontdict=dict(color='white',size=9), bbox=dict(facecolor='green',alpha=0.8)) #plotting txt
    plt.text(x = -7, y = 5 ,s = " Asymptomatic ", fontdict=dict(color='white',size=9), bbox=dict(facecolor='green',alpha=0.8)) #plotting txt -> asym for tbm
    plt.text(x = 3, y = 5 ,s = " Asymptomatic ", fontdict=dict(color='white',size=9), bbox=dict(facecolor='green',alpha=0.8)) #plotting txt for asym -> for pm
  plt.plot(axis.get_xlim(), [0,0], 'k--')  #x axis plot line across
  plt.vlines(x=0, ymin=0, ymax=10, color='k', linestyle='--')
  plt.ylabel('Y - axis')
  plt.xlabel('X - axis')
  plt.title(" Intensity of Meningitis ")
  plt.show()
  return fig

'''
Just for ref -
#plotting points
print("***************************")
print("Intensity of NORMAL - ")
if (0.5 <= score1 <= 3):
print("***************************")
print("Intensity of TBM - ")

elif (1.6 < score2 <= 2.3):

elif (2.3 < score2 <= 3):

else:
  plt.text(x = -7, y = 5 ,s = " Asymptomatic ", fontdict=dict(color='white',size=9), bbox=dict(facecolor='green',alpha=0.8)) #plotting txt
  print("Asymptotic")
print("***************************")
print("Intensity of PM - ")
if (0.5 <= score3 <= 1.6 ):

elif (1.6 < score3 <= 2.3):

elif (2.3 < score3 <= 3):

else:
  plt.text(x = 3, y = 5 ,s = " Asymptomatic ", fontdict=dict(color='white',size=9), bbox=dict(facecolor='green',alpha=0.8)) #plotting txt for asym
  print("Asymptotic")
'''

#interface


TLC = gr.inputs.Textbox(label = "TLC (Cubic per milimeter)"),
lymphocytes = ["text", "checkbox", gr.Slider(minimum = 0, maximum = 100, default=0, label = "Lymphocytes (0% -100%)")],
polymorphs = ["text", "checkbox", gr.Slider(minimum = 0, maximum = 100, default=0, label = "Polymorphs (0% -100%)")],
monocytes = ["text", "checkbox", gr.Slider(minimum = 0, maximum = 100, default=0, label = "Monocytes (0% -100%)")],
eosinophiles = ["text", "checkbox", gr.Slider(minimum = 0, maximum = 100, default=0, label = "Eosinophiles (0% -100%)")],
protein = ["text", "checkbox", gr.Slider(minimum = 0, maximum = 1000, default=0, label = "Protein (mg/dl)")],
sugar = ["text", "checkbox", gr.Slider(minimum = 0, maximum = 1000, default=0, label = "Sugar (mg/dl)")],
output = ["text","plot"]
submit_btn = gr.Button("Submit")

demo = gr.Interface(fn = pred_disease , inputs=["text", "text","text","text","text","text","text"], outputs = output,
                    layout = 'vertical', title="Diagnosis of Meningitis", description="Differentiating Tuberculosis & pyogenic meningitis", theme = 'peach')
theme = gr.themes.Default(primary_hue=gr.themes.colors.blue, secondary_hue=gr.themes.colors.orange)


#Only text box as input
demo = gr.Interface(fn = pred_disease , inputs=["text", "text","text","text","text","text","text"], outputs = output,
                    layout = 'vertical', title="Diagnosis of Tuberculous and Pyogenic Meningitis")

# #All slides as input
# demo = gr.Interface(fn = pred_disease , inputs=[gr.inputs.Slider(minimum = 0, maximum = 1000, default=0),
#                                                 gr.inputs.Slider(minimum = 0, maximum = 100, default=0),
#                                                 gr.inputs.Slider(minimum = 0, maximum = 100, default=0),
#                                                 gr.inputs.Slider(minimum = 0, maximum = 100, default=0),
#                                                 gr.inputs.Slider(minimum = 0, maximum = 100, default=0),
#                                                 gr.inputs.Slider(minimum = 0, maximum = 1000, default=0),
#                                                 gr.inputs.Slider(minimum = 0, maximum = 1000, default=0)], outputs = output,
#                     layout = 'vertical', title="Diagnosis of Tuberculosis and Pyogenic Meningitis")

# demo.inputs[0].label = "Enter TLC value"  # Renaming the first textbox
# demo.inputs[1].label = "Enter Lymphocytes value"  # Renaming the second textbox
# demo.inputs[2].label = "Enter Polymorphs value"  # Renaming the third textbox
# demo.inputs[3].label = "Enter Monocytes value"  # Renaming the fourth textbox
# demo.inputs[4].label = "Enter Eosinophils value"  # Renaming the fifth textbox
# demo.inputs[5].label = "Enter Protein value"  # Renaming the sixth textbox
# demo.inputs[6].label = "Enter Sugar value"  # Renaming the seventh textbox

if(__name__) == "__main__":
  demo.launch(debug = True)