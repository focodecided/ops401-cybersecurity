import sys
from scapy.all import sr1, IP, TCP, send
import random
import logging

# Configure logging to file
logging.basicConfig(filename='network_scan.log',
                    filemode='w',  # Overwrite the log file if it exists
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Set the target host IP address and the range of ports to scan.
host = 'scanme.nmap.org'  # Target host for scanning
port_range = [20, 21, 22, 23, 53, 69, 80, 123, 179, 264, 443, 520]  # Target port range

# Define a function to scan a single port.
def scan_port(host, dst_port):
    try:
        # Randomly select a source port to use for sending packets.
        src_port = random.randint(1024, 65535)
        # Craft a TCP SYN packet with the random source port and the destination port.
        response = sr1(IP(dst=host)/TCP(sport=src_port, dport=dst_port, flags="S"), timeout=1, verbose=0)
        # If no response is received, assume the port is filtered.
        if response is None:
            logging.warning(f"Port {dst_port} is filtered and silently dropped")
            print(f"Port {dst_port} is filtered and silently dropped")
        # If a response is received, check if it's a TCP packet with certain flags.
        elif response.haslayer(TCP):
            # If the TCP flags indicate a SYN-ACK, the port is open.
            if response.getlayer(TCP).flags == 0x12:
                # Send a TCP RST packet to close the connection gracefully.
                send(IP(dst=host)/TCP(sport=src_port, dport=dst_port, flags="R"), verbose=0)
                logging.info(f"Port {dst_port} is open")
                print(f"Port {dst_port} is open")
            # If the TCP flags indicate a RST, the port is closed.
            elif response.getlayer(TCP).flags == 0x14:
                logging.info(f"Port {dst_port} is closed")
                print(f"Port {dst_port} is closed")
    except Exception as e:
        logging.error(f"Error scanning port {dst_port}: {e}")
        print(f"Error scanning port {dst_port}")

# Iterate over the range of ports and scan each one using the function defined above.
for port in port_range:
    scan_port(host, port)

logging.info("Port scanning completed.")
