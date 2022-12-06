    def cleaningdfresource(resource):
        """ 
        Manipulation du jeu de données de 01/01/2019 jusqu'à 06/12/2022.
        
        Manipulations:

                     -Recupérer les colonnes **Date**,**Heure** et **Consommation (MW)**
                     -Supprimer les valeurs manquantes 
                     -Basculer la frequence des observations de **60 min** à **15 min**  
        
        :return: le jeu de données pour chaque 15 min 01/01/2019 jusqu'à 06/12/2022
        
        :rtype: Data frame 
        """
        data1 = pd.read_csv("./Data/adata1.csv", sep=";")
        data1 = data1[['Date', 'Heure', resource]]
        time_improved = pd.to_datetime(data1['Date'] +
                                       ' ' + data1['Heure'],
                                       format='%Y-%m-%d %H:%M')
        data1['Temps'] = time_improved
        data1.set_index('Temps', inplace=True)
        del data1['Heure']
        del data1['Date']
        data1 = data1.sort_index(ascending=True)
        for nan in range(len(data1)-1):
            if data1[[resource]].isna().iloc[:, 0][nan]:
                data1[resource][nan] = data1[resource][nan-1:nan+1].mean()
        data1[resource][len(
            data1)-1] = data1[resource][-3:-2].mean()
        # -----------------------------------------------------------------------------------------
        data2 = pd.read_csv("./Data/adata2.csv", sep=";")
        data2 = data2[['Date', 'Heure', resource]]
        data2['Temps'] = pd.to_datetime(data2['Date'] +
                                        ' ' + data2['Heure'],
                                        format='%Y-%m-%d %H:%M')
        data2.set_index('Temps', inplace=True)
        del data2['Heure']
        del data2['Date']
        data2 = data2.sort_index(ascending=True)
        for nan in range(len(data1)-1):
            if data1[[resource]].isna().iloc[:, 0][nan]:
                data1[resource][nan] = data1[resource][nan-1:nan+1].mean()
        data2[resource][len(
            data1)-1] = data1[resource][-3:-2].mean()
        # -----------------------------------------------------------------------------------------
        data3 = pd.read_csv("./Data/adata3.csv", sep=";")
        data3 = data3[['Date', 'Heure', resource]]
        data3['Temps'] = pd.to_datetime(data3['Date'] +
                                        ' ' + data3['Heure'],
                                        format='%Y-%m-%d %H:%M')
        data3.set_index('Temps', inplace=True)
        del data3['Heure']
        del data3['Date']
        data3 = data3.sort_index(ascending=True)
        for nan in range(len(data1)-1):
            if data1[[resource]].isna().iloc[:, 0][nan]:
                data1[resource][nan] = data1[resource][nan-1:nan+1].mean()
        data3[resource][len(
            data1)-1] = data1[resource][-3:-2].mean()
        # -----------------------------------------------------------------------------------------
        data41 = pd.read_csv("./Data/adata41.csv", sep=";")
        data41 = data41[['Date', 'Heure', resource]]
        data41['Temps'] = pd.to_datetime(data41['Date'] +
                                         ' ' + data41['Heure'],
                                         format='%Y-%m-%d %H:%M')
        data41.set_index('Temps', inplace=True)
        del data41['Heure']
        del data41['Date']
        data41 = data41.sort_index(ascending=True)
        for nan in range(len(data1)-1):
            if data1[[resource]].isna().iloc[:, 0][nan]:
                data1[resource][nan] = data1[resource][nan-1:nan+1].mean()
        data3[resource][len(
            data1)-1] = data1[resource][-3:-2].mean()
        # -----------------------------------------------------------------------------------------
        data42 = pd.read_csv("./Data/adata42.csv", sep=";")
        #Data2022 = Data2022.set_index('Date et Heure')
        data42 = data42[['Date', 'Heure', resource]]
        data42['Temps'] = pd.to_datetime(data42['Date'] +
                                         ' ' + data42['Heure'],
                                         format='%Y-%m-%d %H:%M')
        data42.set_index('Temps', inplace=True)
        del data42['Heure']
        del data42['Date']
        data42 = data42.sort_index(ascending=True)
        data42 = data42.dropna()
        df = pd.concat([data1, data2, data3,
                        data41, data42], axis=0) 
        if resource = 'Gaz (MW)'
            df.to_csv("./Data/datafinalgaz.csv")
        if resource = 'Eiolien (MW)'  
        return df