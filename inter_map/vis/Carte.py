import folium, branca

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
