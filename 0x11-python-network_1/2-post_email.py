#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    email = sys.argv[2]
    url = sys.argv[1]
    data = urllib.parse.urlencode({"email": email}).encode('utf-8')
    with urllib.request.urlopen(url, data) as response:
        page = response.read().decode('utf-8')
        print(page)
