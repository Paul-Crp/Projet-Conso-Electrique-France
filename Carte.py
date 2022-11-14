import folium, branca
import pandas as pd

df = pd.read_csv('TableauTraité.csv')
df["Nom de la commune"]=df["Nom de la commune"].str.lower()

df1 = df.groupby(['Nom de la commune','Année'])[[df.columns[5]]].aggregate(lambda x: x.mean()).reset_index()

df2 = pd.DataFrame(df1.groupby(['Nom de la commune'])[[df1.columns[2]]].aggregate(lambda x : x.mean())).reset_index()

VILLES = ['Aix-en-Provence', "Angers", "Bordeaux", "Brest", "Clermont-Ferrand", "Dijon", "Le Havre", "Le Mans", "Lille", "Lyon", "Marseille", "Montpellier", "Nantes", "Nice", "Nîmes", "Paris", "Reims", "Rennes", "Saint-Denis", "Saint-Étienne", "Toulon", "Toulouse", "Villeurbanne"]

#Coordonnées des villes
LATS = [43.5297420, 47.4711616, 44.8377890,48.3903940,45.7772220,47.3220470,49.4943700,48.0061100,50.6292500,45.7640430,43.2964820,43.6107690,47.2183710,43.8366990,48.8566140,49.2583290,48.1172660,48.9361810,45.4396950,43.1242280,43.6046520,45.7719440]
LONGS = [5.4474270,-0.5518257, -0.5791800,-4.4860760,3.0870250,5.0414800,0.1079290,0.1995560,3.0572560,4.8356590,5.3697800, 3.8767160,-1.5536210,4.3600540,2.3522219,4.0316960,-1.6777926,2.3574430, 4.3871779,5.9280000, 1.4442090,4.8901709]

#Consommation éléctrique
CONSO = df2["Consommation annuelle moyenne de la commune (MWh)"]

#Création carte
fmap = folium.Map(location=[47, 2], tiles='OpenStreetMap', zoom_start=6)

cm = branca.colormap.LinearColormap(['blue','red'], vmin=min(CONSO), vmax=max(CONSO))
fmap.add_child(cm)

#Marqueurs
for lat, lng, color in zip(LATS, LONGS, CONSO) :
    folium.CircleMarker(
        location = [lat, lng],
        radius = 10,
        color = cm(color),
        fill = True,
        fill_color = cm(color),
        fill_opacity = 0.6
    ).add_to(fmap)

fmap.save('Carte.html')
fmap
