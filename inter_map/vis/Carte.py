#%%
import folium, branca
# import pandas as pd
# import geopandas as gpd
# import os
# import pooch

#%%

# df = pd.read_csv('../data/TableauTraité.csv')
# df["Nom de la commune"]=df["Nom de la commune"].str.lower()

# df1 = df.groupby(['Nom de la commune','Année'])[[df.columns[5]]].aggregate(lambda x: x.mean()).reset_index()

# df2 = pd.DataFrame(df1.groupby(['Nom de la commune'])[[df1.columns[2]]].aggregate(lambda x : x.mean())).reset_index()

#%%

# url = "https://static.data.gouv.fr/resources/contours-des-communes-de-france-simplifie-avec-regions-et-departement-doutre-mer-rapproches/20220219-095144/a-com2022.json"
# path_target = "./commf2020.json"
# path, fname = os.path.split(path_target)
# pooch.retrieve(url, path=path, fname=fname, known_hash=None)

# geo=gpd.read_file('../data/commf2020.json')
# geo=geo[['libgeo','geometry']]
# geo['libgeo']=geo['libgeo'].str.lower()

#%%

# df_final = geo.merge(df2, left_on='libgeo', right_on='Nom de la commune',how='outer')
# df_final=df_final[~df_final['geometry'].isna()]
# df_final=df_final.dropna()

#%%

def carte(df_final, df_geo):
    fmap = folium.Map(location=[47, 2], tiles='OpenStreetMap', zoom_start=6)
    folium.Choropleth(
            geo_data=df_geo,
            data=df_final,
            columns=['Nom de la commune', 'Consommation annuelle moyenne de la commune (MWh)'],
            key_on='feature.properties.libgeo',
            fill_color='YlOrRd', 
            nan_fill_color='White',
            fill_opacity=0.7, 
            line_opacity=0.2,
            legend_name='Consommation éléctrique annuelle moyennne',
            highlight=True,
            line_color='black'
        ).add_to(fmap)
    return(fmap)
    

# %%
#Add Customized Tooltips to the map

def legend(df_final,fmap):
    folium.features.GeoJson(
                        data=df_final,
                        name='Consommation éléctrique annuelle moyenne',
                        smooth_factor=2,
                        style_function=lambda x: {'color':'black','fillColor':'transparent','weight':0.5},
                        tooltip=folium.features.GeoJsonTooltip(
                            fields=['Nom de la commune',
                                    'Consommation annuelle moyenne de la commune (MWh)',
                                    ],
                            aliases=["Ville :",
                                    "Consommation annuelle moyenne (en MWh):",
                                    ], 
                            localize=True,
                            sticky=False,
                            labels=True,
                            style="""
                                background-color: #F0EFEF;
                                border: 2px solid black;
                                border-radius: 3px;
                                box-shadow: 3px;
                                """,
                            max_width=800,),
                                highlight_function=lambda x: {'weight':3,'fillColor':'grey'},
                            ).add_to(fmap)   
    return(fmap)    
