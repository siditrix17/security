import os

def rootkit():
 try:
  print'rootkit scanner(scanning for rootkits,trojans,malicious files)'
  print'downloading required rootkit (clamav)'
  os.system('apt-get install rkhunter')
  os.system('rkhunter -c')
  print'DONE!!!!!!'
  os.system('chmod +x sec_patcher.sh')
  os.system('./sec_patcher.sh')
  print'ALL Scans completed!'
 except:
  print"rootkithunter couldn't be initiated due to an error ,\n.skiiping it!!"
