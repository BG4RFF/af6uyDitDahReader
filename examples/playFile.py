#! /usr/bin/env python3
import getopt
import itertools
import sys
import time

import numpy as np

from context import ditDahReader as dd

if __name__ == "__main__":
    wfile = "data/2-grams-1-to-50.txt"
    n = 20
    wpm = 30.0
    farns = 30.0
    repeatN = 1
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:w:f:n:r:",
                                   ["help",
                                    "infile=",
                                    "wpm=",
                                    "farnsworth=",
                                    "nwords=",
                                    "repeat="])
    except:
        print('playFile.py -i words100.txt -n 20')
        print('  Use file 2-grams-1-to-50.txt and play 20 of words at random')
        sys.exit()
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('playFile.py -i 2-grams-1-to-50.txt -n 20')
            print('  Use file words100.txt and play 20 of words at random')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            wfile = arg
        elif opt in ("-w", "--wpm"):
            wpm = float(arg)
        elif opt in ("-f", "--farnsworth"):
            farns = float(arg)
        elif opt in ("-n", "--nwords"):
            n = int(arg)
        elif opt in ("-r", "--repeat"):
            repeatN = int(arg)

    words = [word.strip() for line in open(wfile, 'r')
             for word in line.split()]

    m = dd.Morse(wpm, farns)

    for word in words:
        for i in itertools.repeat(None, repeatN):
            time.sleep(0.5)
            m.play(word)
            time.sleep(0.5)
            print(word)
