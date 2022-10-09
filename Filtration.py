import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "./consommation-annuelle-residentielle-par-adresse.csv"
df = pd.read_csv(url, on_bad_lines='warn', sep=";")

ChoixVilles = ['Aix-en-Provence', "Angers", "Bordeaux", "Brest", "Clermont-Ferrand", "Dijon", "Grenoble", "Le Havre", "Le Mans", "Lille", "Lyon", "Marseille", "Montpellier", "Nantes", "Nice", "Nîmes", "Paris", "Reims", "Rennes", "Saint-Denis", "Saint-Étienne", "Strasbourg", "Toulon", "Toulouse", "Villeurbanne"]
  
df = df[df['Nom de la commune'].str.lower().isin([x.lower() for x in ChoixVilles])]

df.to_csv('TableauTraité.csv')