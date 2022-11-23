import  pandas as pd
import numpy as np
from Interactive_Map.preprocess import url_conso

def get_conso(url_conso):
    """
    Cette fonction extrait du data set de consommation la consommation annuelle moyenne des foyers par ville

    Parameters :
    --------------
    df_conso : (dataframe) dat set contenant les consommations électriques par foyers
    log_scale : (boolean)
    """
    df_conso = pd.read_csv(url_conso, on_bad_lines='warn', sep=";")
    df_conso.drop(df.columns[[1, 2, 3, 4, 5, 6, 7, 9, 14, 15]], axis=1, inplace=True)
    df_conso.to_csv('../data/TableauTraité.csv', index=False)

    df_conso["Nom de la commune"]=df_conso["Nom de la commune"].str.lower()
    df1 = df_conso.groupby(['Nom de la commune','Année'])[[df_conso.columns[5]]].aggregate(lambda x: x.mean()).reset_index()
    df = pd.DataFrame(df1.groupby(['Nom de la commune'])[[df1.columns[2]]].aggregate(lambda x : x.mean())).reset_index()
    return df

def get_geo(df_geo):
    geo=df_geo.loc[:,('libgeo','geometry')]
    geo['libgeo']=geo['libgeo'].str.lower()
    return(geo)

def final_data(df_conso, df_geo):
    df_final = get_geo(df_geo).merge(get_conso(df_conso), left_on='libgeo', right_on='Nom de la commune',how='outer')
    df_final=df_final[~df_final['geometry'].isna()]
    df_final=df_final.dropna()
    return(df_final)
