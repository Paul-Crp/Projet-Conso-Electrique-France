<h1>*Projet :Consommation de l'éléctricité en France*</h1>
 
 
 <h2>*Membres du groupe:*</h2>
 
 Thamara Renoir thamara.renoir@etu.umontpellier.fr
 
 Oualid Lamrini oualid.lamrini@etu.umontpellier.fr
 
 Emma Sinibaldi emma.sinibaldi@etu.umontpellier.fr
 
 Paul Crespin: paul.crespin@etu.umontpellier.fr


<h2>*Composition du projet*</h2>

Notre projet se scinde en deux grandes parties :

Partie visualisation:Consiste à visualiser la consommation d'éléctricité moyenne(sur 4 ans) en france par ville  et ce sous forme d'une carte interactive (qulicable).

Partie prédiction:Consiste à trouver le  modéle mathématique aproprié pour nos données (données temporelles ) ainsi que quelques visualisations dynamiques afin de présenter les résultats sous une forme plus intuitive et plus informative.

<h2>*Affectation des taches:*</h2>

*Crespin:* Partie visualisation.

*Thamara:* Partie visualisation

*Emma:* Partie visualisation.

*Oualid:* Partie prédiction,créer le modele + visualiser les résultats (prédiction d'éléctricité du 08/12/2022 en format *.csv et sous forme de graphiques) 

<h2>*Avancement*</h2>

09/10/22

Ajout d'une branche pour traiter du tri du tableau. (Pandas)

06/10/22

La définition de métropole étant assez restrictive et n'incluant pas une ville comme Lyon, on basculera surement sur les villes les peuplés de France. Soit les 25 premières de façon arbitraires, ou de plus de 100.000 habitants.

03/10/22

Trouver un module python pour traiter des tableaux en .csv .

à faire: trouver aussi un moyen de télécharger les données, si possible en filtrant directement? Mettre en cache pour éviter le téléchargement à chaque fois?

Visualisation:

Notre premier objectif est de trouver comment traiter les données qui nous sont fournis par le site et de le réduire (1.600.000 lignes pour le moment.)

Nous nous sommes fixés pour le moment l'objectif de faire toutes les métroples de France, soit 21 villes, ce qui rendra l'exploitation du tableau plus facile et rendra la carte plus lisible.

Nous allons à priori filtrer avec la colonne "Nom de la commune", ce qui devrait réduire le tableau à 200.000 lignes environ.

Trouver un module python pour afficher une carte + interaction?

Prévision:

Faire un premier jet avec seulement les moyennes pour chaque 1/4 h disponible.
La consommation ne varit pas entre Juillet et Octobre.

Trouver un module Python pour faire des graphes.

12/11/22

créer un modéle mathématique pour prédir la consommation en france chaque 15 min (1/4h) en se basant sur notre base de données qui sera vu comme une série temporelle (une fonction du temps)


