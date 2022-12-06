import matplotlib.pyplot as plt
import mpld3
from matplotlib.pyplot import figure
import folium
plt.rcParams.update({'figure.max_open_warning': 0})



# On crée deux listes : une pour les années et une pour les consommations.

class graphique:
    def __init__(self,k):
        self.k = k

    def plotage(self,d):
        valeurs = []

        for v in d.items():
            valeurs = valeurs + [v]

        fig=figure()
        for i in range(4*self.k,4*self.k+1):
            if valeurs[i]==0:
                plt.plot([2019,2020,2021],  [valeurs[i+1],valeurs[i+2],valeurs[i+3] ] )
            else:
                plt.plot([2018,2019,2020,2021],  [valeurs[i],valeurs[i+1],valeurs[i+2],valeurs[i+3] ] )
        return(fig)



def Marker(Carte, k,d):
    Coord=[43.53,5.45, 47.47,-0.56, 44.83,-0.34, 48.23,-4.49, 45.78,3.08, 47.32,5.04, 49.49,0.1, 48,0.2, 50.64,3.06, 45.76,4.83, 43.3,5.37, 43.61,3.88, 47.22,1.55, 43.7,7.27, 43.83,4.36, 48.86,2.35, 49.27,4.03, 48.11,-1.68, -20.87,55.44, 45.43,4.39, 43.12,5.93, 43.6,1.44, 45.77,4.88]
    A=["Aix-en-Provence", "Angers", "Bordeaux",    "Brest", "Clermont-Ferrand", "Dijon", "Le Havre", "Le Mans", "Lille", "Lyon", "Marseille", "Montpellier", "Nantes", "Nice", "Nîmes",      "Paris",   "Reims",  "Rennes", "Saint-Denis", "Saint-Étienne", "Toulon", "Toulouse", "Villeurbanne"]
    b=graphique(k)
    f=mpld3.fig_to_html(b.plotage(d))
    c='''</style><h1>'''+A[k]+'''</h1>'''
    elements = f.split("</style>")
    f = elements[0] + c + elements[1]
    folium.Marker(
        location=[Coord[2*k],Coord[2*k+1]],
        popup=folium.Popup(
            folium.IFrame(
                html=f,
                width=600,
                height=550),
                max_width=700)).add_to(Carte)
    return(Carte)

# # On crée une classe graphique qui prend en paramètre un entier k, qui correspond à la ville choisie.
# # La méthode graphique permet de créer le graphique de la consommation d'électricité de la ville choisie.