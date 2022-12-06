import matplotlib.pyplot as plt
import mpld3                             # Pour transformer les graphiques en html
from matplotlib.pyplot import figure
import folium


class graphique:
    """
    Graphique de la consommation sur 4 ans à partir d'un dictionaire extraite de la base de données.

    :param k: kème ville de la liste.

    :type k: Integer

    :param d: Data contenant les données de consommation.

    :type d: Dictionnaire

    """


    def __init__(self,k):
        self.k = k

    def plotage(self,d):
        valeurs = []

        for p,v in d.items():
            valeurs = valeurs + [v]              #On récupère les valeurs de consommation. Les années étant toujours les mêmes et les villes dans le même ordre, on ne les récupère pas.

        fig=figure()
        for i in range(4*self.k,4*self.k+1):     #Par simplicité, les villes sans données pour 2018 ont quand même été conservées dans la liste des villes, mais avec une valeur de 0. On vérifie donc si la valeur est nulle ou non pour éviter de tracer un graphique avec une valeur de 0.
            if valeurs[i]==0:
                plt.plot([2019,2020,2021],  [valeurs[i+1],valeurs[i+2],valeurs[i+3] ], 'ks-', mec='w', mew=5, ms=20)
            else:
                plt.plot([2018,2019,2020,2021],  [valeurs[i],valeurs[i+1],valeurs[i+2],valeurs[i+3] ], 'ks-', mec='w', mew=5, ms=20)
        return(fig)



def Marker(Carte, k,d):

    """
    Création d'un marqueur incluant le graphique sur la carte pour la ville k.

    :param Carte: Carte.

    :type Carte: folium.map

    :param k: kème ville de la liste.

    :type k: Integer

    :param d: Data contenant les données de consommation.

    :type d: Dictionnaire

    """

    Coord=[43.53,5.45, 47.47,-0.56, 44.83,-0.34, 48.23,-4.49, 45.78,3.08, 47.32,5.04, 49.49,0.1, 48,0.2, 50.64,3.06, 45.76,4.83, 43.3,5.37, 43.61,3.88, 47.22,1.55, 43.7,7.27, 43.83,4.36, 48.86,2.35, 49.27,4.03, 48.11,-1.68, -20.87,55.44, 45.43,4.39, 43.12,5.93, 43.6,1.44, 45.77,4.88]
    #Coord est une liste contenant les coordonnées des villes dans l'ordre de la liste A.

    A=["Aix-en-Provence", "Angers", "Bordeaux",    "Brest", "Clermont-Ferrand", "Dijon", "Le Havre", "Le Mans", "Lille", "Lyon", "Marseille", "Montpellier", "Nantes", "Nice", "Nîmes",      "Paris",   "Reims",  "Rennes", "Saint-Denis", "Saint-Étienne", "Toulon", "Toulouse", "Villeurbanne"]
    b=graphique(k)                        #On crée un objet graphique pour la ville k.
    f=mpld3.fig_to_html(b.plotage(d))     #On plot et transforme le graphique en html.
    c='''</style><h1>'''+'''&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'''+A[k]+'''</h1>''' #On ajoute le nom de la ville au graphique en html.
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

    plt.close('all') #On ferme le graphique pour éviter de surcharger la mémoire.
    return(Carte)

#Cette fonction permet de créer un marqueur sur la carte avec le graphique correspondant à la ville k.