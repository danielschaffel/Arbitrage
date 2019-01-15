from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

<<<<<<< HEAD
html = urlopen("https://www.x-rates.com/table/?from=USD&amount=1")
bsobj = BeautifulSoup(html,"html.parser")
for link in bsobj.findAll("tr"):#,class_="rtRates"):
    print(link.getText())
=======
html = urlopen("https://www.x-rates.com/")
bsobj = BeautifulSoup(html,"html.parser")
for link in bsobj.findAll("a", href=re.compile("/graph/")):
    print(re.findAll("\w" ,link)
>>>>>>> 9f5d754e65eb8f32c68776e49e85830c410a5021
