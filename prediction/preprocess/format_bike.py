import pandas as pd 
from datetime import date
import datetime
import time

def format_bike(data):
    data.columns=['Date','Heure','Grandtotal','Todaystotal', 'Unnamed','Remark']
    data.pop("Unnamed")
    data.pop("Remark")
    data.pop("Grandtotal")
    data.drop(0,0,inplace=True)
    data.drop(1,0,inplace=True)
    data['Date'] = pd.to_datetime(data['Date'])
    data['Heure'].fillna(0, inplace = True)

    return data

