import urllib3
import urllib.request
import requests
import json
from PIL import Image 

name=input("Enter Instagram username :")
url='https://www.instagram.com/'+name+'/?__a=1'
http = urllib3.PoolManager()
d=http.request('GET',url)
userdata=d.data
info = json.loads(userdata.decode('utf-8'))
#print(type(res_dict))

dpUrl=info['graphql']['user']['profile_pic_url_hd']

print("Full Name : ",info['graphql']['user']['full_name'])
print("Bio : ",info['graphql']['user']['biography'])
print("Posts : ",info['graphql']['user']['edge_owner_to_timeline_media']['count'])
print("Followers : ",info['graphql']['user']['edge_followed_by']['count'])
print("Followed : ",info['graphql']['user']['edge_follow']['count'])

#response = requests.get(dpUrl)

path=r"C:\Users\Asus\Desktop\insta"

urllib.request.urlretrieve(dpUrl, str(path)+"/image"+".jpg")




# creating a object for image 
im = Image.open(path+"\image.jpg")#here use your path where python files are stored.

#this show() uses computer's image viewer
#im.show()

#to convert the jpg image to ppm format
im.save(path+"\image.ppm")

#To display image GUI using tkinter package
from tkinter import *     
root = Tk()      
canvas = Canvas(root, width = 300, height = 300)      
canvas.pack()      
img = PhotoImage(file=path+"\image.ppm")      
canvas.create_image(20,20, anchor=NW, image=img)      
mainloop()   