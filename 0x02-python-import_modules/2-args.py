#!/usr/bin/python3

import sys

if len(sys.argv) == 1:
    print("{} arguments.".format(0))

else:
    lens = len(sys.argv)
    argv = sys.argv

    print("{} arguments:".format(lens - 1))
    for i in range(1, lens):
        print("{}: {}".format(i, argv[i]))
