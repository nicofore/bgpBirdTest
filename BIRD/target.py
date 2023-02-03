import os
import socket
import netifaces as ni

ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
print(ip)



nbNeighbor = int(os.environ.get("NBNEIGHBOR"))
nbPrefix = int(os.environ.get("NBPREFIX"))

ipNeighbor = socket.gethostbyname("neighbor")
ipTarget = socket.gethostbyname("target")

with open("target.conf", "w") as f:
    
    #Write basic configuration

    f.write(
"""
router id """ + ip + """;

protocol device { }
protocol direct { disabled; }
protocol kernel { ipv4 { import none; export none; }; }

log stderr all;
#debug protocols all; # this seems to add a lot of extra load especially in internet/mrt tests

protocol bgp everything{
    local as 65000;
    #neighbor """ + ipNeighbor + """ as 65001;
    neighbor range 10.0.0.0/8 external;
    connect delay time 1;
    ipv4 {import all; export all; };
    #rs client;   
}"""
    )


    #start bird
    os.system("bird -c target.conf")


    #Get route with show route count

    #Write in file

    #Ask to cut the connection

    #Get route with show route count

    #Write in file

    #Stop the program

    
