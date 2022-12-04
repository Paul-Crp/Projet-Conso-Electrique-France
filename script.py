import intermap as IM
import pandas as pd

geo = IM.get_geo(IM.Load_geo().save_as_df())
df = IM.final_data(IM.Load_db().save_as_df(), geo)

IM.legend(df, IM.carte(df, geo)).save('Carte.html')
