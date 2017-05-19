#! /usr/bin/env python3
import itertools
import time

import PlayOptions

import numpy as np

from context import ditDahReader as dd

if __name__ == "__main__":
    po = PlayOptions.PlayOptions("Play the file")

    m = dd.Morse(po.wpm, po.farns, po.hz)

    for line in open(po.wfile, 'r'):
        for i in itertools.repeat(None, po.repeatN):
            time.sleep(0.5)
            m.play(line)
            time.sleep(0.5)
            print(line, end='')
