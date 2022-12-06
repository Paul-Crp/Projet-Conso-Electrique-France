#%%
import warnings
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import statsmodels.api as sm
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
    def __init__(self,debut,fin,nbr):
        self.debut=debut
        self.fin=fin
        self.nbr=nbr
    def df_cleaned(self):
        """Récupere la dataframe préte à l'emploit directementt du package en assurant """
        if self.nbr==1:
            df=pd.read_csv("./Data/dattfinal.csv", sep=";") 
        #if id==2:
            #df=pd.read_csv("./Data/dattfinal_gaz.csv", sep=";") 
        #if id==3:
            #df=pd.read_csv("./Data/dattfinal_nucleaire.csv", sep=";")     
        return df
    def mod(self):
        """ 
        Le modele de prédiction sur une période donnnée 

        :return: la dataframe de la prédiction ,dates de la période donnée et les valeurs correspondantes     
        
        :rtype: Data frame 
        
        """

        df = pd.read_csv("./Data/datafinal.csv",sep=";")#df_cleaned(self)
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
    def ucmplot(predd):
        """ 
        Visualisation de la consommation du jour à prédire

        :param pred: La prédiction d'une période donnée

        :type pred: data frame  

        """
        f, ax = plt.subplots(figsize=(18, 6), dpi=200)
        plt.suptitle('La consommation éléctrique  (MW) du 8 Décembre', fontsize=20)
        plt.ylabel('Consommation (MW) ')
        predd.plot(ax=ax, rot=90, ylabel='Consommation (MW)')
        plt.legend()
        return
#%%
start="2022-12-08 00:00:00"
end="2022-12-08 23:45:00"
obj=Model(start,end,1)
pred=obj.mod()





# %%
