import pywhatkit as pw
from k2 import speak

def handwritten():

     speak("Ok Sir please give me the text: ")

     txt = input("Enter the text: ")

     pw.text_to_handwriting(txt,"demo.png",[0,0,138])

     print("  END  ")

# handwritten()