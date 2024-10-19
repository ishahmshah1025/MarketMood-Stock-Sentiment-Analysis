from flask import Flask, render_template
import yfinance as yf
import pandas as pd
from model import *
app = Flask(__name__)

@app.route('/')
def index():
    top_stocks = get_top_stock_picks()
    return render_template('index.html', top_stocks=top_stocks)

def apple_view():
    images_path = apple_graph()
    return render_template('index.html', image_path=images_path)

if __name__ == '__main__':
    app.run(debug=True)
