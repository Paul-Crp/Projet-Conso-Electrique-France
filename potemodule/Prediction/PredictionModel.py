import warnings
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
class Model():
    """ 
    Cette classe crée la prediction à une date donnée ainsi que sa visualisation 

    :param debut: la date du debut de la prédiction 

    :type debut: Date dans le  format YYYY_MM_DD H:M:S

    :param fin: la date de la fin de la prédiction 
    
    :type fin: Date dans le  format YYYY_MM_DD H:M:S

    """
    def __init__(self,debut,fin):
        self.debut=debut
        self.debut=debut
    def df_cleaned(id):
    """Récupere la dataframe préte à l'emploit directementt du package en assurant """
    if id==1:
        df=pd.read_csv("./Data/dattfinal.csv", sep=";") 
    if id==2:
        df=pd.read_csv("./Data/dattfinal_gaz.csv", sep=";") 
    if id==3:
        df=pd.read_csv("./Data/dattfinal_nucleaire.csv", sep=";")     
    return df
    def mod(self):
        """" Le modele de prédiction sur une période donnnée 

        :return: la dataframe de la prédiction ,dates de la période donnée et les valeurs correspondantes     
        
        :rtype: Data frame 
        
        """
        df=df_cleaned()#pd.read_csv("./Data/datafinal.csv",sep=";")
        UCM = sm.tsa.UnobservedComponents(df,
                                            level='dtrend',
                                            irregular=True,
                                            stochastic_level=False,
                                            stochastic_trend=False,
                                            stochastic_freq_seasonal=[
                                                True, False, False],
                                            freq_seasonal=[{'period': 96, 'harmonics': 6},
                                                           {'period': 672,
                                                               'harmonics': 2},
                                                           {'period': 35066, 'harmonics': 1}])
        m=UCM.fit()
        pred=m.predect(start=self.debut,end=self.fin)
        pred = pred.to_frame()
        pred = pred - 5000
        return pred
     def ucmplot(pred):
        """" Visualisation de la consommation du jour à prédire

        :param pred: La prédiction d'une période donnée

        :type pred: data frame  
        """
        f, ax = plt.subplots(figsize=(18, 6), dpi=200)
        plt.suptitle('La consommation éléctrique  (MW) du 8 Décembre', fontsize=20)
        plt.ylabel('Consommation (MW) ')
        pred.plot(ax=ax, rot=90, ylabel='Consommation (MW)')
        plt.legend()




