import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#^[^;]*;[^;]*;[^;]*;[^;]*;[^;]*;[^;]*;[^;]*;[^;]*;(Aix-en-Provence|Angers|Bordeaux|Brest|Clermont-Ferrand|Dijon|Grenoble|Le Havre|Le Mans|Lille|Lyon|Marseille|Montpellier|Nantes|Nice|Nîmes|Paris|Reims|Rennes|Saint-Denis|Saint-Étienne|Strasbourg|Toulon|Toulouse|Villeurbanne)

url = "./consommation-annuelle-residentielle-par-adresse.csv"
df = pd.read_csv(url, on_bad_lines='warn', sep=";")

df1=df[~(  df['Nom de la commune'] == "Aix-en-Provence") 
& ~ (  df['Nom de la commune'] == "Angers" )
& ~ (  df['Nom de la commune'] == "Bordeaux" )
& ~ (  df['Nom de la commune'] == "Brest" )
& ~ (  df['Nom de la commune'] == "Clermont-Ferrand" )
& ~ (  df['Nom de la commune'] == "Dijon" )
& ~ (  df['Nom de la commune'] == "Grenoble" )
& ~ (  df['Nom de la commune'] == "Le Havre" )
& ~ (  df['Nom de la commune'] == "Le Mans" )
& ~ (  df['Nom de la commune'] == "Lille" )
& ~ (  df['Nom de la commune'] == "Lyon" )
& ~ (  df['Nom de la commune'] == "Marseilles" )
& ~ (  df['Nom de la commune'] == "Montpellier" )
& ~ (  df['Nom de la commune'] == "Nantes" )
& ~ (  df['Nom de la commune'] == "Nice" )
& ~ (  df['Nom de la commune'] == "Nîmes" )
& ~ (  df['Nom de la commune'] == "Paris" )
& ~ (  df['Nom de la commune'] == "Reims" )
& ~ (  df['Nom de la commune'] == "Rennes" )
& ~ (  df['Nom de la commune'] == "Saint-Denis" )
& ~ (  df['Nom de la commune'] == "Saint-Étienne" )
& ~ (  df['Nom de la commune'] == "Strasbourg" )
& ~ (  df['Nom de la commune'] == "Toulon" )
& ~ (  df['Nom de la commune'] == "Toulouse" )
& ~ (  df['Nom de la commune'] == "Villeurbanne" ) ] .index

df.drop(df1, inplace = True)

df.to_csv('TableauTraité.csv')