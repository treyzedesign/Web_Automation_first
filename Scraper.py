from bs4 import BeautifulSoup
import requests

def Scraper(url):
    res = requests.get(url).text
    soup = BeautifulSoup(res, 'lxml')
    print(soup.prettify())