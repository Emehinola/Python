import requests
from bs4 import BeautifulSoup

file = requests.get("http://freebasics.com")

soup = BeautifulSoup(file, "lxml")
print(soup)			