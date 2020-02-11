#This will be a BS4-based scraper to retrieve the 3 first news from  G1 website and save it as JSON file.
import requests
import json
from bs4 import BeautifulSoup
from lxml import html
import lxml.html

class Printer():
    """Print things to stdout on one line dynamically"""
    def __init__(self,data):
        sys.stdout.write("\r"+data.__str__())
        sys.stdout.flush()

#First let us see if we can retrieve some element and save it in the json file. 
#Afterwards we extend to the whole content desired
def getNews():
    item_count = 0
    links = []
    r = requests.get('https://g1.globo.com/')
    
    if r.status_code != 200:
        return None
 
    soup = BeautifulSoup(r.content, 'lxml')
    print 'Dadas as cartas'

    for a in soup.findAll('a', attrs={'class': 'feed-post'}):
        print 'Primeira rodada'
        links.append((a.text, a.get('href')))
        if self.item_count > 3:
            print 'Truco'
            break
        print 'Seis'
    
    if len(links) == 0:
        print ('Sem final feliz aqui')

    return links
    

def exportJSON():
#Save the json file
    f_json = open("itens.json",'w')
    with open("itens.json", "w") as myfile:
        myfile.write(json.dumps(getNews(),sort_keys=False))
    myfile.close()


exportJSON()