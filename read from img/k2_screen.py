import pytesseract
from PIL import Image
from k2 import speak

def k2_ss():
     pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"


     img = Image.open("C:\\Users\\AKASH\\OneDrive\\Desktop\\K2\\img\\t.png")


     text = pytesseract.image_to_string(img)

     # print(text)

     speak("Ok sir! i read what ever i see in your screen ")
     speak("it's written on your screen that ")

     speak(text)


