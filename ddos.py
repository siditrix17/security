import commands

commands.getoutput('iptables -t mangle -A PREROUTING -p tcp --tcp-flags FIN,SYN,RST,PSH,ACK,URG NONE -j DROP')
commands.getoutput('iptables -t mangle -A PREROUTING -p tcp -m conntrack --ctstate NEW -m tcpmss ! --mss 536:65535 -j DROP')
commands.getoutput('iptables -t mangle -A PREROUTING -p tcp ! --syn -m conntrac --ctstate NEW -j DROP')
print'DONE!!'