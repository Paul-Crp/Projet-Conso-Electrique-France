import folium, branca

VILLES = ['Aix-en-Provence', "Angers", "Bordeaux", "Brest", "Clermont-Ferrand", "Dijon", "Le Havre", "Le Mans", "Lille", "Lyon", "Marseille", "Montpellier", "Nantes", "Nice", "Nîmes", "Paris", "Reims", "Rennes", "Saint-Denis", "Saint-Étienne", "Toulon", "Toulouse", "Villeurbanne"]

#Coordonnées des villes
LATS = []
LONGS = []

#Consommation éléctrique
CONSO = []

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
