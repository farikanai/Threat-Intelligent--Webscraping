import requests
from bs4 import BeautifulSoup
import re
import os
import csv 

# def scrape_links(url):
#     response = requests.get(url,headers={'User-Agent': 'WebsecApp'})
#     soup = BeautifulSoup(response.text, 'html.parser')
#     links = []
#     for link in soup.find_all('a'):
#         href = link.get('href')
#         if href and re.match(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', href):
#             links.append(href)
#     return links

# def save_links_to_file(links, filename):
#     with open(filename, 'a') as file:
#         for link in links:
#             file.write(link + '\n')
# # def search_links(search_term, filename):
# #     with open(filename, 'r') as file:
# #         links = file.readlines()
# #     related_links = [link.strip() for link in links if search_term.lower() in link.lower()]
# #     return related_links
# def save_to_csv(data):
#      with open("helil.csv", 'a',newline='', encoding="utf-8") as  csvfile:
#          # Create a CSV writer object
#         writer = csv.writer(csvfile)
        
#         # Write the header if the file is new
#         if csvfile.tell() == 0:
#             writer.writerow(['Date', 'Category', 'Title', 'Description'])
        
#         # Write each article
#         for item in data:
#             writer.writerow(item)
# def main():
    # url = 'https://thehackernews.com'mal
    # List of URLs to scrape
    # urls = [
    #     "https://www.securityweek.com/",
    #     "https://www.securitymagazine.com/",
    #     "https://krebsonsecurity.com/",
    #     "https://www.helpnetsecurity.com/",
    #     "https://grahamcluley.com/",
    #     "https://www.darkreading.com/",
    #     "https://cybersecurityventures.com/today/"
    # ]
url = 'https://thehackernews.com'
filename = 'links.txt'

response = requests.get(url,headers={'User-Agent': 'WebsecApp'})
soup = BeautifulSoup(response.text, 'html.parser')
print(response)
links = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href and re.match(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', href):
        links.append(href)

# with open(filename, 'a') as file:
#     for link in links:
#         file.write(link + '\n')
#         print(links)
    
# Scrape the website and save the links
# links = scrape_links(url)
# save_links_to_file(links, filename)
# for link in links:
#     print(links)

with open("helil.csv", 'a',newline='', encoding="utf-8") as  csvfile:
        # Create a CSV writer object
    writer = csv.writer(csvfile)
    
    # Write the header if the file is new
    if csvfile.tell() == 0:
        writer.writerow(['Date', 'Category', 'Title', 'Description'])
    
    # Write each article
    for item in links:
        writer.writerow(item)

# if __name__ == "__main__":
#     main()

