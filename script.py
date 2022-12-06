import potemodule.intermap as IM
import data,PredictionModel
import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs('Rendus', exist_ok=True)
print("Merci d'avoir choisi notre module!")
print("Si vous souhaitez la prédiction de consommation, veuillez entrer 1")
print("Si vous souhaitez la carte de consommation, veuillez entrer 2")
print("Si vous souhaitez les deux, veuillez entrer 3")
print("Si vous voulez quittez, veuillez entrer 4.")

val = input("Veuillez entrez votre choix: ")

if val == "1":
    print("Vous avez choisi la prédiction de consommation")
    print("Veuillez patienter...")
    start1 = "2022-12-08 00:00:00"
    end1 = "2022-12-08 23:45:00"
    print("Predction de la consommation du 8 Décembre et sa visualisation")
    df = data.Processdf(1)  
    df = df.df_cleaned()
    df.set_index('Temps',inplace=True)
    df.index = pd.to_datetime(df.index)
    obj = PredictionModel.Forcast(debut=start1,fin=end1,pred=pd.DataFrame(),1)
    pred = obj.ucm(df)
    obj.ucmplot()
    print("Predction du Gaz le 8 Décembre et sa visualisation")
    df = data.Processdf(2)  
    df = df.df_cleaned()
    df.set_index('Temps',inplace=True)
    df.index = pd.to_datetime(df.index)
    obj = PredictionModel.Forcast(debut=start1,fin=end1,pred=pd.DataFrame(),2)
    pred = obj.ucm(df)
    obj.ucmplot()

    pred.to_csv("Rendus/prediction.csv")
    plt.savefig("Rendus/Consommation.pdf")
    
    os.makedirs('Rendus', exist_ok=True)

elif val == "2":
    print("Vous avez choisi la carte de consommation")
    print("Veuillez patienter...")
    geo = IM.get_geo(IM.Load_geo().save_as_df())
    df = IM.final_data(IM.Load_db().save_as_df(), geo)

    d=IM.Filtrer()
    f=IM.legend(df, IM.carte(df, geo))

    os.makedirs('Rendus', exist_ok=True)
    print("C'est bientôt fini, merci de patienter encore un peu...")
    for i in range(0,23):
        f=IM.Marker(f,i,d)


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







# %%
