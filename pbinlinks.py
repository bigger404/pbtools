from urllib.request import urlopen
from bs4 import BeautifulSoup

#html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
#html = urlopen("http://en.wikipedia.org/wiki/Railgun")
html = urlopen("http://pastebin.com/archive/")
bsObj = BeautifulSoup(html,"lxml")
for link in bsObj.findAll("a"):
	if 'href' in link.attrs:
		print(link)
	#print(link.attrs)
