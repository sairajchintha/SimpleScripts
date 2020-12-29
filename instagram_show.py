import urllib3
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

response = requests.get(dpUrl)

file = open("insta_image.jpg", "wb")
file.write(response.content)
print("\n===> Profile pic Downloaded as insta_image.jpg <===")
file.close()

C:\Users\Asus\Desktop\sample.py
# creating a object for image 
im = Image.open(r"C:\Users\Asus\Desktop\insta_image.jpg")#here use your path where python files are stored.

#this show() uses computer's image viewer
#im.show()

#to convert the jpg image to ppm format
im.save(r"C:\Users\Asus\Desktop\insta_image.ppm")

#To display image GUI using tkinter package
from tkinter import *     
root = Tk()      
canvas = Canvas(root, width = 300, height = 300)      
canvas.pack()      
img = PhotoImage(file="insta_image1.ppm")      
canvas.create_image(20,20, anchor=NW, image=img)      
mainloop()   