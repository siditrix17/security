print'--------windows vulnerability scanner V+ 1.0--'
print'-------------\               /-----------+------------------'
print'---------------\           /---------------+------------------'
print'-----------------\       /-----------------+-----------------'
print'-------------------\   /-------------------+------------------'
print'---------------------x------------------+-----------------'
print'\n'
print'Hackr.io project work!'

#vulnerability scanner for finding flaws and weakness in pc

import socket
import psutil
import platform
import time
import sys

def gen_info():
 print'----------------------------------------------'
 print'GENERAL MACHINE INFO:-'
 print'machine:',platform.machine()
 print'platform:',platform.platform()
 print'system:',platform.system() 
 print'version no:',platform.version()
 print'processor:',platform.processor()
 time.sleep(2)


def proces():
 pro=psutil.pids()
 print"different process id's running are:-",pro
 print psutil.process_iter()
 print'list of all processes are:- \n'
 for p in psutil.process_iter():
   print p
 time.sleep(1)
 
 '''op=raw_input("wanna delete/terminate any program[y or n]:")
 if(op=='y'):
  op1=int(raw_input("enter pid of process to delete:"))
  op1.terminate()
 else:
  return
'''

def cpu_stats():
 print'printing stats about cpu times:\n'
 print'1)user time:\n2)system time: \n3)idle time:\n4)interrupt time:\n5)dpc   time:\n'
 for k in psutil.cpu_times():
   print k

def netwrk():
 print'network statistics: \n'
 for l in psutil.net_io_counters(pernic=True):
   print l
 print'\n'
 print"active network connections:\n"
 for kl in psutil.net_connections():
   print kl 

def port_sca():
    targetIP = socket.gethostname()

    print'Scanning all open ports please have patience:) : \n this may take few moments '
    for i in range(20, 65535):
       	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	result = s.connect_ex((targetIP, i))
   
	if(result == 0) :
            print '%d :open' % (i)
	    s.close()
     




gen_info()
time.sleep(4)
print'\n'
proces()
time.sleep(4)
print'\n'
cpu_stats()
time.sleep(4)
print'\n'
netwrk()
time.sleep(4)
print"\n"
port_sca()