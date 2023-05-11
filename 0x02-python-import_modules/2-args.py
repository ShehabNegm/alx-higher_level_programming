#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    if len(sys.argv) == 1:
        print("{} arguments.".format(0))

    elif len(sys.argv) == 2:
        print("{} argument:".format(1))
        print("{}: {}".format(1, sys.argv[1]))

    else:
        lens = len(sys.argv)
        argv = sys.argv

        print("{} arguments:".format(lens - 1))
        for i in range(1, lens):
            print("{}: {}".format(i, argv[i]))
