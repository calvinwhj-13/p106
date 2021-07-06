import csv
import plotly.express as px
import numpy as np 
import pandas as pd 

def getDataSource(data_path) :
    coffee = [] 
    sleep = []

    with open(data_path) as csv_file :
        df = csv.DictReader(csv_file)
        for row in df :
            coffee.append(float(row('Coffee in ml'))) 
            sleep.append(float(row('sleep in hours')))
    return{'x' : temperature, 'y' : icecreamsales}

def findCorrelation(dataSource) :
    correlation = np.corrcoef(dataSource['x'], dataSource['y']) 
    print('correlation between temperature and ice cream sales : \n-->', correlation[0, 1])

df = pd.read_csv('cups of coffee vs hours of sleep.csv')
fig = px.scatter(df, x = "Coffee in ml", y = "sleep in hours")
fig.show() 

def setupMain() :
    path = 'cups of coffee vs hours of sleep.csv'
    dataSource = getDataSource(path)
    findCorrelation(dataSource)
setupMain() 