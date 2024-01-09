#!/usr/bin/env python3

# First, I need to import the libraries I need for the script.
import ping3 # Ping3 is a simple library that can send ICMP packets
import time # This library is used to create delays not give time.
import datetime # This library generates timestamp with the date.

# LET'S START

destination_ip = '8.8.8.8'
check_status(destination_ip)

# 1. Define the function. We'll call our function "check_status" and the argument we call "destination_ip"
def check_status(destination_ip) # Now we do a while loop that will run this function and give us a response
    while True:
        response = ping3.ping(destination_ip, timeout=1, unit="s") #This uses the ping3 library to ping the ip address held in the variable "destination_ip" and then waits 1 second before showing a response. The "response" variable stores the response.
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if response is not None:
            status = "Network Active"
        else:
            status = "Network Inactive"
            
        print(f"{timestamp} {status} to {destination_ip}") # 'f' before a string literal indicates an f-string. F-strings are a way to format strings that allows for easy embedding of variables and expressions within the string.
        time.sleep(2) # Wait 2 seconds before sending the next ICMP packet