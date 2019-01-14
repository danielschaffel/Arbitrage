from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

html = urlopen("https://www.x-rates.com/")
bsobj = BeautifulSoup(html,"html.parser")
for link in bsobj.findAll("a", href=re.compile("/graph/")):
    print(re.findAll("\w" ,link)