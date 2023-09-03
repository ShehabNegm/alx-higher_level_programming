#!/usr/bin/python3
"""use urllib"""
from urllib.request import urlopen
from sys import argv

if __name__ == "__main__":
    with urlopen(argv[1]) as res:
        print(res.headers["X-Request-Id"])
