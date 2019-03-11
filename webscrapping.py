from urllib.request import urlopen as urls
from bs4 import BeautifulSoup as su
my_url='https://www.flipkart.com/search?q=apple+phons&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on'
'&as=off&as-pos=0&as-type=HISTORY'
vurl=urls(my_url)
data=vurl.read()
vurl.close()
page_soup=su(data,"html.parser")
content=page_soup.findAll("div",{'class':'_3O0U0u'})
print(len(content))
#print(su.prettify(content[0]))
containers=content[0]
print(containers.div.img['alt'])
price=containers('div',{'class':'_1uv9Cb'})
print(price[0].text)
rating=containers("div",{'class':"hGSR34"})
print(rating[0].text)