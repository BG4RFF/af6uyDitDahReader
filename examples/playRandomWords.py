#! /usr/bin/env python3
import getopt
import sys
import time

import numpy as np

from context import ditDahReader as dd

if __name__ == "__main__":
    wfile = "data/100words.txt"
    n = 20
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:n:", ["help", "infile="])
    except:
        print('playRandomWords.py -i words100.txt -n 20')
        print('  Use file words100.txt and play 20 of words at random')
        sys.exit()
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('playRandomWords.py -i words100.txt -n 20')
            print('  Use file words100.txt and play 20 of words at random')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            wfile = arg
        elif opt in ("-n"):
            n = int(arg)

    rt = dd.RandomTop100(wfile)
    words = rt.choice(n)

    m = dd.Morse()

    for word in words:
        m.play(word)
        time.sleep(1)
        print(word + '\n')
