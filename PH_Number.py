from phonenumbers import timezone, carrier,geocoder
import phonenumbers
import scipy as sp
from k2 import speak


def PH_num():
     speak("Please Enter the Phone number Sir!!")

     num = input("Enter Your No. with +__ : ")
     try:
          phone = phonenumbers.parse(num)

          valid = phonenumbers.is_valid_number(phone)

          if valid:
               time = timezone.time_zones_for_number(phone)
               car = carrier.name_for_number(phone,"en")
               reg = geocoder.description_for_number(phone,"en")
               # print(time)
               speak(f"It's from {time}")
               # print(car)
               speak(f"It's a {car} Sim")
               # print(reg)
               speak(f"registration is {reg}")
          else:
               # print("Not valid\n")
               speak("It's Not a valid phone num Sir, Please give a valid phone number and try again")
     except Exception as ep:
          print(ep)























