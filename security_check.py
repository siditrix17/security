#import subprocess
import os
os.system("apt-get install lynis") #those who don't have lynis
os.system("lynis -c -Q")
#subprocess.call("lynis -c -Q")

