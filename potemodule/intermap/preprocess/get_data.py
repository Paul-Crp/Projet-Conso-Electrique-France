import pandas as pd
import os
from potemodule.intermap.preprocess import Villes


def tri(df_conso):
    """
    Suppression des colonnes non nécessaire à la visualisation et ajout d'une colonne 'Département' contenant le numéro de département de chaque adresse.
    Tri des données pour conserve la ville la plus peuplée par département.

    :param df_conso: dataset contenant les consommation électrique par foyers

    :type df_conso: dataframe
    """

    df_conso.drop(
        df_conso.columns[[1, 2, 3, 4, 5, 6, 9, 10, 12, 14, 15]], axis=1, inplace=True)

    Dept = []
    for i in df_conso['Code INSEE de la commune']:
        i = int(i/1000)
        if i < 10:
            Dept.append(f'{i}'.zfill(2))
        else:
            Dept.append(f'{i}')

    df_conso.insert(1, 'Département', Dept)
    df_conso.drop('Code INSEE de la commune', axis=1, inplace=True)

    df_conso["Nom de la commune"] = df_conso["Nom de la commune"].str.lower()
    df = pd.DataFrame()
    for i in Villes:
        df1 = df_conso[df_conso['Nom de la commune'] == i]
        df = pd.concat([df, df1], ignore_index=True)

    df.to_csv(os.path.join(os.path.dirname(
        os.path.realpath(__file__)), "..", "data", "TableauTraité.csv"), index=False)

    return (df)


def get_conso(df_conso):
    """
    Extraction des données de consommation moyenne annuelle par habitant d'une ville par département triées.

    :param df_conso: jeu de données contenant les consommations électriques par foyers

    :type df_conso: dataframe
    """

    df = tri(df_conso)

    df = df.groupby(['Département', 'Nom de la commune', 'Année'])[
        [df.columns[4]]].aggregate(lambda x: x.max()).reset_index()
    df = df.groupby(['Département', 'Nom de la commune'])[
        [df.columns[3]]].aggregate(lambda x: x.mean()).reset_index()

    return (df)


def get_geo(df_geo):
    """
    Extraction des numéros, nom et contours des départements de France.

    :param df_geo: contours des départements français au format json

    :type df_geo: dataframe
    """

    geo = df_geo.loc[:, ('code', 'nom', 'geometry')]

    return (geo)


def final_data(df_conso, df_geo):
    """
    Fusion du dataframe des contours des départements français trié et du dataframe de la consommation électrique trié.

    :param df_conso: données de consommation triées

    :type df_conso: dataframe

    :param df_geo: contours des départements français trié

    :type df_geo: dataframe
    """

    df_final = get_geo(df_geo).merge(get_conso(df_conso),
                                     left_on='code', right_on='Département', how='outer')
    df_final = df_final[~df_final['geometry'].isna()]
    df_final = df_final.dropna()

    return (df_final)
