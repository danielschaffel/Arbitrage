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
    graph = EdgeWeightedDigraph.Digraph(len(links))
    for link in links:
        #findAll returns a set with all of the info so that is how i need to be accesing it
        name = link.findAll("td")
        for nam in name:
            fromCurr = name.pop().get_text()
            toCurr = name.pop().get_text()
            currName = name.pop().get_text()
            edgeTo = EdgeWeightedDigraph.DirectedEdge("USD" , currName , toCurr)
            edgeFrom = EdgeWeightedDigraph.DirectedEdge(currName , "USD" , fromCurr)
            print(str(edgeTo.edge_from()) + "---->" + str(edgeTo.get_weight()) + "---->" + str(edgeTo.edge_to()))
            print(str(edgeFrom.edge_from()) + "---->" + str(edgeFrom.get_weight()) + "---->" + str(edgeFrom.edge_to()))
            #graph.add_edge(edgeTo)
            # graph.add_edge(edgeFrom)
        print()

getRates()
