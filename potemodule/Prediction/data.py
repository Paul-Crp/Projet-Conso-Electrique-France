import pandas as pd
import os
import pooch
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)
from potemodule.Prediction import urls,paths

class Load():
    """
        Cette classe permet le téléchargement des données de consommation électrique de 2019 à  2022.

        :param urls: adresses urls du jeu de données

        :type urls: string

        :param target_name: chemins locaux où le jeu de données est enregistrer

        :type target_name: string
    """
    def __init__(self, url=urls, target_name=paths):
        """"
        Fonction d'initialisation 
        Elle permet le téléchargement des données au bon emplacement "./Data"

        """
        for i in range(5):
            path ,fname = os.path.split(paths[i])
            pooch.retrieve(urls[i], path=path, fname=fname, known_hash=None,)
    
def df_cleaning():
    """ Manipulation du jeu de données de 01/01/2019 jusqu'à 06/12/2022.
        Manipulations:
                     -Recupérer les colonnes **Date**,**Heure** et **Consommation (MW)**
                     -Supprimer les valeurs manquantes 
                     -Basculer la frequence des observations de **60 min** à **15 min**  
        :return: le jeu de données pour chaque 15 min 01/01/2019 jusqu'à 06/12/2022
        
        :rtype: Data frame 
    """
    data1 = pd.read_csv("./Data/data1.csv", sep=";")
    data1 = data1[['Date', 'Heure', 'Consommation (MW)']]
    time_improved = pd.to_datetime(data1['Date'] +
                                   ' ' + data1['Heure'],
                                   format='%Y-%m-%d %H:%M')
    data1['Temps'] = time_improved
    data1.set_index('Temps', inplace=True)
    del data1['Heure']
    del data1['Date']
    data1 = data1.sort_index(ascending=True)
    for nan in range(len(data1)-1):
        if data1[['Consommation (MW)']].isna().iloc[:, 0][nan]:
            data1['Consommation (MW)'][nan] = data1['Consommation (MW)'][nan-1:nan+1].mean()
    data1['Consommation (MW)'][len(
        data1)-1] = data1['Consommation (MW)'][-3:-2].mean()
    # -----------------------------------------------------------------------------------------
    data2 = pd.read_csv("./Data/data2.csv", sep=";")
    data2 = data2[['Date', 'Heure', 'Consommation (MW)']]
    data2['Temps'] = pd.to_datetime(data2['Date'] +
                                    ' ' + data2['Heure'],
                                    format='%Y-%m-%d %H:%M')
    data2.set_index('Temps', inplace=True)
    del data2['Heure']
    del data2['Date']
    data2 = data2.sort_index(ascending=True)
    for nan in range(len(data1)-1):
        if data1[['Consommation (MW)']].isna().iloc[:, 0][nan]:
            data1['Consommation (MW)'][nan] = data1['Consommation (MW)'][nan-1:nan+1].mean()
    data2['Consommation (MW)'][len(
        data1)-1] = data1['Consommation (MW)'][-3:-2].mean()
    # -----------------------------------------------------------------------------------------
    data3 = pd.read_csv("./Data/data3.csv", sep=";")
    data3 = data3[['Date', 'Heure', 'Consommation (MW)']]
    data3['Temps'] = pd.to_datetime(data3['Date'] +
                                    ' ' + data3['Heure'],
                                    format='%Y-%m-%d %H:%M')
    data3.set_index('Temps', inplace=True)
    del data3['Heure']
    del data3['Date']
    data3 = data3.sort_index(ascending=True)
    for nan in range(len(data1)-1):
        if data1[['Consommation (MW)']].isna().iloc[:, 0][nan]:
            data1['Consommation (MW)'][nan] = data1['Consommation (MW)'][nan-1:nan+1].mean()
    data3['Consommation (MW)'][len(
        data1)-1] = data1['Consommation (MW)'][-3:-2].mean()
    # -----------------------------------------------------------------------------------------
    data41 = pd.read_csv("./Data/data41.csv", sep=";")
    data41 = data41[['Date', 'Heure', 'Consommation (MW)']]
    data41['Temps'] = pd.to_datetime(data41['Date'] +
                                     ' ' + data41['Heure'],
                                     format='%Y-%m-%d %H:%M')
    data41.set_index('Temps', inplace=True)
    del data41['Heure']
    del data41['Date']
    data41 = data41.sort_index(ascending=True)
    for nan in range(len(data1)-1):
        if data1[['Consommation (MW)']].isna().iloc[:, 0][nan]:
            data1['Consommation (MW)'][nan] = data1['Consommation (MW)'][nan-1:nan+1].mean()
    data3['Consommation (MW)'][len(
        data1)-1] = data1['Consommation (MW)'][-3:-2].mean()
    # -----------------------------------------------------------------------------------------
    data42 = pd.read_csv("./Data/data42.csv", sep=";")
    #Data2022 = Data2022.set_index('Date et Heure')
    data42 = data42[['Date', 'Heure', 'Consommation (MW)']]
    data42['Temps'] = pd.to_datetime(data42['Date'] +
                                     ' ' + data42['Heure'],
                                     format='%Y-%m-%d %H:%M')
    data42.set_index('Temps', inplace=True)
    del data42['Heure']
    del data42['Date']
    data42 = data42.sort_index(ascending=True)
    data42 = data42.dropna()
    df = pd.concat([data1, data2, data3,
                    data41, data42], axis=0)
    #save as csv 
    return df
def df_cleaned(id):
    """" Récupere la dataframe préte à l'emploit directementt du package en assurant """
    if id==1:
        df=pd.read_csv("./Data/dattfinal.csv", sep=";") 
    if id==2:
        df=pd.read_csv("./Data/dattfinal_gaz.csv", sep=";") 
    if id==3:
        df=pd.read_csv("./Data/dattfinal_nucleaire.csv", sep=";")     
    return df
