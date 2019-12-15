from bs4 import BeautifulSoup
import requests

url = requests.get("https://free.facebook.com/?af_rdr=1")

soup = BeautifulSoup(url, 'lxml')
print(soup)