import bs4
import requests

link="https://economictimes.indiatimes.com/commoditysummary/symbol-SILVER.cms"
link2="https://economictimes.indiatimes.com/commoditysummary/symbol-GOLD.cms"
res2=requests.get(link2)
res=requests.get(link)
soup=bs4.BeautifulSoup(res.content, 'lxml')
soup2=bs4.BeautifulSoup(res2.content, 'lxml')
result=soup.find(class_='commodityPrice')
result2=soup2.find(class_='commodityPrice')
print("Today's 1 Kg Silver Price in India :₹"+result.text)
print("Today's 10 gm Gold Price in India :₹"+result2.text)