if [[ $1 = "clean" ]]; then
    iptables -F FORWARD
    iptables -F INPUT
    iptables -F OUTPUT
    iptables -P FORWARD ACCEPT
    iptables -P INPUT ACCEPT
    iptables -P OUTPUT ACCEPT
else
    # Remove previous rules && default deny.
    iptables -F OUTPUT
    iptables -P OUTPUT DROP

    # Allow SSH only externally initiated for management.
    iptables -A INPUT -i eth0 -p tcp --dport 22 -m state --state NEW,ESTABLISHED -j ACCEPT
    iptables -A OUTPUT -o eth0 -p tcp --sport 22 -m state --state ESTABLISHED -j ACCEPT

    # Only debian-tor && loopback.
    iptables -A OUTPUT -j ACCEPT -m owner --uid-owner debian-tor
    iptables -A OUTPUT -j ACCEPT -o lo
    iptables -A OUTPUT -j ACCEPT -p udp --dport 123
fi

iptables -L -v
