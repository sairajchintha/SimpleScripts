import requests
import bs4
url="https://www.etrainstatus.com/live-status?train_number="
train_number=input("enter train number :")
fin_url=url+train_number
res=requests.get(fin_url)
soup=bs4.BeautifulSoup(res.content, 'lxml')
result=soup.find(class_='contantprt')
for li in result.findAll('li'):
    print(li.text)