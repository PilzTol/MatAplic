import streamlit as st
#import yfinance as yf


st.title('Stock Price App')
#Sidebar 
st.sidebar.header('User Input')
symbol = st.sidebar.text_input('Esolha um ativo:', 'AAPL')
st.write(symbol)
