#python version :2.7

import commands

print'--killing the ports--\n'
print'info enter: 2 for killing two ports \n' 
n=int(raw_input('Enter number of times to kill different ports :'))

for i in range(0,n):
 print'\n'
 port_no=raw_input('Enter port no to kill :')
 print commands.getoutput('fuser -k -n tcp '+port_no)
 print'killing of port :'+port_no+' done!!'

print'ALL PORTS KILLED!!!'
