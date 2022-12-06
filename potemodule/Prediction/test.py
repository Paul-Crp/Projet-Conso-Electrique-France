#%%
import data 
#%%
import PredictionModel
#%%
start1="2022-12-08 00:00:00"
end1="2022-12-08 23:45:00"
df=data.Processdf(1)  #
df.df_cleaned()

#%%
obj=PredictionModel.Model(debut=start1,fin=end1,df=df)
pred=obj.mod()
# %%
