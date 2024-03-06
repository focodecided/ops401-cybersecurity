#!/usr/bin/env python3

# The below Python script shows one possible method to return the cookie from a site that supports cookies.

import requests
import webbrowser
import os

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

    # Send the cookies back to the site and receive a HTTP response
    response_with_cookies = requests.get(target_site, cookies=cookies.get_dict())

    # Generate a .html file to capture the contents of the HTTP response
    html_filename = "response_with_cookies.html"
    with open(html_filename, "w") as file:
        file.write(response_with_cookies.text)

    # Open the HTML file with the default web browser
    webbrowser.open('file://' + os.path.realpath(html_filename))

target_site = "http://www.whatarecookies.com/cookietest.asp"
fetch_and_resend_cookies(target_site)