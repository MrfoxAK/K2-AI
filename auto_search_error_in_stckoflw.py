from subprocess import Popen , PIPE
import requests

def execute_return(cmd):
    args = cmd.split()
    proc = Popen(args, stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()
    return out, err


def req(err):
     resp = requests.get("https://api.stackexchange.com/"+"/2.3/search?order=desc&sort=activity&tagged=python&intitle={}&site=stackoverflow".format(err))
     return resp.json()

def get_url(js_dict):
     url_l = []
     c=0
     for i in js_dict["items"]:
          if i["is_answered"]:
               url_l.append(i["link"])
          c+=1
          if c==3 or c ==len(i):
               break
     import webbrowser
     for i in url_l:
          webbrowser.open(i)

if __name__ == "__main__":
     op , err = execute_return("python test.py")
     # print(err)
     error_msg = err.decode("utf-8").strip().split("\r\n")[-1]
     print(error_msg)
     if error_msg:
          filter_err = error_msg.split(":")
          js1 = req(filter_err[0])
          js2 = req(filter_err[1])
          js = req(error_msg)
          get_url(js1)
          get_url(js2)
          get_url(js)
     else:
          print("No Error")













