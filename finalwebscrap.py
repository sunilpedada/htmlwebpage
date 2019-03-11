from urllib.request import urlopen as urls
from bs4 import BeautifulSoup as su
import csv
my_url='https://www.flipkart.com/search?q=apple+phons&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on'
'&as=off&as-pos=0&as-type=HISTORY'
vurl=urls(my_url)
data=vurl.read()
vurl.close()
page_soup=su(data,"html.parser")
content=page_soup.findAll("div",{'class':'_3O0U0u'})
print(len(content))
#print(su.prettify(content[0]))
for containers in content:
    product = containers.div.img['alt']
    price_content = containers('div', {'class': '_1vC4OE _2rQ-NK'})
    price = price_content[0].text
    rating_content = containers("div", {'class': "hGSR34"})
    ratings = rating_content[0].text
    p=product+'\n'+price+'\n'+ratings+'\n'
    print(p)
file=open('products.csv','w')
file.write(p)
file.close()
