import folium, branca
import pandas as pd
import geopandas as gpd
import os

#Récupération des données pour créer la carte
df = pd.read_csv('TableauTraité.csv')
df["Nom de la commune"]=df["Nom de la commune"].str.lower()
df1 = df.groupby(['Nom de la commune','Année'])[[df.columns[5]]].aggregate(lambda x: x.mean()).reset_index()
df2 = pd.DataFrame(df1.groupby(['Nom de la commune'])[[df1.columns[2]]].aggregate(lambda x : x.mean())).reset_index()

#Récupération du fichier contenant les contours des communes
url = "https://static.data.gouv.fr/resources/contours-des-communes-de-france-simplifie-avec-regions-et-departement-doutre-mer-rapproches/20220219-095144/a-com2022.json"
path_target = "./commf2022.json"
path, fname = os.path.split(path_target)
pooch.retrieve(url, path=path, fname=fname, known_hash=None)

#On ne garde que les colonnes contenant les noms des communes et leurs contours
geo=gpd.read_file('commf2022.json') #ouverture lente
geo=geo[['libgeo','geometry']]
geo['libgeo']=geo['libgeo'].str.lower()

#Création du tableau de donnée final joint sur la base de 'libgeo' et 'Nom de la commune'
df_final = geo.merge(df2, left_on='libgeo', right_on='Nom de la commune',how='outer')
df_final=df_final[~df_final['geometry'].isna()]
df_final.dropna()

#Base de la carte
fmap = folium.Map(location=[47, 2], tiles='OpenStreetMap', zoom_start=6)

#Coloration de la carte
folium.Choropleth(
    geo_data=geo,
    data=df_final,
    columns=['Nom de la commune', 'Consommation annuelle moyenne de la commune (MWh)'],
    key_on='feature.properties.libgeo',
    fill_color='YlOrRd', 
    nan_fill_color='White',
    fill_opacity=0.7, 
    line_opacity=0.2,
    legend_name='Consommation éléctrique moyennne',
    highlight=True,
    line_color='black'
).add_to(fmap)

fmap.save('Carte2.html')

