from flask import Flask, render_template, request, jsonify
import praw
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import io
import base64

app = Flask(__name__)

reddit = praw.Reddit(
    client_id='t2bNyMB4wU0yXdeWb7nVcQ',
    client_secret='Y5iOhI76laXgItwsSFTiKfDcRNyqwQ',
    user_agent='QuantumCoders/0.1 by Ok_profession1025'
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sentiment', methods=['POST'])
def sentiment():
    stock_name = request.form.get('stock_name')
    sentiment_analyzer = SentimentIntensityAnalyzer()
    
    sentiments = {"positive": 0, "negative": 0, "neutral": 0}
    
    posts = reddit.subreddit('IndianStockMarket').search(stock_name, limit=100)
    
    for post in posts:
        text = post.title + " " + post.selftext
        sentiment_score = sentiment_analyzer.polarity_scores(text)

        # Count sentiments
        sentiments["positive"] += sentiment_score["pos"]
        sentiments["negative"] += sentiment_score["neg"]
        sentiments["neutral"] += sentiment_score["neu"]
    
    # Create a pie chart
    labels = ['Positive', 'Negative', 'Neutral']
    sizes = [sentiments["positive"], sentiments["negative"], sentiments["neutral"]]
    
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    
    pie_chart = base64.b64encode(img.getvalue()).decode('utf8')
    
    return jsonify({'chart': pie_chart})

if __name__ == '__main__':
    app.run(debug=True)
