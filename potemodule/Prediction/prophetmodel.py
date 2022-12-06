
from statsmodels.tools.eval_measures import rmse
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

from prophet import Prophet
#from Prediction import data
import pandas as dp 

#clss Conso:
# preprocessing  data
class modele:
    def __init__(self) -> None:
        pass
    
    def modeele():
        df = pd.red_csv(".data/datafinal.csv")
        dff = df.reset_index()
        dff.rename(columns={'Consommation (MW)': 'y', '': 'ds'}, inplace=True)
        plt.plot(dff['y'], label='Consommation (MW)')
        plt.grid()
        plt.legend()
        # training data
        train, test = train_test_split(dff, test_size=0.20, shuffle=False)
        m = Prophet()
        # m=Prophet(changepoint_prior_scale=0.01).fit(train)
        future = m.fit(train).make_future_dataframe(periods=len(test), freq='15T')
        forcast = m.predict(future)
        # Visualisation
        forcast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(10)
        fig = m.plot_components(forcast)
        fig2 = m.plot(forcast.iloc[-97:-1, :])
        predictions = forcast.iloc[-len(test):]['yhat'] - 20000
        err = rmse(predictions, test['y'])
        moy = test['y'].mean()
        print('Erreure quadrartique moyenne entre :', err)
        print('Moyenne du test : ', moy)
        print('Erreur retaltive :', err/moy)
        #clss Resouces:
        #def # charbon 
        #def #
###################################################################################
#_____________________________________________________________________________________
#%%
 
#mathematical operations
import numpy as np

#plotting
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#machine learning and statistical methods
import statsmodels.api as sm
df = pd.read_csv("./Data/datafinal.csv",sep=";")#df_cleaned(self)
#muting unnecessary warnings if needed
import warnings
# %%____________________________________________-
ts = DataCollection.data() # data from 2019-01-01 00:00:00 to 2022-11-14 23:45:00

# %%
#splitting time series to train and test subsets
#y_test = ts.iloc[-35880:,:].copy()
#Unobserved Components model definition
df = pd.read_csv("./Data/datafinal.csv",sep=";")#df_cleaned(self)
model_UC1 = sm.tsa.UnobservedComponents(df,
                                        level='dtrend',
                                        irregular=True,
                                        stochastic_level = False,
                                        stochastic_trend = False,
                                        stochastic_freq_seasonal = [False, False, False],
                                        freq_seasonal=[{'period': 672, 'harmonics': 1},
                                                       {'period': 2880, 'harmonics': 1},
                                                       {'period': 35066, 'harmonics': 2}])
#fitting model to train data
model_UC1res = model_UC1.fit()
#%%
#printing statsmodels summary for model
print(model_UC1res.summary())

print("")

#calculating mean absolute error and root mean squared error for in-sample prediction of model
print(f"In-sample mean absolute error (MAE): {'%.0f' % model_UC1res.mae}, In-sample root mean squared error (RMSE): {'%.0f' % np.sqrt(model_UC1res.mse)}")

#model forecast
forecast_UC1 = model_UC1res.forecast(steps=35880)

#calculating mean absolute error and root mean squared error for out-of-sample prediction for model evaluation
error = np.sqrt(np.mean([(y_test.iloc[x,:] - forecast_UC1[x]) ** 2 for x in range(len(forecast_UC1))]))      
print(f"Out-of-sample root mean squared error (RMSE): {'%.0f' % error}")
# %%__________________
#plotting residual diagnostics of Unobserved Components model
model_UC1res.plot_diagnostics(figsize=(18,18),lags=60).set_dpi(200);
plt.show();
# %%
model_UC1res.predict(start="2022-12-08 00:00:00", end="2022-12-08 23:45:00")
# %%

pred = model_UC1res.predict(start="2021-11-06 06:00:00", end="2022-12-08 23:45:00")
f = plt.figure(figsize=(18,6),dpi=200);
#setting title and size of title
plt.suptitle('Unobserved Components model prediction Vs Real dataset', fontsize=20);
#setting y axis label
plt.ylabel('MW');
#plotting trend component
plt.plot(y_test, label='France Electric Power Energy consumption (MW)');
#plotting linear model of trend component
plt.plot(pred, label='Unobserved Components model prediction');

plt.legend();

