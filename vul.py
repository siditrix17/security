print'--------linux  vulnerability scanner V+ 1.0--'
print'-------------\               /-----------+------------------'
print'---------------\           /---------------+------------------'
print'-----------------\       /-----------------+-----------------'
print'-------------------\   /-------------------+------------------'
print'---------------------x------------------+-----------------'
print'\n'


#vulnerability scanner for finding flaws and weakness in pc

import socket
import psutil
import platform
import time
import sys
import os

def gen_info():
 try :
  print'----------------------------------------------'
  print'GENERAL MACHINE INFO:-'
  print'machine:',platform.machine()
  print'platform:',platform.platform()
  print'system:',platform.system() 
  print'version no:',platform.version()
  print'processor:',platform.processor()
  time.sleep(2)

  os.system('pip install psutil')
  print'psutils required for scanning processes *'
  time.sleep(2)

  pro=psutil.pids()
  print"different process id's running are:-",pro
  print psutil.process_iter()
  print'list of all processes are:- \n'
  for p in psutil.process_iter():
    print p
  time.sleep(2)


  print'printing stats about cpu times:\n'
  print'1)user time:\n2)system time: \n3)idle time:\n4)interrupt time:\n'
  for k in psutil.cpu_times():
    print k
  time.sleep(1)

  print'network statistics: \n'
  for l in psutil.net_io_counters(pernic=True):
    print l
  time.sleep(1)
  print'\n'
  print"active network connections:\n"
  for kl in psutil.net_connections():
    print kl 
  time.sleep(2)

 except:
  print"general infomation couldn't be provided ...skipping it!!"




''' def port_sca():
    targetIP = socket.gethostname()

    print'Scanning all open ports please have patience:) : \n this may take few moments '
    for i in range(20, 65535):
       	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	result = s.connect_ex((targetIP, i) 
	if(result == 0) :
            print '%d :open' % (i)
	    s.close()
 '''    





