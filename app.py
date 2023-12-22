import streamlit as st
#import yfinance as yf
from plot.interactive import plot_line_i

st.title('Stock Price App')
#Sidebar 
st.sidebar.header('User Input')
symbol = st.sidebar.text_input('Esolha um ativo:', 'AAPL')
st.write(symbol)

#Plot

fig = plot_line_i(symbol)
st.plotly_chart(fig)