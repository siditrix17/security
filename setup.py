import os
try:
 os.system('pip install psutil')
 os.system('apt-get install rkhunter')
 os.system('apt-get install lynis')
except:
 print'installation failed!! try again'
