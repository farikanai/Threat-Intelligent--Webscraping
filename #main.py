import re
from flask import Flask, render_template, request 
from bs4 import BeautifulSoup
import matplotlib
import requests
from textblob import TextBlob
from jinja2 import Environment
env = Environment()
env.globals.update(zip=zip)
from dotenv import load_dotenv
from pprint import pprint
from bs4 import BeautifulSoup 
from urllib.request import urlopen
from urllib.error import HTTPError 
from urllib.error import URLError 
from urllib.parse import urljoin 
import requests
import csv
import os
from flask import Flask,render_template, request, send_file
import base64
import pandas as pd
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import io

app = Flask(__name__)

# def get_cyber_crime_feed():
#     articles = []
#     box_count =  0
#     url = 'https://thehackernews.com/'
#      #' https://thehackernews.com/'
    
#     ''' user agent to to prevent blocking :D, next challenge pagination '''
#     response = requests.get(url, headers={'User-Agent': 'WebsecApp'}) 
#     soup = BeautifulSoup(response.text, 'html.parser')
#     boxes = soup.find_all(class_='clear home-right')
    
#     for  box in boxes:
#         title = box.find(class_='home-title')
#         category = box.find(class_='h-tags')
#         date = box.find(class_='h-datetime')
#         description = box.find(class_='home-desc')
#         if title and date and description:
#             title = title.get_text()
#             date = date.get_text()
#             description = description.get_text()

#             category = category.get_text() if category else 'Unknown'
#             articles.append([date, category, title, description])
#             box_count +=  1
    
    
#     return articles, box_count

def data_cleaner():
    # Define a function to clean a string
    def clean_string(s):
        # Ensure s is a string
        if not isinstance(s, str):
            s = str(s)
        # Remove non-text characters
        return re.sub(r'\W+', ' ', s)

    # Read the CSV file
    df = pd.read_csv('helil.csv')

    # Apply the cleaning function to each cell in the DataFrame
    df = df.applymap(clean_string)

    # Save the cleaned DataFrame to a new CSV file
    df.to_csv('cleaned_file.csv', index=False)

    # Print a success message
    print("The CSV file was successfully cleaned and saved as cleaned_file.csv")



# @app.route('/')
# def index():
    
#         return render_template('index.html', articles= articles)
    


@app.route("/")
def show_plots():
    data = pd.read_csv('cleaned_file.csv', encoding='utf-8')

    # Ensure the 'Description' column is string type
    data['Description'] = data['Description'].astype(str)

    # Apply sentiment analysis
    data['Sentiment'] = data['Description'].apply(lambda x: TextBlob(x).sentiment.polarity)

    # Convert 'Date' column to datetime
    data['Date'] = pd.to_datetime(data['Date'], format='mixed',)

    # Save the data with the new 'Sentiment' column
    data.to_csv('cleaned_file1.csv', index=False)

    def save_plot_to_img(fig):
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        img = base64.b64encode(buf.getvalue()).decode('utf-8')
        return img

    # Plot a histogram of the sentiment scores
    plt.figure(figsize=(10, 6))
    plt.hist(data['Sentiment'], bins=30, color='skyblue', edgecolor='black')
    plt.title('Histogram of Sentiment Scores')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Frequency')
    hist_img = plt.show()
    plt.savefig('hist.png')
    hist_img= save_plot_to_img(plt)

    # # Plot a time series of the sentiment scores
    # plt.figure(figsize=(10, 6))
    # plt.plot_date(data['Date'], data['Sentiment'], linestyle='solid', marker=None)
    # plt.title('Time Series of Sentiment Scores')
    # plt.xlabel('Date')
    # plt.ylabel('Sentiment Score')
    # plt.show()

    # Plot a pie chart of the sentiment categories
    sentiment_categories = ['Positive' if score > 0 else 'Negative' if score < 0 else 'Neutral' for score in data['Sentiment']]
    sentiment_counts = pd.Series(sentiment_categories).value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Pie Chart of Sentiment Categories')
    # plt.show()
    pie_img = save_plot_to_img(plt)

    # Plot a bar chart of the average sentiment score per title
    average_sentiment_per_title = data.groupby('Title')['Sentiment'].mean()
    plt.figure(figsize=(10, 10))
    plt.bar(average_sentiment_per_title.index, average_sentiment_per_title.values, color='skyblue', edgecolor='black')
    plt.title('Bar Chart of Average Sentiment Score Per Title')
    plt.xlabel('Title')
    plt.ylabel('Average Sentiment Score')
    plt.xticks(rotation=90)
    # plt.show()
    bar_img = save_plot_to_img(plt)

    # print(hist_img,bar_img,pie_img )
    return render_template('index.html', hist_img=hist_img, pie_img=pie_img, bar_img=bar_img)


if __name__ == '__main__':
    app.run(debug=True)