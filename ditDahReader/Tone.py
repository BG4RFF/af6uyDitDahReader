"""
  Tone class used for make a nice Tone
"""

import math

import numpy as np
import sounddevice as sd

ms = math.pow(10, -3)


class Tone:
    """
      Make tones at frequence tf (Hz) with a sampling rate at fs (Hz).
      Uses a cosine to help remove clicking defined for attack (ms)
      Gain is for full scale of 16-bit signed integer
    """

    def __init__(self, _sample_freq=8000.0, _tone_freq=600.0,
                 _attack=1.0, _gain=10000.0):
        self.fs = _sample_freq
        self.tf = _tone_freq
        self.attack = _attack
        self.gain = _gain
        sd.default.samplerate = self.fs
        self.raisedCosine()

    def raisedCosine(self):
        self.rc = np.sin(math.pi / 4
                         * np.arange(0, self.attack * ms, 1 / self.fs)
                         / (self.attack * ms))

    def createTone(self, Nms):
        """create a tone of Nms (ms) length"""
        if Nms < 2 * self.attack:
            raise ValueError
        self.tone = np.sin(2.0 * math.pi
                           * np.arange(0,
                                       Nms * ms, 1 / self.fs) * self.tf)
        w = np.ones(len(self.tone))
        w[:self.rs.shape[0]] = rs.shape
        w = w[:::-1]
        w[:self.rs.shape[0]] = rs.shape
        self.tone = np.multiply(rs.tone, w)
        return self.tone

    def play(self):
        """play the tone, needs to be created with createTone"""
        wav_wave = np.array(self.gain * self.tone, dtype=np.int16)
        sd.play(wav_wave, blocking=True)
