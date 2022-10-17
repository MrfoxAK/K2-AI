from cProfile import label
from logging import root
from msilib.schema import Condition
from tkinter import *
import tkinter as tk
from unittest import result
from cv2 import exp
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from matplotlib import image, test
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import ImageTk, Image

def myWeather():
          

     root = Tk()
     root.title("Weather App MrFoxAK")
     root.geometry("900x500+300+200")
     root.resizable(False, False)

     def getWeather():
          try:
               city = textfield.get()
               geolocator = Nominatim(user_agent="geoapiExercises")
               location = geolocator.geocode(city)
               obj = TimezoneFinder()
               result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
               lat1 = location.latitude
               lon1 = location.longitude
               # print(lon1)
               # print(lat1)
               home = pytz.timezone(result)
               local_time = datetime.now(home)
               curr_time = local_time.strftime("%I:%M %p")
               clock.config(text=curr_time)
               tt.config(text="CURRENT WEATHER")
               API_KEY = "b85966b8fc4d28c66f2717956a04a062"
               # weather
               api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat1}&lon={lon1}&appid={API_KEY}"

               json_data = requests.get(api).json()
               condition = json_data['weather'][0]['main']
               description = json_data['weather'][0]['description']
               temp = int(json_data['main']['temp']-273.15)
               pressure = json_data['main']['pressure']
               humidity = json_data['main']['humidity']
               wind = json_data['wind']['speed']

               # print(condition)
               t.config(text=(temp,"°"))
               c.config(text=(condition, "|", "FEELS","LIKE",temp,"°"))

               w.config(text=wind)
               h.config(text=humidity)
               d.config(text=description)
               p.config(text=pressure)
          except Exception as e:
               messagebox.showerror("Weather App MrFoxAK","Invalid Entry")

     # img = ImageTk.PhotoImage(Image.open("w.jpg"))
     # # reading the image
     # panel = tk.Label(root, image=img)

     # # setting the application
     # panel.pack(side="bottom", fill="both",
     #            expand="yes")


     # search box
     search_image = PhotoImage(file="search.png")
     # search_image.tk.call(search_image,'blank')
     myimg = Label(image=search_image)
     myimg.place(x=20, y=20)

     textfield = tk.Entry(root, justify="center", width=17, font=(
     "poppins", 25, "bold"),bg="#404040", border=0, fg="white")
     textfield.place(x=50, y=40)
     textfield.focus()

     search_icon = PhotoImage(file="search_icon.png")
     myimage_icon = Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
     myimage_icon.place(x=400,y=34)



     # logo
     logo_image = PhotoImage(file="logo.png")
     logo = Label(image=logo_image)
     logo.place(x=150,y=100)


     # time
     tt = Label(root,font=("arial",15,"bold"))
     tt.place(x=30,y=100)
     clock = Label(root,font=("Helvetica",20))
     clock.place(x=30,y=130)


     # bottom box
     frame_image = PhotoImage(file="box.png")
     frame_myimg = Label(image=frame_image)
     frame_myimg.pack(padx=5,pady=5,side=BOTTOM)

     # Label
     label1 = Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
     label1.place(x=120,y=400)

     label2 = Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
     label2.place(x=250,y=400)

     label3 = Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
     label3.place(x=430,y=400)

     label4 = Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
     label4.place(x=650,y=400)


     t=Label(font=("arial",70,"bold"),fg="#ee666d")
     t.place(x=400,y=150)
     c=Label(font=("arial",15,"bold"),fg="#ee666d")
     c.place(x=400,y=250)



     w=Label(text="....",font=("arial",15,"bold"),bg="#1ab5ef")
     w.place(x=120,y=430)

     h=Label(text="....",font=("arial",15,"bold"),bg="#1ab5ef")
     h.place(x=280,y=430)

     d=Label(text="....",font=("arial",15,"bold"),bg="#1ab5ef")
     d.place(x=450,y=430)

     p=Label(text="....",font=("arial",15,"bold"),bg="#1ab5ef")
     p.place(x=670,y=430)












     root.mainloop()

# myWeather()