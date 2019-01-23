import sys
sys.path.insert(0,'/home/daniel/Desktop/Arbitrage/Structures')
import EdgeWeightedDigraph
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
from selenium import webdriver

#di is going to be used to associate each currency with a number for the digraph
di = {}
#di["USD"] = 1 

#returns a sequence of name and values
def getRates(url):
    html = urlopen(url)
    bsobj = BeautifulSoup(html,"html.parser")

    
    #so the link is a BeutifulSoup object so if i want to access just remember that
    #table is the table with all the exchange values
    table =  bsobj.find("table", class_ = "tablesorter ratesTable")
    links = table.findAll('tr')
    #from whatever currency in the table to the currency in the link
    fromCurr = []
    #from currency in the link to one in the table
    toCurr = []
    currName = []
    for link in links:
        #findAll returns a set with all of the info so that is how i need to be accesing it
        name = link.findAll("td")
        #adds all of them into individual lists
        for nam in name:
            fc = name.pop()
            tc = name.pop()
            #extracts the two initials as a tuple but that tuple is returned in a list
            fcI = re.findall('from=(.+)&amp;to=(.+)\"',str(fc))
            print(fcI)
            fromCurr.append(fc.get_text())
            toCurr.append(tc.get_text())
            cur = name.pop().get_text()
            if cur not in di:
                di[cur] = len(di) + 1 
            #currName.append(name.pop().get_text())
            #currName.append(re.compile())
    for name,num in di.items():
        print(name," = ",num)
    
    #returns all the lists together
    return zip(currName,fromCurr,toCurr)

urlU = "https://www.x-rates.com/table/?from=USD&amount=1"
urlB = "https://www.x-rates.com/table/?from=GBP&amount=1"

for (a,b,c) in getRates(urlU):
    print(a,b,c)


print()
getRates(urlB)