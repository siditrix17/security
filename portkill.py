#python version :2.7

import os
import time
import commands

def portkil():
 op=raw_input('wanna kill any port (y/n) :')
 if(op=='y'):
  os.system('pip install fuser')
  os.system('clear')
  print'--killing the ports--\n'
  print'info enter: 2 for killing two ports \n' 
  n=int(raw_input('Enter number of times to kill different ports :'))

  for i in range(0,n):
   print'\n'
   port_no=raw_input('Enter port no to kill :')
   print commands.getoutput('fuser -k -n tcp '+port_no)
   print'killing of port :'+port_no+' done!!'

  print'ALL PORTS KILLED!!!'
  time.sleep(2)
 else:
   print'ok!!cool Let them remain as it is '
   time.sleep(2)
 
