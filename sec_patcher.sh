echo "ICMP request ignoring :"
echo "${yellow}Ignore ICMP Request ${reset}"
echo net.ipv4.icmp_echo_ignore_all = 1 >> /etc/sysctl.conf
echo "${yellow}Ignore Broadcast Request ${reset}"
echo net.ipv4.icmp_echo_ignore_broadcasts = 1 >> /etc/sysctl.conf
sysctl -p

#Preventing IP spoofing
echo "${yellow}Would you like to prevent IP spoofing? (This will reset you /etc/host.conf) (y/n)${reset}"
read foe
if [ "$foe" = "y" ]; then
echo order bind,hosts > /etc/host.conf
echo nospoof on >> /etc/host.conf
fi

#Specific System Security
echo "${yellow}Would you like to secure shared memory? Keep in mind that a reboot is required. (y/n)${reset}"
read fod
if [ "$fod" = "y" ]; then
echo "tmpfs /run/shm tmpfs defaults,noexec,nosuid 0 0" | sudo tee -a /etc/fstab
fi

#Log management
echo "${yellow}Would you like to copy all system logs in ./SystemLogs? (y/n)${reset}"
read foc
if [ "$foc" = "y" ]; then
mkdir SystemLogs
cp -a /var/log/. ./SystemLogs/
fi
