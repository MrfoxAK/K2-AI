import moviepy.editor
from tkinter.filedialog import *
from k2 import speak

def vd_2_au():
     speak("Ok Sir! Please select the video")
     vid = askopenfilename()

     video = moviepy.editor.VideoFileClip(vid)
     speak("Converting in process. Please wait Sir")
     audio = video.audio

     audio.write_audiofile("C:\\Users\\AKASH\\OneDrive\\Desktop\\K2\\audioFile\\demo.mp3")


     speak("Converting Done Sir, Please check it out")













