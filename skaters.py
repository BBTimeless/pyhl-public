import pandas as pd 

DATA = pd.read_csv('static/data/data_skater.csv')

def get_skater_data():
    return(DATA)
