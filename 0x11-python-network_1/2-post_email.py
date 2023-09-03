#!/usr/bin/python3
"""use urllib"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv

if __name__ == "__main__":

    url = argv[1]
    parm = {"email": argv[2]}
    data = urlencode(parm)
    data = data.encode('ascii')
    req = Request(url, data)
    with urlopen(req) as res:
        html = res.read()
        print(html.decode("utf-8"))
