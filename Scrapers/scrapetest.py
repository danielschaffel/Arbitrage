import sys
sys.path.append('/home/daniel/Desktop/Arbitrage/Structures')
import EdgeWeightedDigraph
sys.path.append('/home/daniel/Desktop/Arbitrage/CycleDetectors')
import BellmanFord
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import math

#di is going to be used to associate each currency with a number for the digraph
di = {}
di['USD'] = 0
#returns a sequence of name and values
def getRates(url):
    html = urlopen(url)
    bsobj = BeautifulSoup(html,"html.parser")

    #so the link is a BeutifulSoup object so if i want to access just remember that
    #table is the table with all the exchange values
    table =  bsobj.find("table", class_ = "ratesTable")
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
            #this last one contains the title which i dont care about now that extract with regex
            name.pop()

            #extracts the two initials as a tuple but that tuple is returned in a list
            fcT = re.findall('from=(.+)&amp;to=(.+)\"',str(fc))
            tcT = re.findall('from=(.+)&amp;to=(.+)\"',str(tc))
            fromCurr.append(fc.get_text())
            toCurr.append(tc.get_text())
            cur = fcT[0][0]
            currName.append(cur)
            #adds cur initials if not in di
            if cur not in di:
                di[cur] = len(di) + 1 
    
    #returns all the lists together
    return zip(currName,fromCurr,toCurr)

def addToGraph():
    urlU = "https://www.x-rates.com/table/?from=USD&amount=1"
    urlBeginning = "https://www.x-rates.com/table/?from="
    urlEnd = "&amount=1"
    graph = EdgeWeightedDigraph.Digraph(12)
    getRates(urlU)
    
    for url in di:
        current = url
        fullUrl = urlBeginning + url + urlEnd

        for (a,b,c) in getRates(fullUrl):
            #edge from current to current from getRates
            edgeTo = EdgeWeightedDigraph.DirectedEdge(di[current],di[a],math.log(float(b)))
            #other way around
            edgeFrom = EdgeWeightedDigraph.DirectedEdge(di[a],di[current],math.log(float(c)))
            graph.add_edge(edgeTo)
            graph.add_edge(edgeFrom)
    return graph
gr = addToGraph()
print("finished reading from x-rates",gr.get_E(),gr.get_V())
bf = BellmanFord.BellmanFord(gr,0)
bf.printDistTo()