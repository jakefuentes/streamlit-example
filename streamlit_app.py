from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.title("Playing around - stock prices")

ticker = st.text_input("Enter ticker symbol")

clicked = st.button("Get Prices")

base_url = "https://query1.finance.yahoo.com/v7/finance/download/"
url_args= "?period1=1619473704&period2=1651009704&interval=1d&events=history&includeAdjustedClose=true"

url = base_url + ticker + url_args
st.write(url)
