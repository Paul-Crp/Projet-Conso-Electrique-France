import pandas as pd
import pooch
import os.path

if os.path.isfile('./consommation-annuelle-residentielle-par-adresse.csv'):
    print("File already exists, no need to download it again.")
else:
    print("Downloading data, file is 210 MB, may take a long time...")
    file_path = pooch.retrieve(
    url="https://data.enedis.fr/explore/dataset/consommation-annuelle-residentielle-par-adresse/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B",
    known_hash=None,
    fname="consommation-annuelle-residentielle-par-adrespise.csv",
    path="./",
    progressbar=True
    )

data = "./consommation-annuelle-residentielle-par-adresse.csv"
df = pd.read_csv(data, on_bad_lines='warn', sep=";")

ChoixVilles = ['Aix-en-Provence', "Angers", "Bordeaux", "Brest", "Clermont-Ferrand", "Dijon", "Le Havre", "Le Mans", "Lille", "Lyon", "Marseille", "Montpellier", "Nantes", "Nice", "Nîmes", "Paris", "Reims", "Rennes", "Saint-Denis", "Saint-Étienne", "Toulon", "Toulouse", "Villeurbanne"]
  
df.drop(df.columns[[1, 2, 3, 4, 5, 6, 7, 9, 14, 15]], axis=1, inplace=True)

dff = df[df['Nom de la commune'].str.lower().isin([x.lower() for x in ChoixVilles])]

d={}

for i in ChoixVilles:
    for a in [2018, 2019, 2020, 2021]:
        df1 = dff[dff['Année']==a]
        df2 = df1[df1['Nom de la commune'].str.lower().isin([i.lower()])]
        d["Total-{0}".format(i+str(a))] = round(df2['Consommation annuelle totale de l\'adresse (MWh)'].sum(),3)

print(d)

dff.to_csv('TableauTraité.csv', index=False)
