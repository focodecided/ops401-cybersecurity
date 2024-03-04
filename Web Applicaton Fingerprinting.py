#!/usr/bin/env python3

# Script Name: Web Application Fingerprinting
# Author: Festus Oguhebe Jr. 
# Purpose: Banner grabbing, also known as “service fingerprinting,” is a way to check if your target computer supports specific services. This is useful when gathering intelligence on a target such as a web server.

import subprocess

def grab_banner_netcat(ip, port):
    try:
        result = subprocess.check_output(f"echo | nc {ip} {port}", shell=True, stderr=subprocess.STDOUT)
        print(f"Netcat banner grabbing result on {ip}:{port}:\n{result.decode()}")
    except subprocess.CalledProcessError as e:
        print(f"Error during Netcat banner grabbing: {e.output.decode()}")

def grab_banner_telnet(ip, port):
    try:
        result = subprocess.check_output(f"echo | telnet {ip} {port}", shell=True, stderr=subprocess.STDOUT, timeout=10)
        print(f"Telnet banner grabbing result on {ip}:{port}:\n{result.decode()}")
    except subprocess.CalledProcessError as e:
        print(f"Error during Telnet banner grabbing: {e.output.decode()}")
    except subprocess.TimeoutExpired:
        print("Telnet connection timed out.")

def grab_banner_nmap(ip):
    try:
        result = subprocess.check_output(f"nmap -sV {ip}", shell=True, stderr=subprocess.STDOUT)
        print(f"Nmap banner grabbing result on {ip} (well-known ports):\n{result.decode()}")
    except subprocess.CalledProcessError as e:
        print(f"Error during Nmap banner grabbing: {e.output.decode()}")

def main():
    ip = input("Enter a URL or IP address: ")
    port = input("Enter a port number: ")

    print("\nPerforming banner grabbing with Netcat...")
    grab_banner_netcat(ip, port)

    print("\nPerforming banner grabbing with Telnet...")
    grab_banner_telnet(ip, port)

    print("\nPerforming banner grabbing with Nmap...")
    grab_banner_nmap(ip)

if __name__ == "__main__":
    main()
