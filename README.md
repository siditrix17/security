# linux vulnerability scanner
hackr.io project work (Linux based vulnerability scanner and patcher)
This a python 2.7 based vulnerability scanner and ddos patcher . It provides general low level machine information 
It uses lynis and clamAV opensource scanners as well .

before running main file (vulscanner.py) , few installations need to be made . 
This installations are pre-build in project but separate installation will ensure proper working.

MODULES USED :   (project implemented in python 2.7)
commands,
os,
time,
socket,
subprocess, 
sys,
psutil (pip install psutil),
platform.

PACKAGES USED :
rkhunter(apt-get install rkhunter),
lynis(apt-get install lynis)

if setup.py fails to download ,check installation settings or manaully install them using above commands.

process of using :- 1) setup.py 2)vulscanner.py 
