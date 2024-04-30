# collect web data and generate threat intelligent insights ( topic modelling and sentiment analysis)
""" https://www.securityweek.com/
https://www.securitymagazine.com/
https://krebsonsecurity.com/
https://www.helpnetsecurity.com/
https://grahamcluley.com/
https://www.darkreading.com/
https://cybersecurityventures.com/today/
https://thehackernews.com/
"""
# a webscraper for eachone  saving to a single file

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



load_dotenv()
#def load_existing_content():
    

def get_cyber_crime_feed():
    articles = []
    box_count =  0
    url = 'https://thehackernews.com/'
     #' https://thehackernews.com/'
    
    ''' user agent to to prevent blocking :D, next challenge pagination '''
    response = requests.get(url, headers={'User-Agent': 'WebsecApp'}) 
    soup = BeautifulSoup(response.text, 'html.parser')
    boxes = soup.find_all(class_='clear home-right')
    
    for  box in boxes:
        title = box.find(class_='home-title')
        category = box.find(class_='h-tags')
        date = box.find(class_='h-datetime')
        description = box.find(class_='home-desc')
        if title and date and description:
            title = title.get_text()
            date = date.get_text()
            description = description.get_text()
            category = category.get_text() if category else 'Unknown'
            articles.append([date, category, title, description])
            box_count +=  1
    
    
    return articles, box_count

def save_to_csv(data):

    """    RSave  content from the webscraper  to csv (title, date ,description
    """
    with open("helil.csv", 'a',newline='', encoding="utf-8") as  csvfile:
         # Create a CSV writer object
        writer = csv.writer(csvfile)
        
        # Write the header if the file is new
        if csvfile.tell() == 0:
            writer.writerow(['Date', 'Category', 'Title', 'Description'])
        
        # Write each article
        for item in data:
            writer.writerow(item)
def read_from_file(data):

    """    Reads content from the specified file and returns it as a list of strings,
    where each string represents a line from the file.
    """
    try:
        # Read articles from CSV file
        with open("helil.csv", 'r', newline='', encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            content = list(reader)
            print("Content from CSV file:")
            pprint(content)
    except FileNotFoundError:
        print(f"File {'helil.csv'} not found.")
        return []

def main():
    articles, box_count = get_cyber_crime_feed()
    save_to_csv(articles)
    read_from_file('helil.csv')

if __name__ == '__main__':
    main()
