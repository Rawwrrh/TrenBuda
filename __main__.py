#!/usr/bin/env python3
import sys

from src import Metro, Train


def getArgs():
    if len(sys.argv) < 3:
        raise Exception("usage: <file.json?> <origin> <destination> <color?>")

    # filename origin destination color?
    if ".json" in sys.argv[1]:
        if len(sys.argv) < 5:
            return (sys.argv[1], sys.argv[2], sys.argv[3], None)
        return (sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

    # origin destination
    if len(sys.argv) < 4:
        return (None, sys.argv[1], sys.argv[2], None)

    # origin destination color
    if len(sys.argv) >= 4:
        return (None, sys.argv[1], sys.argv[2], sys.argv[3])


def main():
    try:
        filename, origin, destination, color = getArgs()
        metro = Metro.fromJson(filename)
        train = Train.new(metro).color(color).origin(origin).to(destination).travel()

        print(train)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
