import potemodule.intermap as IM
import os

geo = IM.get_geo(IM.Load_geo().save_as_df())
df = IM.final_data(IM.Load_db().save_as_df(), geo)

os.makedirs('Carte', exist_ok=True)
IM.legend(df, IM.carte(df, geo)).save('Carte/Carte.html')