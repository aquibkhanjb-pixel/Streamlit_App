import pandas as pd 
import streamlit as st
import yfinance as yf
import datetime as dt

st.write("""
# Stock Price Analyser
         
Shown are the stock closing price and volume of a company!
""")


#ticker_symbol = 'AAPL' # You can change the ticker symbol to any valid stock ticker
ticker_symbol = st.text_input("Enter Stock Symbol", "AAPL") #input for ticker symbol

col1, col2 = st.columns(2) #creating two columns in the app
with col1:
    #start date from the user
    start_date = st.date_input("Input Start date", dt.date(2023, 1, 1))
with col2:
    #end date from the user
    end_date = st.date_input("Input End date", dt.date(2025, 6, 3))
# If the start date is after the end date, raise an error
if start_date > end_date:
    st.error("Error: End date must be after start date.")  

st.write(f" ### Showing data for {ticker_symbol} from {start_date} to {end_date}")
# Fetching stock data using yfinance      
ticker_data = yf.Ticker(ticker_symbol) #you can get this from yfinance website
ticker_df = ticker_data.history(period="1d")
ticker_df = ticker_data.history(start=f"{start_date}", end=f"{end_date}") 
#period can be minute, hour, day, week, month, year
#history() returns a pandas dataframe with the stock data
st.dataframe(ticker_df) #it will display the dataframe in the app

#Showcasing charts
st.write(""" ## Daily Closing Price charts""")
st.line_chart(ticker_df.Close) #line chart for closing price

st.write(""" ## Volume of shares traded each day""")
st.line_chart(ticker_df.Volume) #line chart for volume 
#Volume is the number of shares traded during a given period
