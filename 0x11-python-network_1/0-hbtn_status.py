#!/usr/bin/python3
"""use urllib"""
from urllib.request import urlopen
from pprint import pprint

if __name__ == "__main__":
    with urlopen("https://alx-intranet.hbtn.io/status") as res:
        html = res.read()
        print("Body response:")
        print("\t - type: {}".format(type(html)))
        print("\t - content: {}".format(html))
        print("\t - utf8 content: {}".format(html.decode("utf-8")))
