#!/usr/bin/env python
from WumpusWorld import Wumpus
from optparse import OptionParser


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-s", "--size", dest="size", default=10, help="NxN size board")

    (options, args) = parser.parse_args()
    # Let's be reasonable here
    if options.size > 26:
        size = 26
    else:
        size = options.size
    Wumpus(size).game_loop()
