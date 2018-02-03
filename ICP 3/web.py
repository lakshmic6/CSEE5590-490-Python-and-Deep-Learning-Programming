from bs4 import BeautifulSoup
import urllib.request
import os
def x():
    url = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
    source_code = urllib.request.urlopen(url)
    plain_text = source_code
    soup = BeautifulSoup(plain_text, "html.parser")
    linked=soup
    print('<title>'.join(soup.title))
    for link in linked.find_all('a'):
        print(link.get('href'))
x()
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