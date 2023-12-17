from keras.models import load_model
import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
import pandas as pd
from  datetime import datetime , timedelta

stock_tickers = []
# number_of_stocks = st.text_input("Enter number of stocks you want to compare:","max 5 ")
user_input1 = st.text_input("Enter Stock Ticker 1:")
stock_tickers.append(user_input1)
# for i in range (int(number_of_stocks)):


user_input2 = st.text_input("Enter Stock Ticker 2:")
stock_tickers.append(user_input2)


# user_input3 = st.text_input("Enter Stock Ticker 3:")
# stock_tickers.append(user_input3)

# user_input4= st.text_input("Enter Stock Ticker 4:")
# stock_tickers.append(user_input4)

# user_input5 = st.text_input("Enter Stock Ticker 5:")
# stock_tickers.append(user_input5)




st.title(f"Stock price comparison")
# stock_tickers = ['AAPL', 'MSFT','GOOGL','TSLA']
end_date = datetime.now()
start_date = end_date - timedelta(days=365) 
# Fetch historical stock data using yfinance
stock_data = {ticker: yf.download(ticker, start=start_date, end=end_date )['Close'] for ticker in stock_tickers}

st.subheader(f"Comparison of stocks {stock_tickers[0]} ,{stock_tickers[1]}  : ({start_date} -({end_date}) ")
# Define a color map for stocks
if (len(stock_tickers)==2):
    color_map = {
    stock_tickers[0]: 'blue',
    stock_tickers[1]: 'green'
    }
elif (len(stock_tickers)==3):
    
    color_map = {
    stock_tickers[0]: 'blue',
    stock_tickers[1]: 'green',
    stock_tickers[2]: 'red'
    }
elif (len(stock_tickers)==4):
    
    color_map = {
    stock_tickers[0]: 'blue',
    stock_tickers[1]: 'green',
    stock_tickers[2]: 'red',
    stock_tickers[3]: 'orange'
    }


else:
    color_map = {
    stock_tickers[0]: 'blue',
    stock_tickers[1]: 'green',
    stock_tickers[2]: 'red',
    stock_tickers[3]: 'orange',
    stock_tickers[4]: 'purple'
}


traces = []
for ticker in stock_tickers:
    traces.append(go.Scatter(x=stock_data[ticker].index, y=stock_data[ticker], mode='lines', name=ticker, line=dict(color=color_map[ticker])))


layout = go.Layout(title='Stock Price Comparison', xaxis=dict(title='Date'), yaxis=dict(title='Stock Price (USD)'))


fig = go.Figure(data=traces, layout=layout)


# fig.show()
st.plotly_chart(fig)
for ticker in stock_data:
    st.title(ticker)
    # st.write(stock_data[ticker].describe())
    st_1 = yf.download(ticker, start="2022-01-01", end="2023-01-01")
    st.write(st_1)
    st.write(st_1.describe())