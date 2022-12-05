
from statsmodels.tools.eval_measures import rmse
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
#from prophet import plot_components_plotly
#from prophet import plot_plotly
from prophet import Prophet
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import statsmodels.api as sm
#import data 

def Model():

    df = pd.read_csv(".data/datafinal.cvs")#pd.read_csv("/Users/mac/Desktop/HAX712X-DOS/Project/Prediction/DataSet.csv")
    df = df.set_index("Time")
    df.index = pd.to_datetime(df.index)
    ts = df[df.index<"2022-11-30 00:00:00"]
    f, ax = plt.subplots(figsize=(12,6),dpi=200);
    plt.suptitle('France Electric Power Energy (MW) consumption', fontsize=24);
    df.plot(ax=ax,rot=90,ylabel='MW');
    plt.show()
    df['ds'] = df.index
    df.rename(columns={'Consommation (MW)': 'y'}, inplace=True)
    # training data
    #train, test = train_test_split(df, test_size=0.20, shuffle=False)
    m = Prophet()
    # m=Prophet(changepoint_prior_scale=0.01).fit(train)
    proph = m.fit(df)
    #traine_fauture = proph.make_future_dataframe(periods=len(test), freq='15T')
    usecols2019=['Date', 'Heure', "Consommation (MW)"] # variables we needs
    days = pd.read_csv("/Users/mac/Downloads/3days.csv",usecols=usecols2019, sep = ";")
    time_improved = pd.to_datetime(days['Date'] +
                                       ' ' + days['Heure'],
                                       format='%Y-%m-%d %H:%M')
    days['Time'] = time_improved  # add the Time to the data
    days.set_index('Time', inplace=True) # set time as index
    # remove useles columns
    del days['Heure']
    del days['Date']
    days = days.sort_index(ascending=True)
    test = days.copy()
    test['ds'] = test.index
    test = test.rename(columns={'Consommation (MW)': 'y'}, inplace=False)
    forcast = proph.predict(test)
    daypred = forcast[["ds", "yhat"]]
    daypred = daypred.set_index("ds") 
    daypred.index = pd.to_datetime(daypred.index)
    daypred = daypred + 7000 #shifting 
    #test = test.set_index("ds")
    #test.index = pd.to_datetime(test.index)
    f, ax = plt.subplots(figsize=(12,6),dpi=200);
    plt.suptitle('France Electric Power Energy (MW) consumption', fontsize=24);
    daypred.plot(ax=ax,rot=90,ylabel='MW');
    days.plot(ax=ax,rot=90,ylabel='MW');
    plt.show()