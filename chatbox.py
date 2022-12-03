from pyexpat import features
import pyttsx3
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)

def speak(audio):
     engine.say(audio)
     engine.runAndWait()

Hello = ('hello','hi','hii','hy','hey','hay','hai')

reply_Hello = ('Hello Sir , I am Sunday .',"Hey, What's Up","Hey how are you?","Hello Sir, Nice to meet you again","Of Course Sir, Hello","Hello Sir I'm Sunday")

Bye = ('bye','exit','sleep','go')

reply_Bye = ('Bye Sir',"It's Okay","Bye","Thanks","Ok Sir Bye","It will Be Nice to meet you Sir")

How_are_you = ('how are you','are you ok','are you fine')

reply_How = ("I am Fine Sir, what about you Sir?","Excellent Sir","Moj ho rhi hai Sir","Absolutely Fine Sir","I'm Fine","Thanks For asking Sir, I'm well")

nice = ('nice','good','well done')

reply_nice = ('Thanks',"Ohh It's Okay","ALl Thanks to you Sir")

Functions = ('functions','ability','abilities','what can you do','features')

reply_Functtion = ("I can Perform many task or varietis of task , how can i help you sir? ","I can call your G.F .","I can message your mom that you are studing","Let me ask first , How Can I help you?","I can trun on the light of your room","I can shutdown The computer ","I can message in whatsApp whatever you want")

Sorry_reply = ("Sorry, That's beyond My Abilites .","Sorry , I can't do that","Sorry , That's Above me")



def chatBox(text):
     Text = str(text)

     for word in Text.split():
          if word in Hello:
               reply = random.choice(reply_Hello)

               speak(reply)

          elif word in Bye:
               reply = random.choice(reply_Bye)

               speak(reply)

          elif word in How_are_you:
               reply = random.choice(reply_How)

               speak(reply)

          elif word in nice:
               reply = random.choice(reply_nice)

               speak(reply)

          elif word in Functions:
               reply = random.choice(reply_Functtion)

               speak(reply)

          # else:
          #      return random.choice(Sorry_reply)


# v = chatBox('hello')
# print(v)