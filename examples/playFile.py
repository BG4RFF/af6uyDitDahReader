#! /usr/bin/env python3
import itertools
import time

import PlayOptions

import numpy as np

from context import ditDahReader as dd

if __name__ == "__main__":
    po = PlayOptions.PlayOptions("Play the file")

    words = [word.strip() for line in open(po.wfile, 'r')
             for word in line.split()]

    m = dd.Morse(po.wpm, po.farns, po.hz)

    for word in words:
        for i in itertools.repeat(None, po.repeatN):
            time.sleep(0.5)
            m.play(word)
            time.sleep(0.5)
            print(word)
