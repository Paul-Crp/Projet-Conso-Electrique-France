import os
import pandas as pd
import pooch
import geopandas as gpd
from inter_map.io import url_geo, path_target_geo

class Load_geo:
    """
    This class download the geographic data set

    Parameters :
    ---------------

    url : (string) path to the data set
    target_name : (string) local path where data is saved
    """
    def __init__(self, url=url_geo, target_name=path_target_geo):
        path, fname = os.path.split(path_target_geo)
        pooch.retrieve(url, path=path, fname=fname, known_hash=None)

    @staticmethod
    def save_as_df():
        """
        A documentation
        
        .. code:: python
            >>> import inter_map
            >>> Load_geo.save_as_df()
        """
        df_geo=gpd.read_file(path_target_geo)

        return df_geo
