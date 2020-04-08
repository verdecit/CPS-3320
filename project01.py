
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

myurl = 'http://books.toscrape.com/'

uClient = uReq(myurl)
pagehtml = uClient.read()
uClient.close()

pageSoup = soup(pagehtml, "html.parser")

#grabs the book info
containers = pageSoup.findAll("article",{"class":"product_pod"})

filename =  "Books.csv"
f = open(filename,"w")

headers = "Title, Status, Price\n"

f.write(headers)

#grabs, assigns and prints title, price and availability status for each book
for container in containers:
	title = container.h3.a["title"]

	status_container = container.findAll("p",{"class":"instock availability"})
	status = status_container[0].text.strip()

	container_price = container.findAll("p",{"class":"price_color"})
	price = container_price[0].text

	print("title: " + title)
	print("status: " + status)
	print("price: " + price.replace("£","$"))

	#writes to a csv file in excel to view spreadsheet
	f.write(title.replace(",",".") + "," + status + "," + price.replace("£","$") + "\n")