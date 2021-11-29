import pandas as pd
import numpy as np
import seaborn as sns
import math
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def passPrediction():

    df=pd.read_csv("F:\\academic_performance\\academic.csv")

    train,test=train_test_split(df,test_size=0.2)

    train_data=[]
    train_labels=['CNS_INTERNAL','UML_INTERNAL','MC_INTERNAL','STM_INTERNAL','HBD_INTERNAL','ATTENDANCE']
    train_data=train[train_labels].values.tolist()

    
    target=[]
    target=train['PASS/FAIL'].values.tolist()

    from sklearn.svm import SVC
    classifier=SVC(kernel='rbf',random_state=1)

    classifier.fit(train_data,target)

    return classifier

def cnsmarksPredict():
    df=pd.read_csv("F:\\academic_performance\\academic.csv")

    train,test=train_test_split(df,test_size=0.2)

    train_data=[]

    train_labels=['CNS_INTERNAL','ATTENDANCE']

    train_data=train[train_labels].values.tolist()

    
    target=[]

    target=train['CNS_EXTERNAL'].values.tolist()
    
    from sklearn.linear_model import LinearRegression

    model = LinearRegression()

    model.fit(train_data,target)

    return model

def umlmarksPredict():
    df=pd.read_csv("F:\\academic_performance\\academic.csv")

    train,test=train_test_split(df,test_size=0.2)

    train_data=[]

    train_labels=['UML_INTERNAL','ATTENDANCE']

    train_data=train[train_labels].values.tolist()

    
    target=[]

    target=train['UML_EXTERNAL'].values.tolist()
    
    from sklearn.linear_model import LinearRegression

    model = LinearRegression()

    model.fit(train_data,target)

    return model

def mcmarksPredict():
    df=pd.read_csv("F:\\academic_performance\\academic.csv")

    train,test=train_test_split(df,test_size=0.2)

    train_data=[]

    train_labels=['MC_INTERNAL','ATTENDANCE']

    train_data=train[train_labels].values.tolist()

    
    target=[]

    target=train['MC_EXTERNAL'].values.tolist()
    
    from sklearn.linear_model import LinearRegression

    model = LinearRegression()

    model.fit(train_data,target)

    return model

def stmmarksPredict():
    df=pd.read_csv("F:\\academic_performance\\academic.csv")

    train,test=train_test_split(df,test_size=0.2)

    train_data=[]

    train_labels=['STM_INTERNAL','ATTENDANCE']

    train_data=train[train_labels].values.tolist()

    
    target=[]

    target=train['STM_EXTERNAL'].values.tolist()
    
    from sklearn.linear_model import LinearRegression

    model = LinearRegression()

    model.fit(train_data,target)

    return model

def hbdmarksPredict():
    df=pd.read_csv("F:\\academic_performance\\academic.csv")

    train,test=train_test_split(df,test_size=0.2)

    train_data=[]

    train_labels=['HBD_INTERNAL','ATTENDANCE']

    train_data=train[train_labels].values.tolist()

    
    target=[]

    target=train['HBD_EXTERNAL'].values.tolist()
    
    from sklearn.linear_model import LinearRegression

    model = LinearRegression()

    model.fit(train_data,target)

    return model
