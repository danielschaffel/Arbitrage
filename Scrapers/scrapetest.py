from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

html = urlopen("https://www.x-rates.com/table/?from=USD&amount=1")
bsobj = BeautifulSoup(html,"html.parser")
for link in bsobj.findAll("tr"):#,class_="rtRates"):
    print(link.getText())
