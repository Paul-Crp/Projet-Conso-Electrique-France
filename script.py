import potemodule.intermap as IM
import os

print("Merci d'avoir choisi notre module!")
print("Si vous souhaitez la prédiction de consommation, veuillez entrer 1")
print("Si vous souhaitez la carte de consommation, veuillez entrer 2")
print("Si vous souhaitez les deux, veuillez entrer 3")
print("Si vous voulez quittez, veuillez entrer 4.")

val = input("Veuillez entrez votre choix: ")

if val == "1":
    print("Vous avez choisi la prédiction de consommation")
    print("Veuillez patienter...")
    # RAJOUTEZ LA FONCTION DE PRÉDICTION ICI

elif val == "2":
    print("Vous avez choisi la carte de consommation")
    print("Veuillez patienter...")
    geo = IM.get_geo(IM.Load_geo().save_as_df())
    df = IM.final_data(IM.Load_db().save_as_df(), geo)

    d=IM.Filtrer()
    f=IM.legend(df, IM.carte(df, geo))

    os.makedirs('Rendus', exist_ok=True)
    for i in range(0,23):
        f=IM.Marker(f,i,d)
        if i == 0:
            print("C'est bientôt fini, merci de patienter encore un peu...")


    f.save('Rendus/Carte.html')
    print("Votre carte se situe dans le dossier Rendus sous le nom de Carte.html.")
    print("Vous pouvez la visualiser en ouvrant le fichier avec votre navigateur préféré.")
    print("Merci pour votre confiance, à bientôt!")

elif val == "3":
    print("Vous avez choisi les deux")
    print("Veuillez patienter...")
    # RAJOUTEZ LES DEUX FONCTIONS ICI

elif val == "4":
    print("Merci d'avoir utilisé notre module!")
    exit()

else:
    print("Veuillez entrer un choix valide la prochaine fois ^^")
    exit()