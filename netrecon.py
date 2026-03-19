import socket 
import subprocess
import sys
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
    

#Testing(uncomment to test)
#ip = "scanme.nmap.org"  #a legal safe test plaec
#for port in commonPorts:
#    if portScan(ip, port):
#        print(f"[Open] {ip}:{port}")