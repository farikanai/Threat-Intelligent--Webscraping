#1. to parse and collect web data on cyberthreats (webcrawler
#2.To use keywords to suggest user interested  sites webcrawler links}
#3.generate  threat intelligent insight data ( and sentiment analysis)
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import os

def scrape_links(url):
    response = requests.get(url,headers={'User-Agent': 'WebsecApp'})
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and re.match(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', href):
            links.append(href)
    return links

def save_links_to_file(links, filename):
    with open(filename, 'a') as file:
        for link in links:
            file.write(link + '\n')
    df = pd.read_csv('link.csv')

# Apply the cleaning function to each cell in the DataFrame
    df = df.drop_duplicates()
       
def search_links(search_term, filename):
    with open(filename, 'r') as file:
        links = file.readlines()
    related_links = [link.strip() for link in links if search_term.lower() in link.lower()]
    return related_links

def main():
    # url = 'https://thehackernews.com'mal
    # List of URLs to scrape
    urls = [
        "https://www.securityweek.com/",
        "https://www.securitymagazine.com/",
        "https://krebsonsecurity.com/",
        "https://www.helpnetsecurity.com/",
        "https://grahamcluley.com/",
        "https://www.darkreading.com/",
        "https://cybersecurityventures.com/today/",
        "https://thehackernews.com/"

    ]
    # url = 'https://helpnetsecurity.com'
    filename = 'link.csv'
    
    for url in urls :  
        # Scrape the website and save the links
        links = scrape_links(url)
        save_links_to_file(links, filename)
    
    # Search for a related link
    search_term = input("Enter a search term: ")
    related_links = search_links(search_term, filename)
    
    if related_links:
        print("Related links:")
        for link in related_links:
            print(link)
    else:
        print("No related links found.")

if __name__ == "__main__":
    main()

