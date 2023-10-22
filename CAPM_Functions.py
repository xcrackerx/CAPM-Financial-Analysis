import plotly.express as px
import numpy as np

#function to plot interactive plotly chart

def plot_chart(df):
    figure = px.line()
    for i in df.columns[1:]:
        figure.add_scatter(x = df['Date'], y = df[i], name = i)
        figure.update_layout(width = 450, margin = dict(l=20, r=20, t=50, b=20), legend = dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1))
    return figure

#function to normalize the prices based on the initial price

def normalize(df_2):
    df = df_2.copy()
    for i in df.columns[1:]:
        df[i] = df[i]/df[i][0]
    return df

#function to calculate daily returns

def daily_return(df):
    df_daily_return = df.copy()
    for i in df.columns[1:]:
        for j in range(1, len(df)):
            df_daily_return[i][j] = ((df[i][j]-df[i][j-1])/df[i][j-1])*100
    df_daily_return[i][0] = 0
    return df_daily_return

#function to calculate beta

def beta_calculation(stocks_daily_return , stock):
    rm = stocks_daily_return['sp500'].mean()*252

    b, a = np.polyfit(stocks_daily_return['sp500'], stocks_daily_return[stock], 1)
    return b,a