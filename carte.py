

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





map_df = df[['Nom de la commune', 'Consommation annuelle moyenne de la commune (MWh)']]
map_df.head()



#Définir un objet, ici notre cartet avec les coordinnées de la France
M = folium.Map(location=[46.232192999999995,2.209666999999996], zoom_start=15)
M




#Création de la carte partionner en région
folium.Choropleth( 
    geo_data=geojson, 
    df=map_df, 
    colums=['Nom de la commune', 'Consommation annuelle moyenne de la commune (MWh)'] , 
    key_one='feature.id', 
    fill_color='YlGnBu', 
    fill_opacity=0.7, 
    line_opacity=0.2, 
).add_to(M)







#Ajouter des marqueurs:
#Par exemple pour marquer les villes choisies 
folium.Marker(localisationMontpellier=[43.608292,3.879600], 
              popup="<stong>Montpellier</stong>").add_to(M)
folium.Marker(localisationParis=[48.856613,2.352222], popup="<stong>Paris</stong>").add_to(M)


#sauvegarder le tout dans un fichier html
M.save('carte.html')
