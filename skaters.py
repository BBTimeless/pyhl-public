import pandas as pd 

DATA = pd.read_csv('static/data/data_skater.csv')

def get_skater_data():
    return(DATA)

def get_skater_features():
    features = []
    for column in DATA.columns:
        features.append(column)
    return(features)
