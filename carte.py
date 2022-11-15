

import folium
import json
import requests
import pandas as pd
import os

#Partitionner la carte en départements
#Le geojson représente les coordonnées de nos départements.
geojson_url = 'https://france-geojson.gregoiredavid.fr/repo/departements.geojson'
response = requests.get(geojson_url)
geojson = response.json()
#geojson



#Création d'un dictionnaire
#state_id_map = {}
#for feature in geojson['features']:
#   feature['id'] = feature['properties']['code']
#    state_id_map[feature['properties']['nom']] = feature['id']
    
#state_id_map




print(os.getcwd())


#Tableau du jeu de donnée (filtré) qu'on veut afficher sur la carte 
df = pd.read_csv('TableauTraité.csv')
df.head()

#df['Année'].min(), df['Année'].max()



#on définit l'indicateur de la carte 
indicateur = 'Consommation annuelle moyenne de la commune'
data = df[df['Consommation annuelle moyenne de la commune (MWh)'] == indicateur]
data.head()



#Définir un objet, ici notre cartet avec les coordinnées de la France
M = folium.Map(location=[46.232192999999995,2.209666999999996], zoom_start=15)
M




#Création de la carte partionner en région
folium.Choropleth( 
    geo_data=geojson, 
    data=df, 
    colums= ['Consommation annuelle moyenne par logement de ladresse (MWh)' , 'Nom de la commune'] , 
    key_one='feature.id', 
    fill_color='YlGnBu', 
    fill_opacity=0.7, 
    line_opacity=0.2, 
    legend_name=indicateur).add_to(M)


#Ajouter des marqueurs:
#Par exemple pour marquer les villes choisies 
folium.Marker(localisationMontpellier=[43.608292,3.879600], 
              popup="<stong>Montpellier</stong>").add_to(M)
folium.Marker(localisationParis=[48.856613,2.352222], popup="<stong>Paris</stong>").add_to(M)


#sauvegarder le tout dans un fichier html
M.save('carte.html')
