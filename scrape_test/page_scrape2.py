# Scraping a webpage on the World Wide Web

from bs4 import BeautifulSoup
import requests

url = requests.get('http://quotes.toscrape.com/page/3')
soup = BeautifulSoup(url.text, 'html.parser')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')

for quote, author  in zip(quotes, authors):
    print(quote.text + ' - ' + author.text)
