import os
import pandas as pd
import pooch
from Interactive_Map.io import url_db, path_target_db

class Load_db:
    """
    This class download the geographic data set

    Parameters :
    ---------------

    url : (string) path to the data set
    target_name : (string) local path where data is saved
    """
    def __init__(self, url=url_db, target_name=path_target_db):
        path, fname = os.path.split(path_target_db)
        pooch.retrieve(url, path=path, fname=fname, known_hash=None)

    @staticmethod
    def save_as_df():
        """
        A documentation
        
        .. code:: python
            >>> import biketrauma
            >>> Load_db.save_as_df()
        """
        
        df_db = pd.read_csv(
            path_target,
            na_values="",
            low_memory=False,
        )

        return df_db