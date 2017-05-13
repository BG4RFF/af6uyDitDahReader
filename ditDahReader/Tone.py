"""
  Tone class used for make a nice Tone
"""

import math

import numpy as np

from .Play import *

ms = math.pow(10, -3)


class Tone:
    """
      Make tones at frequence tf (Hz) with a sampling rate at fs (Hz).
      Uses a cosine to help remove clicking defined for attack (ms)
      Gain is for full scale of 16-bit signed integer
    """

    def __init__(self, _sample_freq=8000.0, _tone_freq=600.0,
                 _attack=15.0, _gain=10000.0):
        self.fs = _sample_freq
        self.tf = _tone_freq
        self.attack = _attack
        self.gain = _gain
        self.raisedCosine()
        self.p = Play(_sample_freq)

    def raisedCosine(self):
        self.rc = (1 + np.cos(np.arange(-math.pi,
                                        0,
                                        math.pi / (self.attack * ms
                                                   * self.fs)))) * .5

    def createTone(self, Nms):
        """create a tone of Nms (ms) length"""
        if Nms < 2 * self.attack:
            raise ValueError
        self.tone = np.sin(2.0 * math.pi
                           * np.arange(0,
                                       Nms * ms, 1 / self.fs) * self.tf)
        w = np.ones(len(self.tone))
        w[:self.rc.shape[0]] = self.rc
        w = np.flip(w, 0)
        w[:self.rc.shape[0]] = self.rc
        self.tone = np.multiply(self.tone, w)
        return self.tone

    def play(self):
        """play the tone, needs to be created with createTone"""
        p.play(self.tone, self.gain)
