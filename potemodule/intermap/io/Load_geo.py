import os
import pooch
import geopandas as gpd
from potemodule.intermap.io import url_geo, path_target_geo


class Load_geo:
    """
    Téléchargement du fichier au format json décvrivant les contours des départements français.
    """

    def __init__(self, url=url_geo, target_name=path_target_geo):
        """
        Téléchargement.

        Paramètres :

        - url : (string) adresse url du jeu de données

        - target_name : (string) chemin local où le jeu de données est enregistrer
        """
        path, fname = os.path.split(path_target_geo)
        pooch.retrieve(url, path=path, fname=fname, known_hash=None)

    @staticmethod
    def save_as_df():
        """
        Import des données géographique dans un dataframe.
        """
        df_geo = gpd.read_file(path_target_geo)

        return (df_geo)
