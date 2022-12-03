import datetime
import winsound

def alarm(timing):
     altime = str(datetime.datetime.now().strftime(timing,"%I:%M %p"))

     altime = altime[11:-3]

     h=altime[:2]
     h=int(h)
     m=altime[3:5]
     m=int(m)

     print(f"Done, alarm is set for {timing}")


     while True:
          if h==datetime.datetime.now().hour:
               if m==datetime.datetime.now().minute:
                    print("alarm is running")
                    winsound.PlaySound('abc',winsound.SND_LOOP)

          elif m<datetime.datetime.now().minute:
               break


if __name__ == "__main__":
     alarm('20:5 PM')













