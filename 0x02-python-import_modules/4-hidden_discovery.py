#!/usr/bin/python3
import hidden_4


def disc():
    name = dir(hidden_4)
    for m in name:
        if m[:2] != '__':
            print("{:s}".format(m))


if __name__ == "__main__":
    disc()
