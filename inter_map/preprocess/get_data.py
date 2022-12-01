import  pandas as pd
import numpy as np
from inter_map.preprocess import Villes

def tri(df_conso):
    """
    Cette fonction tri les données du data set pour ne conserve qu'une ville par département.

    Paramètres :
    -------------
    df_conso : (dataframe) dataset contenant les consommation électrique par foyers
    """

    df_conso.drop(df_conso.columns[[1, 2, 3, 4, 5, 6, 9, 14, 15]], axis=1, inplace=True)
    
    Dept=[]
    for i in df_conso['Code INSEE de la commune']:
        i=int(i/1000)
        if i<10:
            Dept.append(f'{i}'.zfill(2))
        else:
            Dept.append(f'{i}')

    df_conso.insert(1,'Département', Dept)
    df_conso.drop('Code INSEE de la commune', axis=1, inplace=True)
    
    df_conso["Nom de la commune"] = df_conso["Nom de la commune"].str.lower()
    df=pd.DataFrame()
    for i in Villes:
        df1 = df_conso[df_conso['Nom de la commune']==i]
        df = pd.concat([df,df1],ignore_index=True)

    df.to_csv('inter_map/data/TableauTraité.csv', index=False)
    
    return(df)

def get_conso(df_conso):
    """
    Cette fonction extrait du data set de consommation la consommation annuelle moyenne des foyers par ville

    Parameters :
    --------------
    df_conso : (dataframe) dat set contenant les consommations électriques par foyers
    """
    df = tri(df_conso)

    df = df.groupby(['Département','Nom de la commune','Année'])[[df.columns[6]]].aggregate(lambda x: x.max()).reset_index()
    df = df.groupby(['Département','Nom de la commune'])[[df.columns[3]]].aggregate(lambda x : x.mean())).reset_index()
    
    return df

def get_geo(df_geo):
    geo=df_geo.loc[:,('code','nom','geometry')]
    
    return(geo)

def final_data(df_conso, df_geo):
    df_final = get_geo(df_geo).merge(get_conso(df_conso), left_on='conde', right_on='Département',how='outer')
    df_final=df_final[~df_final['geometry'].isna()]
    df_final=df_final.dropna()
    
    return(df_final)
