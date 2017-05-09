import getopt
import random
import sys
import time

from .Morse import *


class RandomTop100:
    def __init__(self, wfile="data/100words.txt"):
        self.words = [word.strip() for line in open(wfile, 'r')
                      for word in line.split()]

    def choice(self, n=20):
        return random.choices(self.words, k=n)
