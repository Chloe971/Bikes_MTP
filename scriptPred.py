import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import prediction 
import os

__file__ = 'scriptPred.py'
url='https://docs.google.com/spreadsheets/d/e/2PACX-1vQVtdpXMHB4g9h75a0jw8CsrqSuQmP5eMIB2adpKR5hkRggwMwzFy5kB-AIThodhVHNLxlZYm8fuoWj/pub?gid=2105854808&single=true&output=csv'
target_name = os.path.join(os.path.dirname(os.path.realpath(__file__)), "prediction","data", "bikes.csv")
data= prediction.Load_data(url, target_name).save_as_df(target_name) 
data = prediction.format_bike(data)

data['Day of Week'] = data['Date'].apply(lambda time: time.dayofweek)
data['Year'] = data['Date'].apply(lambda t: t.year)
data.columns=['Date','Heure','Todaystotal','DayOfWeek','Year']
data['Heure'] = data['Heure'].str.replace(':','-')

lis1 = data.DayOfWeek
lis2 = data.Heure
lis3 = data.Todaystotal
lis4 = data.Date
lis5 = data.Year

df = pd.DataFrame(list(zip(lis1,lis2,lis3,lis4,lis5)), columns = ['DayOfWeek','Heure',"Todaystotal","Date","Year"])
P = df[(df.Heure > '01:00') & (df.Heure < '08:00')]

P0 = df[(df.Heure > '23:59') & (df.Heure < '00:01')].tail(30)
P1 = df[(df.Heure > '00:01') & (df.Heure < '01:00')].tail(30)
P2 = df[(df.Heure > '01:00') & (df.Heure < '02:00')].tail(30)
P3 = df[(df.Heure > '02:00') & (df.Heure < '03:00')].tail(30)
P4 = df[(df.Heure > '03:00') & (df.Heure < '04:00')].tail(30)
P5 = df[(df.Heure > '04:00') & (df.Heure < '05:00')].tail(30)
P6 = df[(df.Heure > '05:00') & (df.Heure < '06:00')].tail(30)
P7 = df[(df.Heure > '06:00') & (df.Heure < '07:00')].tail(30)
P8 = df[(df.Heure > '07:00') & (df.Heure < '08:00')].tail(30)


#Moyenne de P1
milanoData1 = P1['Todaystotal']
moyenne1 = np.mean(milanoData1)

print ("Moyenne de P1 est : ", round(moyenne1, 2))


#Moyenne de P2
milanoData2 = P2['Todaystotal']
moyenne2 = np.mean(milanoData2)

print ("Moyenne de P2 est : ", round(moyenne2, 2))


#Moyenne de P4
milanoData4 = P4['Todaystotal']
moyenne4 = np.mean(milanoData4)

print ("Moyenne de P4 est : ", round(moyenne4, 2))


#Moyenne de P5
milanoData5 = P5['Todaystotal']
moyenne5 = np.mean(milanoData5)

print ("Moyenne de P5 est : ", round(moyenne5, 2))
print ("----------------------------------------")
#Moyenne de P6
milanoData6 = P6['Todaystotal']
moyenne6 = np.mean(milanoData6)

print ("Moyenne de P6 est : ", round(moyenne6, 2))


#Moyenne de P7
milanoData7 = P7['Todaystotal']
moyenne7 = np.mean(milanoData7)

print ("Moyenne de P7 est : ", round(moyenne7, 2))

#Moyenne de P8
milanoData8 = P8['Todaystotal']
moyenne8 = np.mean(milanoData8)

print ("Moyenne de P8 est : ", round(moyenne8, 2))
print ("----------------------------------------")

#Médiane de P1
mediane1 = np.median(milanoData1)
print ("La mediane de P1 est : ", round(mediane1, 2))

#Médiane de P2
mediane2 = np.median(milanoData2)
print ("La mediane de P2 est : ", round(mediane2, 2))

#Médiane de P4
mediane4 = np.median(milanoData4)
print ("La mediane de P2 est : ", round(mediane4, 2))

#Médiane de P5
mediane5 = np.median(milanoData5)
print ("La mediane de P5 est : ", round(mediane5, 2))

#Médiane de P6
mediane6 = np.median(milanoData6)
print ("La mediane de P6 est : ", round(mediane6, 2))

#Médiane de P7
mediane7 = np.median(milanoData7)
print ("La mediane de P7 est : ", round(mediane7, 2))

#Médiane de P8
mediane8 = np.median(milanoData8)
print ("La mediane de P8 est : ", round(mediane8, 2))

print ("----------------------------------------")

print(moyenne1+moyenne2+moyenne4+moyenne5+moyenne6+moyenne7+moyenne8)
print ("----------------------------------------")
print(mediane1+mediane2+mediane4+mediane5+mediane6+mediane7+mediane8)

#Il est plus intéressant de regarder les données depuis le début du couvre-feu à 18h-06h. 
#Or on ne peut pas P1 car la date prise était pendant les vacances sans couvre-feu ni confinement (2020-03-07,2020-08-21)
#Donc depuis le couvre-feu à 18h qui à été déclaré le 2 Janvier, Il n'y a plus eu de vélos entre 1h et 2h du matin; donc compter sa moyenne et sa médiane fausseraient la prédiction. 

#Nous ne pouvons pas prendre P2 aussi car nous avons des données prises seulement en 2020 lorsqu'il n'y avait pas de couvre-feu. 

#Meme chose pour P4
#Meme chose pour P5

#Nous commencerons à avoir des valeurs qui nous sont utiles à la prédiction à partir de P6 soit à partir de 6h du matin soit la levée du couvre-feu.
#Pour cela, on applique un filtre sur l'année. 

#P6 depuis 1 janvier 2021
filtre = df.query('Year > 2020 ')
P6New = filtre[(filtre.Heure > '05:00') & (filtre.Heure < '06:00')].tail(30)

print ("----------------------------------------")

#P7 depuis 1 janvier 2021
filtre = df.query('Year > 2020 ')
P7New = filtre[(filtre.Heure > '06:00') & (filtre.Heure < '07:00')].tail(30)

print ("----------------------------------------")

#P8 depuis 1 janvier 2021
filtre = df.query('Year > 2020 ')
P8New = filtre[(filtre.Heure > '07:00') & (filtre.Heure < '08:00')].tail(30)
print(P8New)

print ("----------------------------------------")

#Moyenne de P6New
milanoData6New = P6New['Todaystotal']
moyenne6New = np.mean(milanoData6New)

print ("Moyenne de P6New est : ", round(moyenne6New, 2))

#Moyenne de P7New
milanoData7New = P7New['Todaystotal']
moyenne7New = np.mean(milanoData7New)

print ("Moyenne de P7New est : ", round(moyenne7New, 2))

#Moyenne de P8New
milanoData8New = P8New['Todaystotal']
moyenne8New = np.mean(milanoData8New)
print ("Moyenne de P8New est : ", round(moyenne8New, 2))

print ("----------------------------------------")

#Médiane de P6New
milanoData6New = P6New['Todaystotal']
mediane6New = np.median(milanoData6New)
print ("La mediane de P6New est : ", round(mediane6New, 2))

#Médiane de P7New
milanoData7New = P7New['Todaystotal']
mediane7New = np.median(milanoData7New)
print ("La mediane de P7New est : ", round(mediane7New, 2))

#Médiane de P8New
mediane8New = np.median(milanoData8New)
print ("La mediane de P8New est : ", round(mediane8New, 2))

print ("----------------------------------------")

print(moyenne6New + moyenne7New + moyenne8New)
print ("----------------------------------------")
print(mediane6New + mediane7New + mediane8New)