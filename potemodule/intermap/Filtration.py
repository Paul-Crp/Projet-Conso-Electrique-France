import pandas as pd

def Filtrer():
    ChoixVilles = ['Aix-en-Provence', "Angers", "Bordeaux", "Brest", "Clermont-Ferrand", "Dijon", "Le Havre", "Le Mans", "Lille", "Lyon", "Marseille", "Montpellier", "Nantes", "Nice", "Nîmes", "Paris", "Reims", "Rennes", "Saint-Denis", "Saint-Etienne", "Saint-Étienne", "Toulon", "Toulouse", "Villeurbanne"]
    df = pd.read_csv('./potemodule/intermap/data/conso.csv', on_bad_lines='warn', sep=";",low_memory=False)
    df.drop(df.columns[[1, 2, 3, 4, 5, 6, 7, 9, 14, 15]], axis=1, inplace=True)

    dff = df[df['Nom de la commune'].str.lower().isin([x.lower() for x in ChoixVilles])]

    d={}

    for i in ChoixVilles:
        for a in [2018, 2019, 2020, 2021]:
            df1 = dff[dff['Année']==a]
            df2 = df1[df1['Nom de la commune'].str.lower().isin([i.lower()])]
            d["Total-{0}".format(i+str(a))] = round(df2['Consommation annuelle totale de l\'adresse (MWh)'].sum(),3)

    del d['Total-Saint-Etienne2019']
    del d['Total-Saint-Etienne2020']
    del d['Total-Saint-Etienne2021']
    del d['Total-Saint-Étienne2018']

    return(d)