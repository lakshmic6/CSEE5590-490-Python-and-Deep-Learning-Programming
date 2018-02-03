import urllib.request
from bs4 import BeautifulSoup
import os

def y():
    url = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
    source_code = urllib.request.urlopen(url)
    plain_text = source_code
    soup = BeautifulSoup(plain_text, "html.parser")
    tabulka = soup.find("table", {"class" : "wikitable sortable plainrowheaders"})
    for row in tabulka.findAll('tr'):
      col = row.findAll('td')
      b = row.findAll('th')
      print(col)
      print(b)

y()