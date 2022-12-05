import os
import pandas as pd
import pooch
from potemodule.intermap.io import url_db, path_target_db


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
        pooch.retrieve(url, path=path, fname=fname, known_hash=None)
        print("Merci de patienter le téléchargement des données est en cours.\n",
                "Cette action peut prendre plusieurs minutes.")

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
