#!/usr/bin/python3

if __name__ == "__main__":

    import hidden_4

    hidden = dir(hidden_4)

    for i in dir(hidden):
        if i[0] and i[1] != "_":
            print("{}".format(i))
