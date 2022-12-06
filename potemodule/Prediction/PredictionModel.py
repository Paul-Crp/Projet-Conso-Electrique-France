#%%
import warnings
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set()

class Forcast():
    """ 
    Cette classe crée la prediction à une date donnée ainsi que sa visualisation 

    :param debut: la date du debut de la prédiction 

    :type debut: Date dans le  format YYYY_MM_DD H:M:S

    :param fin: la date de la fin de la prédiction 
    
    :type fin: Date dans le  format YYYY_MM_DD H:M:S

    :param pred: La prediction retenu par la méthode *ucm*

    :type pred: Dataframe

    :param id: vaut 1 si la prediction porte sur la consommation\\
                et vaut 2 si elle porte sur le Gaz .
    :type id: Entier            
                 

    """
    def __init__(self,debut,fin,pred,id):
        self.debut=debut
        self.fin=fin
        self.pred=pred
        self.id=id

    def ucm(self,df):
        """ 
        Le modele de prédiction sur une période donnnée 

        :return: la dataframe de la prédiction ,dates de la période donnée et les valeurs correspondantes     
        
        :rtype: Data frame 
        
        """

        
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
        self.pred=m.predict(start=self.debut,end=self.fin)
        self.pred = self.pred.to_frame()
        self.pred = self.pred - 5000
        return self.pred
    def ucmplot(self):
        """ 
        Visualisation de la consommation du jour à prédire

        :param pred: La prédiction d'une période donnée

        :type pred: data frame  
        """
        if (self.id==1):
            f, ax = plt.subplots(figsize=(18, 6), dpi=200)
            plt.suptitle('La prediction de la consommation éléctrique  (MW) du 8 Décembre', fontsize=20)
            plt.ylabel('Consommation (MW) ')
            self.pred.plot(ax=ax, rot=90, ylabel='Consommation (MW)')
            plt.legend()
        if (self.id==2):
            f, ax = plt.subplots(figsize=(18, 6), dpi=200)
            plt.suptitle('La prediction du Gaz (MW) du 8 Décembre', fontsize=20)
            plt.ylabel('Gaz (MW) ')
            self.pred.plot(ax=ax, rot=90, ylabel='Gaz (MW)')
            plt.legend()     
       
