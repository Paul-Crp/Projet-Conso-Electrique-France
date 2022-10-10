import folium

# Création d'une carte
fmap = folium.Map(location=[47, 2], tiles='OpenStreetMap', zoom_start=6)

#display(fmap)

# Ajout d'un marqueur
#folium.Marker([55.8716693, 9.8839912],
#              popup='VIA University College',
#              icon=folium.Icon(color='green')).add_to(fmap)


# Ajout d'une ligne brisée définie à partir de 5 points
#points = [
#  (55.6713808, 12.4533972),
#  (55.4013094, 11.2062387),
#  (55.3311408, 10.6322608),
#  (55.7148992, 9.3734841),
#  (55.8716693, 9.8839912)
#]

#folium.PolyLine(points, color='blue', weight=2.5, opacity=0.8).add_to(fmap)

# Génération du fichier HTML contenant la carte
fmap.save('via.html')