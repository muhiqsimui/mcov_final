import requests as r
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re




def scrape_case(url,class_name):
  data = r.get(url)
  soup = BeautifulSoup(data.content, 'html.parser')
  x = soup.find_all("span", class_=class_name)
  g = x[2].text
  h = re.findall(r'\d+', g)
  s_case = ''.join(map(str,h))
  return s_case

# scrape_case('https://covid19.who.int/','sc-fzoVTD ckBKGO')

def scrape_death(url,class_name):
  data = r.get(url)
  soup = BeautifulSoup(data.content, 'html.parser')
  x2 = soup.find("span", class_=class_name).text
  h = re.findall(r'\d+', x2)
  s_death = ''.join(map(str,h))
  return s_death

# scrape_death('https://covid19.who.int/','sc-fzoVTD wbXOD')

jumlah_positif = str(scrape_case('https://covid19.who.int/','sc-fzoVTD ckBKGO'))
jumlah_sembuh = '0'
jumlah_meninggal = str(scrape_death('https://covid19.who.int/','sc-fzoVTD wbXOD'))