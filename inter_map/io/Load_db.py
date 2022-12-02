import os
import pandas as pd
import pooch
from inter_map.io import url_db, path_target_db

class Load_db:
    """
    Cette classe permet le téléchargement des données de consommation électrique par foyers de 2018 à 2021.

    Paramètres :
    ---------------

    url : (string) adresse url du jeu de données
    target_name : (string) chemin local où le jeu de données est enregistrer
    """
    def __init__(self, url=url_db, target_name=path_target_db):
        path, fname = os.path.split(path_target_db)
        pooch.retrieve(url, path=path, fname=fname, known_hash=None)

    @staticmethod
    def save_as_df():
        """
        Téléchargement des données dans un dataframe avec le module pandas.
        """
        
        df_db = pd.read_csv(
            path_target,
            na_values="",
            low_memory=False,
            sep=";"
        )

        return df_db
