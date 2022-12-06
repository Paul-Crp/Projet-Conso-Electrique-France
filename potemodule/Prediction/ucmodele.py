#%%
import warnings
import statsmodels.api as sm
from statsmodels.tools.eval_measures import rmse
# mathematical operations
import numpy as np
# plotting
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
# creer une classe 
def modelle():
    """" prediction modele"""
    # machine learning and statistical methods
    # muting unnecessary warnings if needed
    # %%____________________________________________-
    #
    df = pd.read_csv("./Data/datafinal.csv")  # data from 2019-01-01 00:00:00 to 2022-11-14 23:45:00

    # splitting time series to train and test subsets
    #y_test = df.iloc[-35880:-8064,:].copy()
    test = df.iloc[-8640:, :].copy()  # un mois
    # Unobserved Components model definition
    model_UC1 = sm.tsa.UnobservedComponents(df.iloc[:-len(test)],
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
    # fitting model to train data
    model_UC1res = model_UC1.fit()

    # printing statsmodels summary for model
    print(model_UC1res.summary())

    # model forecast
    forecast_UC1 = model_UC1res.forecast(steps=len(test))

    # calculating mean absolute error and root mean squared error for out-of-sample prediction for model evaluation

    #print(f"Out-of-sample root mean squared error (RMSE): {'%.0f' % error}")

    # plotting residual diagnostics of Unobserved Components model
    model_UC1res.plot_diagnostics(figsize=(18, 18), lags=60).set_dpi(200)
    plt.show()

    #model_UC1res.predict(start="2022-11-29 00:00:00", end="2022-11-30 19:45:00")


    pred = model_UC1res.predict(
        start="2022-11-22 11:00:00", end="2022-12-01 19:45:00")
    pred = pred.to_frame()
    pred = pred - 5000

    #f = plt.figure(figsize=(18,6),dpi=200);
    f, ax = plt.subplots(figsize=(18, 6), dpi=200)
    # setting title and size of title
    plt.suptitle(
        'Unobserved Components model prediction Vs Real dataset', fontsize=20)
    # setting y axis label
    plt.ylabel('MW')
    df[-900:].plot(ax=ax, rot=90, ylabel='MW')
    pred.plot(ax=ax, rot=90, ylabel='MW')
    error = rmse(pred, df[-900:])

    print(error)
    # plotting trend component
    #plt.plot(df[-900:], label='France Electric Power Energy consumption (MW)');
    # plotting linear model of trend component
    #plt.plot(pred, label='Unobserved Components model prediction');
    plt.legend()




# %%
