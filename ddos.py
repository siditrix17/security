import commands
import time

def ddos_preven():
 time.sleep(2)
 print'Blocking packets with Bogus tCp Flags :'
 commands.getoutput('iptables -t mangle -A PREROUTING -p tcp --tcp-flags FIN,SYN ,RST,PSH,ACK,URG NONE -j DROP')
 commands.getoutput('iptables -t mangle -A PREROUTING -p tcp -m conntrack --ctst ate NEW -m tcpmss ! --mss 536:65535 -j DROP')
 commands.getoutput('iptables -t mangle -A PREROUTING -p tcp ! --syn -m conntrac --ctstate NEW -j DROP')
 commands.getoutput('iptables -t mangle -A PREROUTING -p tcp --tcp-flags FIN,SYN ,RST,PSH,ACK,URG NONE -j DROP')
 commands.getoutput('iptables -t mangle -A PREROUTING -p tcp --tcp-flags SYN,RST  SYN,RST -j DROP')
 commands.getoutput('iptables -t mangle -A PREROUTING -p tcp --tcp-flags FIN,RST  FIN,RST -j DROP')
 commands.getoutput('iptables -t mangle -A PREROUTING -p tcp --tcp-flags FIN,ACK  FIN -j DROP')
 commands.getoutput('iptables -t mangle -A PREROUTING -p tcp --tcp-flags ACK,URG  URG -j DROP')
 commands.getoutput('iptables -t mangle -A PREROUTING -p tcp --tcp-flags ACK,FIN  FIN -j DROP')
 commands.getoutput('iptables -t mangle -A PREROUTING -p tcp --tcp-flags ACK,PSH  PSH -j DROP')
 commands.getoutput('iptables -t mangle -A PREROUTING -p tcp --tcp-flags ALL ALL  -j DROP')
 commands.getoutput('iptables -t mangle -A PREROUTING -p tcp --tcp-flags ALL NON  E -j DROP')
 commands.getoutput('iptables -t mangle -A PREROUTING -p tcp --tcp-flags ALL FIN ,PSH,URG -j DROP')
 commands.getoutput('iptables -t mangle -A PREROUTING -p tcp --tcp-flags ALL SYN ,FIN,PSH,URG -j DROP')
 commands.getoutput('iptables -t mangle -A PREROUTING -p tcp --tcp-flags ALL SYN ,RST,ACK,FIN,URG -j DROP')
 
 print'Done!!'
 time.sleep(2)
 print'Blocking packets from private subnets :'
 
 commands.getoutput('iptables -t mangle -A PREROUTING -s 224.0.0.0/3 -j DROP ')
 commands.getoutput('iptables -t mangle -A PREROUTING -s 169.254.0.0/16 -j DROP' )
 commands.getoutput('iptables -t mangle -A PREROUTING -s 192.0.2.0/24 -j DROP')
 commands.getoutput('iptables -t mangle -A PREROUTING -s 192.168.0.0/16 -j DROP' )
 commands.getoutput('iptables -t mangle -A PREROUTING -s 240.0.0.0/5 -j DROP')
 commands.getoutput('iptables -t mangle -A PREROUTING -s 127.0.0.0/8 ! -i lo -j  DROP')
 print'DONE!!!!'
 commands.getoutput('iptables -t mangle -A PREROUTING -p icmp -j DROP')
 commands.getoutput('iptables -A INPUT -p tcp -m connlimit --connlimit-above 80  -j REJECT --reject-with tcp-reset')
 commands.getoutput('iptables -A INPUT -p tcp -m conntrack --ctstate NEW -m limi t --limit 60/s --limit-burst 20 -j ACCEPT')
 commands.getoutput('iptables -A INPUT -p tcp -m conntrack --ctstate NEW -j DROP ')
 commands.getoutput('iptables -t mangle -A PREROUTING -f -j DROP')
 commands.getoutput('iptables -A INPUT -p tcp --tcp-flags RST RST -m limit --lim it 2/s --limit-burst 2 -j ACCEPT')
 commands.getoutput('iptables -A INPUT -p tcp --tcp-flags RST RST -j DROP')


