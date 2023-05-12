#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    lens = len(sys.argv)
    argv = sys.argv
    sum = 0

    if lens == 1:
        print("{}".format(lens - 1))

    else:
        for i in range(1, lens):
            sum += int(argv[i])

        print("{}".format(sum))
