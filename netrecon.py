import socket 
import subprocess
import sys
import ipaddress
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# common ports as searched online

commonPorts = [
    21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3306, 8080 
]

def portScan(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        sock.close()

        if result == 0:
            return True
        return False
    except Exception:
        return False
    
#if on windows use -n | linux -c

def pingHost(ip):
    try:
        socket.setdefaulttimeout(1)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((str(ip), 80))
        s.close()
        return True
    except Exception:
        return False
    
def discoverHost(network):
    print(f"\n[*] Scanning network: {network}")
    net = ipaddress.ip_network(network, strict=False)
    alive = []

    with ThreadPoolExecutor(max_workers=100) as ex:
        futures = {ex.submit(pingHost, str(ip)): str(ip) for ip in net.hosts()}
        for future in as_completed(futures):
            ip = futures[future]
            if future.result():
                print(f" [+] {ip} is UP")
                alive.append(ip)

    print(f"\n[*] {len(alive)} host(s) found.")
    return sorted(alive)

# Testing v2
#discoverHost("192.168.68.0/24")

#Testing 
#ip = "scanme.nmap.org"  #a legal safe test plaec
#for port in commonPorts:
#    if portScan(ip, port):
#        print(f"[Open] {ip}:{port}")