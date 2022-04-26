from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.title("Playing around - stock prices")
"Retrieves recent stock prices from Yahoo Finance"

ticker = st.text_input("Enter ticker symbol")

clicked = st.button("Get Prices")

if clicked:

  if ticker:

    base_url = "https://query1.finance.yahoo.com/v7/finance/download/"
    url_args= "?period1=1619473704&period2=1651009704&interval=1d&events=history&includeAdjustedClose=true"
    url = base_url + ticker + url_args

    try:
      df = pd.read_csv(url)
    except:
      st.error("No data from that ticker. Try again, Jon!")
      st.stop()
    if df.empty:
      st.error("No data from that ticker. Try again, Jon!")
    else:
      price = df[['Date','Close']]
      price['Date'] = price['Date'].astype('datetime64[D]')
      price = price.set_index('Date')
      last_close = price.iloc[0,0]
      st.metric("Last Close Price", last_close)

      st.line_chart(price)
  else:
    st.error("Needs a ticker, Jon!")
