

import folium
import json
import requests
import pandas as pd
import os
import geopandas as gpd

#Partitionner la carte en communes
#Le geojson représente les coordonnées de nos communes.
geojson_url = 'https://www.data.gouv.fr/fr/datasets/r/fb3580f6-e875-408d-809a-ad22fc418581'
response = requests.get(geojson_url)
geojson = response.json()



#Tableau du jeu de donnée (filtré) qu'on veut afficher sur la carte 
df = pd.read_csv('TableauTraité.csv')
df.head()

#df['Année'].min(), df['Année'].max()


df["Nom de la commune"]=df["Nom de la commune"].str.lower()

df1 = df.groupby(['Nom de la commune','Année'])[[df.columns[5]]].aggregate(lambda x: x.mean()).reset_index()
df2 = pd.DataFrame(df1.groupby(['Nom de la commune'])[[df1.columns[2]]].aggregate(lambda x : x.mean())).reset_index()
df_final = df2.dropna()


#Création carte de la France
M = folium.Map(location=[46.232192999999995,2.209666999999996], zoom_start=15)
M



#Création de la carte partionner en communes
folium.Choropleth( 
    geo_data=geojson, 
    df=map_df, 
    colums=['Nom de la commune', 'Consommation annuelle moyenne de la commune (MWh)'] , 
    key_one='feature.id', 
    fill_color='YlGnBu', 
    fill_opacity=0.7, 
    line_opacity=0.2, 
).add_to(M)




#ajouter les fonctionnalités d'intércation
folium.features.GeoJson(
    data=df_final,
    style_function= style_function, 
    control=False,
    highlight_function=lambda x: {'weight': 3, 'fillColor': 'grey'}, 
    tooltip=folium.features.GeoJsonTooltip(
    fields=['Nom de la commune','Consommation annuelle moyenne de la commune (MWh)'],
    aliases=['Ville: ','Consommation annuelle moyenne (MWh): '],
    style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;"),
    localize=True,
    sticky=True,
    labels=True,
            )
).add_to(M)




#sauvegarder le tout dans un fichier html
M.save('carte.html')
