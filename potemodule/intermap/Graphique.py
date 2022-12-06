import matplotlib.pyplot as plt
import mpld3                                          # Pour tranfirmer les graphiques en html
from matplotlib.pyplot import figure
import folium
plt.rcParams.update({'figure.max_open_warning': 0})   # Pour éviter le warning de trop de figures ouvertes.


class graphique:
    def __init__(self,k):
        self.k = k

    def plotage(self,d):
        valeurs = []

        for p,v in d.items():
            valeurs = valeurs + [v]              #On récupère les valeurs de consommation. Les années étant toujours les mêmes et les villes dans le même ordre, on ne les récupère pas.

        fig=figure()
        for i in range(4*self.k,4*self.k+1):     #Par simplicité, les villes sans données pour 2018 ont quand même été conservées dans la liste des villes, mais avec une valeur de 0. On vérifie donc si la valeur est nulle ou non pour éviter de tracer un graphique avec une valeur de 0.
            if valeurs[i]==0:
                plt.plot([2019,2020,2021],  [valeurs[i+1],valeurs[i+2],valeurs[i+3] ] )
            else:
                plt.plot([2018,2019,2020,2021],  [valeurs[i],valeurs[i+1],valeurs[i+2],valeurs[i+3] ] )
        return(fig)



def Marker(Carte, k,d):
    Coord=[43.53,5.45, 47.47,-0.56, 44.83,-0.34, 48.23,-4.49, 45.78,3.08, 47.32,5.04, 49.49,0.1, 48,0.2, 50.64,3.06, 45.76,4.83, 43.3,5.37, 43.61,3.88, 47.22,1.55, 43.7,7.27, 43.83,4.36, 48.86,2.35, 49.27,4.03, 48.11,-1.68, -20.87,55.44, 45.43,4.39, 43.12,5.93, 43.6,1.44, 45.77,4.88]
    #Coord est une liste contenant les coordonnées des villes dans l'ordre de la liste A.

    A=["Aix-en-Provence", "Angers", "Bordeaux",    "Brest", "Clermont-Ferrand", "Dijon", "Le Havre", "Le Mans", "Lille", "Lyon", "Marseille", "Montpellier", "Nantes", "Nice", "Nîmes",      "Paris",   "Reims",  "Rennes", "Saint-Denis", "Saint-Étienne", "Toulon", "Toulouse", "Villeurbanne"]
    b=graphique(k)                        #On crée un objet graphique pour la ville k.
    f=mpld3.fig_to_html(b.plotage(d))     #On plot et transforme le graphique en html.
    c='''</style><h1>'''+A[k]+'''</h1>''' #On ajoute le nom de la ville au graphique en html.
    elements = f.split("</style>")
    f = elements[0] + c + elements[1]
    folium.Marker( 
        location=[Coord[2*k],Coord[2*k+1]],
        popup=folium.Popup(
            folium.IFrame(
                html=f,
                width=600,
                height=550),
                max_width=700)).add_to(Carte) #On ajoute le marqueur à la carte.
    return(Carte)

#Cette fonction permet de créer un marqueur sur la carte avec le graphique correspondant à la ville k.