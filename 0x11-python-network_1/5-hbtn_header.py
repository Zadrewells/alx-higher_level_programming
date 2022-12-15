#!/usr/bin/python3
"""displays the value of the variable X-Request-Id in the response header"""
import requests
import sys

if __name__ == "__main__":
    data = requests.get(sys.argv[1])
    print(data.headers.get("X-Request-Id"))
