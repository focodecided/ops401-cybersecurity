#!/usr/bin/env python3

# Script Name: Create NMAP using Scapy
# Author: Festus Oguhebe Jr. 
# Purpose: Scan Network using Scapy


# In Python, create a TCP Port Range Scanner that tests whether a TCP port is open or closed. The script must: Utilize the scapy library
# Define host IP 
# Define port range or specific set of ports to scan
# Test each port in the specified range using a for loop
# If flag 0x12 received, send a RST packet to graciously close the open connection. Notify the user the port is open.
# If flag 0x14 received, notify user the port is closed.
# If no flag is received, notify the user the port is filtered and silently dropped.

import sys
from scapy.all import sr1, IP, TCP, send
import random

# Set the target host IP address and the range of ports to scan.
host = 'scanme.nmap.org'  # Target host for scanning
port_range = [20, 21, 22, 23, 53, 69, 80, 123, 179, 264, 443, 520]  # Target port range

# Define a function to scan a single port.
def scan_port(host, dst_port):
    # Randomly select a source port to use for sending packets.
    src_port = random.randint(1024, 65535)
    # Craft a TCP SYN packet with the random source port and the destination port.
    response = sr1(IP(dst=host)/TCP(sport=src_port, dport=dst_port, flags="S"), timeout=1, verbose=0)
    # If no response is received, assume the port is filtered.
    if response is None:
        print(f"Port {dst_port} is filtered and silently dropped")
    # If a response is received, check if it's a TCP packet with certain flags.
    elif response.haslayer(TCP):
        # If the TCP flags indicate a SYN-ACK, the port is open.
        if response.getlayer(TCP).flags == 0x12:
            # Send a TCP RST packet to close the connection gracefully.
            send(IP(dst=host)/TCP(sport=src_port, dport=dst_port, flags="R"), verbose=0)
            print(f"Port {dst_port} is open")
        # If the TCP flags indicate a RST, the port is closed.
        elif response.getlayer(TCP).flags == 0x14:
            print(f"Port {dst_port} is closed")

# Iterate over the range of ports and scan each one using the function defined above.
for port in port_range:
    scan_port(host, port)