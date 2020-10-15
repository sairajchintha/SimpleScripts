
import selenium.webdriver as webdriver
from bs4 import BeautifulSoup as bs
import requests
import urllib.request,urllib.parse,urllib.error
print('Input Instagram picture url to Download:')
url=input()
driver = webdriver.Chrome()
driver.get(url)
urls=requests.get(url)
soup=bs(driver.page_source,"html.parser")
download=soup.find(class_="FFVAD")
r=download.get('src',None)
path="D:\YTDL"
#urllib.request.urlretrieve(r, path)
urllib.request.urlretrieve(r, str(path)+"/image"+".jpg")


#request = requests.get("https://www.instagram.com/explore/tags/nature/")
#content = request.content
#soup = BeautifulSoup(content,"html.parser")
#element = soup.find("srcset")
#print(element.text.strip())