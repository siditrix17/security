import portkill
import portscan
import vul
import security_check
import rootkithunter
import ddos

def main():
  print'-----=linux vulnerability scanner=------- '
  vul.gen_info()
  portscan.portsca()
  portkill.portkil()
  security_check.lyni()
  print'implementing linux preventing measures from ddos..'
  ddos.ddos_preven()
  rootkithunter.rootkit() 
  print'Scanning of system complete !!'


if __name__=='__main__':
     main()  
