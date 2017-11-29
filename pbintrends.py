from urllib.request import urlopen
from bs4 import BeautifulSoup
Base = "http://pastebin.com"
Url = "http://pastebin.com/trends/"

def getText(Url):
	html= urlopen(Url)
	bsObj=BeautifulSoup(html,"lxml")
	try:
		return bsObj.find("textarea",{"id":"paste_code"}).getText()
	except Exception:
		pass

def getLinks(Url):
	html= urlopen(Url)
	bsObj=BeautifulSoup(html).find("table",{"class":"maintable"})
	for link in bsObj.findAll("a"):
#		print(bsObj)

#		print(link)
		if 'href' in link.attrs:
#			print(Base + link.attrs['href'])
			print("---------\n----------URL::\n--------- " + Base + link.attrs['href'])
			print(getText(Base + link.attrs['href']))
			print("\n")
#	return bsObj
	#print(bsObj)
#	return bsObj.find("div",{"class":"maintable"})#.findAll("a")

getLinks(Url)
#data = getLinks(Url)	
#print(data)
#for link in data:
#	if 'href' in link.attrs:
#		print(link)
		#print(link.attrs)

