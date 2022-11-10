Super Projet

10/11/2022

- Modification de "Filtration.py" pour ajouter le Nombres de logements, la consommation annuelle moyenne par logement et la consommation annuelle moyenne de la communne au tableau traité pour les calculs de moyennes annuelles


09/10/22

-Ajout d'une branche pour traiter du tri du tableau. (Pandas)

-Passage de la fonction df.drop à .isin , permettant d'avoir une simple liste plutôt qu'une superposition de 25 "& ~".
Mais surtout permet de chercher les villes sans problème de casse. (Sur un petit exemple de Aix-En-Provence, on passe de 3846 résultats à 5040 et 368025 à 513073 pour le tableau complet. Le traitement semble aussi être plus rapide.)

Il semblerait qu'une colonne se rajoute à la première place, pour indiquer l'ancienne ligne de chaque ligne. (Ex: la première était à la 857ème place avant.)

-Suppression de l'expression Regex qui ne sera surement pas utile au final.

Pour des raisons inconnues, Grenoble et Strasbourg n'ont aucune données dans le site. On va donc les ignorer.

Garde-t-on toutes les colonnes?
Serait-il plus simple de séparer chaque ville dans un tableau distinct?

-Bon, pour les colonnes, je ne sais pas lesquelles garder exactement, mais je sais lesquelles vont sauter à coup sûr: Code IRIS ; Nom IRIS ; Numéro de voie ; Indice de répétition ; Type de voie ; Libellé de voie ; Code INSEE de la commune ; Segment de Client ; Adresse ; Tri des adresses

Plutôt qu'une liste de mot, je vais directement les enlever avec leur abscisses, soit les colonnes 1, 2, 3, 4, 5, 6, 7, 9, 14 et 15.

Mieux vaut le faire avant la filtration des villes.

-Problème de colonne qui se rajoute résolu par index=False, il venait du df.to_csv qui rajoute un index.

-Pour calculer la consommation totale, on a la consommation totale de l'adresse ou la moyenne de la commune. Soit on ajoute toute les consommation totale par adresse de la commune, soit on compte le nombre de lignes de que chaque commune possède et on multiplie par la moyenne.

Les deux méthodes donnent des résultats suffisament différents pour ne pas être ignorer. Le plus élevé varit selon l'endroit. Cela provient surement de commune plus ou moins vide rattachées à la commune étudié qui tire la moyenne vers le haut ou le bas. C'est probablement mieux de faire juste avec la ville seule, sans la moyenne, mais à voir.

Je vais partir sur juste le total mais si besoin est: len(df.axes[0])

-Le résultat final pour le moment est un "dictionnaire" avec chaque consommation annuelle de chaque ville noté par année. Certaines villes n'ont pas de consommation en 2018.

Je crois que la partie extraction des données est faite, il faut juste faire la carte, trouver comment télécharger le fichier, regrouper le tout et le tranformer en module téléchargeable avec un meilleur nom. La seconde partie ne sera pas trop compliqué, il faudra juste réutiliser le code "Filtration" et faire des écarts quadratiques en plus, pas la mer à boire je suppose.

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
