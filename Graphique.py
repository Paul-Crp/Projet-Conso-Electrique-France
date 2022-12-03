import matplotlib.pyplot as plt

d={'Total-Aix-en-Provence2018': 93228.182, 'Total-Aix-en-Provence2019': 98952.252, 'Total-Aix-en-Provence2020': 109801.538, 'Total-Aix-en-Provence2021': 100121.393, 'Total-Angers2018': 103899.182, 'Total-Angers2019': 103658.135, 'Total-Angers2020': 102867.719, 'Total-Angers2021': 106931.844, 'Total-Bordeaux2018': 177061.352, 'Total-Bordeaux2019': 170608.26, 'Total-Bordeaux2020': 171213.726, 'Total-Bordeaux2021': 170698.699, 'Total-Brest2018': 72499.392, 'Total-Brest2019': 70752.45, 'Total-Brest2020': 70567.448, 'Total-Brest2021': 73195.642, 'Total-Clermont-Ferrand2018': 96237.593, 'Total-Clermont-Ferrand2019': 95400.754, 'Total-Clermont-Ferrand2020': 95024.763, 'Total-Clermont-Ferrand2021': 97129.53, 'Total-Dijon2018': 123659.549, 'Total-Dijon2019': 125649.636, 'Total-Dijon2020': 127386.067, 'Total-Dijon2021': 133838.298, 'Total-Le Havre2018': 0.0, 'Total-Le Havre2019': 91211.677, 'Total-Le Havre2020': 93539.886, 'Total-Le Havre2021': 91336.741, 'Total-Le Mans2018': 0.0, 'Total-Le Mans2019': 71744.059, 'Total-Le Mans2020': 73280.61, 'Total-Le Mans2021': 74773.211, 'Total-Lille2018': 180185.222, 'Total-Lille2019': 176068.886, 'Total-Lille2020': 176050.618, 'Total-Lille2021': 174688.706, 'Total-Lyon2018': 729971.421, 'Total-Lyon2019': 727687.63, 'Total-Lyon2020': 730295.0, 'Total-Lyon2021': 757451.467, 'Total-Marseille2018': 763693.857, 'Total-Marseille2019': 770666.223, 'Total-Marseille2020': 791437.353, 'Total-Marseille2021': 810800.766, 'Total-Montpellier2018': 275626.693, 'Total-Montpellier2019': 275111.754, 'Total-Montpellier2020': 281156.621, 'Total-Montpellier2021': 280508.721, 'Total-Nantes2018': 260473.448, 'Total-Nantes2019': 264162.564, 'Total-Nantes2020': 260616.834, 'Total-Nantes2021': 263596.436, 'Total-Nice2018': 534235.065, 'Total-Nice2019': 542065.315, 'Total-Nice2020': 541272.738, 'Total-Nice2021': 527234.572, 'Total-Nîmes2018': 0.0, 'Total-Nîmes2019': 87477.113, 'Total-Nîmes2020': 90761.739, 'Total-Nîmes2021': 92447.773, 'Total-Paris2018': 3701763.491, 'Total-Paris2019': 3594081.194, 'Total-Paris2020': 3620908.748, 'Total-Paris2021': 3648864.492, 'Total-Reims2018': 116429.253, 'Total-Reims2019': 118159.23, 'Total-Reims2020': 118393.078, 'Total-Reims2021': 123094.336, 'Total-Rennes2018': 156216.844, 'Total-Rennes2019': 156424.596, 'Total-Rennes2020': 159149.711, 'Total-Rennes2021': 158780.152, 'Total-Saint-Denis2018': 104662.477, 'Total-Saint-Denis2019': 107112.861, 'Total-Saint-Denis2020': 108704.0, 'Total-Saint-Denis2021': 107121.457, 'Total-Saint-Étienne2018': 0.0, 'Total-Saint-Étienne2019': 105023.661, 'Total-Saint-Étienne2020': 108172.572, 'Total-Saint-Étienne2021': 106771.311, 'Total-Toulon2018': 102394.537, 'Total-Toulon2019': 102936.779, 'Total-Toulon2020': 114762.627, 'Total-Toulon2021': 102540.744, 'Total-Toulouse2018': 524566.453, 'Total-Toulouse2019': 522317.427, 'Total-Toulouse2020': 519559.0, 'Total-Toulouse2021': 529209.582, 'Total-Villeurbanne2018': 183007.35, 'Total-Villeurbanne2019': 181716.828, 'Total-Villeurbanne2020': 185907.198, 'Total-Villeurbanne2021': 184715.95}

# Ce dictionnaire contient les données de la consommation d'électricité par ville et par année. Il sera utilisé pour créer le graphique. 
# Il sera produit par la filtration du tableau mais pour l'instant, il est créé manuellement.

année = []
valeurs = []

for k,v in d.items():
    année = année + [k]
    valeurs = valeurs + [v]

# On crée deux listes : une pour les années et une pour les consommations.

class graphique:
    def __init__(self,k):
        self.k = k

    def graphique(self):
        for i in range(4*self.k,4*self.k+1):
            plt.plot([année[i],année[i+1],année[i+2],année[i+3]], [valeurs[i],valeurs[i+1],valeurs[i+2],valeurs[i+3]])
        plt.show()

# On crée une classe graphique qui prend en paramètre un entier k, qui correspond à la ville choisie.
# La méthode graphique permet de créer le graphique de la consommation d'électricité de la ville choisie.

p0 = graphique(0)

p1 = graphique(1)

p0.graphique()

p1.graphique()

p0.graphique()