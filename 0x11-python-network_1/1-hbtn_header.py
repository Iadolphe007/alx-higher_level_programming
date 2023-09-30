#!/usr/bin/python3
"""python script that takes in URL"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        request_id = headers.get('X-Request-Id')
        print(request_id)
