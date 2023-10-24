#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status"""


import requests


if __name__ == '__main__':
    response = requests.get("https://intranet.hbtn.io/status")
    text = response.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
