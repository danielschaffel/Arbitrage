import sys
sys.path.insert(0,'/home/daniel/Desktop/Arbitrage/Structures')
import EdgeWeightedDigraph
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
from selenium import webdriver

def getRates():
    html = urlopen("https://www.x-rates.com/table/?from=USD&amount=1")
    bsobj = BeautifulSoup(html,"html.parser")
    #so the link is a BeutifulSoup object so if i want to access just remember that
    links =  bsobj.findAll("tr") 
    for link in links:
        #findAll returns a set with all of the info so that is how i need to be accesing it
        val = link.findAll("a")
        name = link.findAll("td")
        for nam in name:
            print(name.pop().get_text())
            print(name.pop().get_text())
            print(name.pop().get_text())
        print()

getRates()
