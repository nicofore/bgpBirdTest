import os
import socket
import netaddr
import netifaces as ni

ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
print(ip)

it = netaddr.iter_iprange('100.0.0.0','160.0.0.0')


nbNeighbor = int(os.environ.get("NBNEIGHBOR"))
nbPrefix = int(os.environ.get("NBPREFIX"))

ipNeighbor = socket.gethostbyname("neighbor")
ipTarget = socket.gethostbyname("target")
if (ip[-1] == "3"):
    ipTarget = ipTarget[0:-1] + "6"
else:
    ipTarget = ipTarget[0:-1] + "3"


with open("neighbor.conf", "w") as f:
    
    #Write basic configuration

    f.write(
"""
router id """ + ip + """;

debug protocols {states};
protocol device {}

protocol bgp {
    #hold time 5;
    source address """ + ip + """;
    connect delay time 1;
    interface "eth0";
    strict bind;
    ipv4 { import none; export all; };
    local """ + ip + """ as 65001;
    neighbor """ + ipTarget + """ as 65000;
    #neighbor target as 65000;
    #neighbor range 10.0.0.0/8 external;
}
"""
    )

    #Write prefixes
    f.write("protocol static {ipv4;\n")

    for i in range(nbPrefix):
        f.write("route " + str(next(it)) + "/32 via " + ip + ";\n")

    f.write("}")


#Start bird
os.system("bird -c neighbor.conf")

