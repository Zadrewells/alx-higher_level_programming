#!/usr/bin/python3
""" code to fetch data """
from urllib import request

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    with request.urlopen(url) as response:
        print("Body response:")
        page = response.read()
        data = '\t- type: {}\n\t- content: {}\n\t- utf8 content: {}'
        print(data.format(type(page), page, page.decode('UTF-8')))
