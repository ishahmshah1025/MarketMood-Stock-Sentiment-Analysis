from flask import Flask, jsonify, render_template
import yfinance as yf
import pandas as pd

app = Flask(__name__)

def get_top_stock_picks():
    symbols = [
        'RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'INFY.NS', 'HINDUNILVR.NS',
        'ICICIBANK.NS', 'SBIN.NS', 'BHARTIARTL.NS', 'KOTAKBANK.NS', 'LT.NS',
        'AAPL', 'TSLA', 'AMZN', 'GOOGL', 'MSFT', 'NFLX', 'NVDA', 'FB', 'JPM', 'V'
    ]
    
    stock_data = pd.DataFrame()

    # Fetch data for each symbol
    for symbol in symbols:
        stock = yf.Ticker(symbol)
        hist = stock.history(period="1d")  # Get today's data
        
        # Check if the historical data is not empty
        if not hist.empty and 'Close' in hist.columns and 'Open' in hist.columns:
            last_price = hist['Close'].iloc[-1]
            change = last_price - hist['Open'].iloc[-1]
            percent_change = (change / hist['Open'].iloc[-1]) * 100
            
            # Create a new DataFrame for the current stock
            new_row = pd.DataFrame({
                'Symbol': [symbol],
                'Last Price': [last_price],
                'Change': [change],
                '% Change': [percent_change],
                'Volume': [hist['Volume'].iloc[-1]]
            })

            # Concatenate the new row with the existing DataFrame
            stock_data = pd.concat([stock_data, new_row], ignore_index=True)
        else:
            print(f"No data for {symbol}. It may be due to market closure or invalid symbol.")

    # Sort by % Change to find top picks
    if not stock_data.empty:
        top_picks = stock_data.sort_values(by='% Change', ascending=False).head(5)  # Top 5 stocks
        return top_picks
    else:
        print("No valid stock data retrieved.")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_top_stocks')
def get_top_stocks():
    top_stocks = get_top_stock_picks()
    if top_stocks is not None:
        return jsonify(top_stocks.to_dict(orient='records'))  # Convert DataFrame to JSON
    else:
        return jsonify([])  # Return empty list if no data

if __name__ == '__main__':
    app.run(debug=True)
