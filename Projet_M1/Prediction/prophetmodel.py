class Model():
    from statsmodels.tools.eval_measures import rmse
    from sklearn.model_selection import train_test_split
    import matplotlib.pyplot as plt
    from prophet.plot import plot_components_plotly
    from prophet.plot import plot_plotly
    from prophet import Prophet
    from Prediction import data
    import pandas as dp
    # preprocessing  data
    df = data.dataframe()
    dff = df.reset_index()
    dff.rename(columns={'Consommation (MW)': 'y', 'Temps': 'ds'}, inplace=True)
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


    # penser à rendre le telechargement plus rapide
    #
