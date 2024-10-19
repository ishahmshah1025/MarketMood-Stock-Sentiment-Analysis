from flask import Flask, render_template, redirect, url_for
import yfinance as yf
import pandas as pd
from model import *

app = Flask(__name__)

@app.route('/')
def index():
    top_stocks = get_top_stock_picks()
    return render_template('index.html', top_stocks=top_stocks)

@app.route('/index2')  # New route for index2 page
def index2():
    # Logic for index2 page (if any)
    return render_template('index2.html')  # Ensure this template exists

@app.route('/get-started')  # Route to handle the "Get Started" button click
def get_started():
    return redirect(url_for('index2'))  # Redirect to the index2 page

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

if __name__ == '__main__':
    app.run(debug=True)
