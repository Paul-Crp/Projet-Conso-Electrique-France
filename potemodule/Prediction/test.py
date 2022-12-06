#%%
import data 
#%%
import PredictionModel
#%%
import pandas as pd 
start1="2022-12-08 00:00:00"
end1="2022-12-08 23:45:00"
df=data.Processdf(1)  #
df = df.df_cleaned()
df.set_index('Temps',inplace=True)
df.index=pd.to_datetime(df.index)
#%%
obj=PredictionModel.Model(debut=start1,fin=end1,pred=pd.DataFrame())
pred=obj.mod(df)
#%%
obj.ucmplot()
# %%
