#! /usr/bin/env python3
import itertools
import time

import PlayOptions

from context import ditDahReader as dd

if __name__ == "__main__":
    po = PlayOptions.PlayOptions("Play random words from file")

    rt = dd.RandomTop100(po.wfile)
    words = rt.choice(po.n)

    m = dd.Morse(po.wpm, po.farns, po.hz)

    for word in words:
        for i in itertools.repeat(None, po.repeatN):
            time.sleep(0.5)
            m.play(word)
            time.sleep(0.5)
            print(word)
