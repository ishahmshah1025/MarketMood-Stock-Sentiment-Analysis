import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import os
import requests
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

def apple_graph():

    image_path = '\static.apple_stock_price.png'
    print(image_path)  
    return image_path

apple_graph()
def get_top_stock_picks():
    symbols = [
        'RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'INFY.NS', 'HINDUNILVR.NS',
        'ICICIBANK.NS', 'SBIN.NS', 'BHARTIARTL.NS', 'KOTAKBANK.NS', 'LT.NS',
        'AAPL', 'TSLA', 'AMZN', 'GOOGL', 'MSFT', 'NFLX', 'NVDA', 'FB', 'JPM', 'V'
    ]
    
    stock_data = pd.DataFrame()

    for symbol in symbols:
        stock = yf.Ticker(symbol)
        hist = stock.history(period="1d")  
        
        if not hist.empty and 'Close' in hist.columns and 'Open' in hist.columns:
            last_price = hist['Close'].iloc[-1]
            change = last_price - hist['Open'].iloc[-1]
            percent_change = (change / hist['Open'].iloc[-1]) * 100
            
            new_row = pd.DataFrame({
                'Symbol': [symbol],
                'Last Price': [last_price],
                'Change': [change],
                '% Change': [percent_change],
                'Volume': [hist['Volume'].iloc[-1]]
            })

            stock_data = pd.concat([stock_data, new_row], ignore_index=True)

    if not stock_data.empty:
        top_picks = stock_data.sort_values(by='% Change', ascending=False).head(5)  
        return top_picks
    else:
        return None