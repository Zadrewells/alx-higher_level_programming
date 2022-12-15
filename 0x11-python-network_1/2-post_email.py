#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""

import sys
from urllib import request, parse

if __name__ == "__main__":
    if len(sys.argv) == 3:
        url = sys.argv[1]
        data = {"email": sys.argv[2]}
        data = parse.urlencode(data).encode('ascii')
        with request.urlopen(url, data) as r:
            response = r.read()
            print(response.decode('UTF-8'))
