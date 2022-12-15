#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import requests

data = requests.get("https://alx-intranet.hbtn.io/status")
print("Body response:")
print("\t- type: {}".format(type(data.text)))
print("\t- content: {}".format(data.text))
