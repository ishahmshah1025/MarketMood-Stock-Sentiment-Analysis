# MarketMood - Stock Sentiment Analysis
# Overview:
MarketMood is a comprehensive website that aims to analyze stock sentiment from various online platforms - taking information from trending news as well as social media sites, using natural language processing techniques. The project utilizes the VADER and FinBERT to classify sentiments as bullish, bearish or negative based on user discussions about stocks. The results are visualized through interactive charts, providing insights into market trends.

# Features:
- Sentiment Analysis: Analyzes stock related news and discussions to gauge public sentiment.
- Data Visualization: Present sentiment data in a user-friendly manner using pie and bar charts.
- Real-time Updates: Fetch the latest sentiment analysis based on user input for different stocks.
- Forum for real time news updates: Links to top trending news articles on stocks.
- Top stocks: Top stocks extracted from Money Control in real-time and displayed.
- Prediction: Using LSTM models to predict future stock prices.

# Technologies Used:
- Backend: Flask (Python web framework)
- Sentiment Analysis: VADER (Valence Aware Dictionary and sEntiment Reasoner) and FinBERT
- Data Visualization: Matplotlib and Chart.js (JavaScript library for data visualization)
- Frontend: HTML, CSS (with Tailwind CSS for styling)

# Acknowledgments:
- PRAW - Python Reddit API Wrapper
- VADER - Sentiment analysis tool
- Chart.js - Data visualization library
- Flask - Web framework for Python
- FinBERT: https://arxiv.org/abs/1908.10063
