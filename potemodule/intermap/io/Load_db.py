import os
import pandas as pd
import pooch
from potemodule.intermap.io import url_db, path_target_db
import tqdm

class Load_db:
    """
    Téléchargement des données de consommation électrique par foyers de 2018 à 2021 de plusieurs communnes de france.
    """

    def __init__(self, url=url_db, target_name=path_target_db):
        """
        Téléchargement.

        Paramètres :

        - url : (string) adresse url du jeu de données

        - target_name : (string) chemin local où le jeu de données est enregistrer
        """
        path, fname = os.path.split(path_target_db)
        if os.path.isfile('./potemodule/intermap/data/conso.csv'):
            print("La base de données existe déjà.")
        else:
            print("Téléchargement de la base de données, elle fait 209 Mb, ça risque de prendre un moment...")
            pooch.retrieve(url, path=path, fname=fname, known_hash=None, progressbar=True)

    @staticmethod
    def save_as_df():
        """
        Import des données dans un dataframe avec le module pandas.
        """

        df_db = pd.read_csv(
            path_target_db,
            na_values="",
            low_memory=False,
            sep=";"
        )

        return (df_db)
