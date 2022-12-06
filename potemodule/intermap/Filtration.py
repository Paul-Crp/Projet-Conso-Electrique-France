import pandas as pd


def Filtrer():
    ChoixVilles = ['Aix-en-Provence', "Angers", "Bordeaux", "Brest", "Clermont-Ferrand", "Dijon", "Le Havre", "Le Mans", "Lille", "Lyon", "Marseille",
                   "Montpellier", "Nantes", "Nice", "Nîmes", "Paris", "Reims", "Rennes", "Saint-Denis", "Saint-Etienne", "Saint-Étienne", "Toulon", "Toulouse", "Villeurbanne"]
    df = pd.read_csv('./potemodule/intermap/data/conso.csv',
                     on_bad_lines='warn', sep=";", low_memory=False)
    df.drop(df.columns[[1, 2, 3, 4, 5, 6, 7, 9, 14, 15]], axis=1, inplace=True)

    # On a la liste des villes les plus grandes de France, on retire les donneés qui ne nous intéressent pas dans le csv.

    dff = df[df['Nom de la commune'].str.lower().isin([x.lower()
                                                       for x in ChoixVilles])]

    d = {}
    # Ce dictionnaire va contenir les données que l'on va utiliser pour la carte, la ville, l'année et la conso.

    for i in ChoixVilles:
        for a in [2018, 2019, 2020, 2021]:
            try:
                df1 = dff[dff['Année'] == a]
                df2 = df1[df1['Nom de la commune'].str.lower().isin([
                    i.lower()])]
                d["Total-{0}".format(i+str(a))] = df2.iat[1, 5]
            except IndexError:
                # Pour des raisons inconnues, certaines villes n'ont pas de données pour 2018, ce qui fait que le df2.iat[1,5] est hors range. On les remplace donc par 0.
                d["Total-{0}".format(i+str(a))] = 0

    del d['Total-Saint-Etienne2019']
    del d['Total-Saint-Etienne2020']
    del d['Total-Saint-Etienne2021']
    del d['Total-Saint-Étienne2018']

    # Les données de Saint-Etienne en 2018 sont sans accents, mais celle des autres années sont avec.
    # Par simplicité, on a mis un doublon avec et sans accent dans la liste des villes, mais cela pose problème pour le dictionnaire.
    # On supprime donc les données vides avec parcimonie.

    return (d)
