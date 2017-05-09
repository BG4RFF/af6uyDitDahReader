import math
import re

from .morse_dict import *
from .Tone import *


class Morse:

    def setWPM(self, _wpm, _farnsworth=-1.0):
        if _farnsworth > _wpm or _farnsworth <= 0.0:
            _farnsworth = _wpm
        self.wpm = _wpm
        # paris is 50 dits (word used to define a word)
        _paris = 50.0
        self.dit = self.ms_per_min / (_paris * self.wpm)
        self.dah = 3.0 * self.dit
        self.dit_farns = self.ms_per_min / (_paris * _farnsworth)
        self.element_space = self.dit
        self.char_space = self.dit_farns * 3.0
        self.word_space = self.dit_farns * 7.0

    def __init__(self, _wpm=25, _farnsworth=-1.0, _hzTone=600.0,
                 _sample_rate=8000.0, _gain=10000.0):
        self.wpm = 25
        self.ms = math.pow(10, -3)
        self.ms_per_min = 60 / self.ms
        self.char_space_char = ":"
        self.setWPM(_wpm, _farnsworth)
        self.sample_rate = _sample_rate
        self.ditT = Tone(_sample_rate, _tone_freq=_hzTone)
        self.ditT.createTone(self.dit)
        self.dahT = Tone(_sample_rate, _tone_freq=_hzTone)
        self.dahT.createTone(self.dah)
        self.element_spaceZ = np.zeros(
            int(self.element_space * self.ms * self.sample_rate + 0.5))
        self.char_spaceZ = np.zeros(
            int(self.char_space * self.ms * self.sample_rate + 0.5))
        self.word_spaceZ = np.zeros(
            int(self.word_space * self.ms * self.sample_rate + 0.5))
        self.gain = _gain
        self.hzTone = _hzTone

    def translate(self, text):
        """
          Translate from text to string of dits (.) and dahs (-).
          Character space is a ':'.  Word space is ' '.

          >>> m = Morse()
          >>> m.translate("a book")
          '.- -...:---:---:-.-'
          >>> m.translate("AF6UY")
          '._:..-.:-....:..-:-.--'
        """
        rtn = ""
        for c in text.lower():
            if c == " ":
                rtn = rtn + " "
            else:
                rtn = rtn + morse_dict[c] + self.char_space_char

        rtn = re.sub(": ", " ", rtn)  # remove extra : at end of each word
        return re.sub(":$", "", rtn)  # remove last : if it is there

    def play(self, text, _start=100.0):
        """plays the text, but this is likely a poor implementation."""
        m = self.translate(text)

        w = np.zeros(int(_start * self.ms * self.sample_rate), dtype=float)
        for c in m:
            if c == '.':
                w = np.append(w, self.ditT.tone)
                w = np.append(w, self.element_spaceZ)
            if c == '-':
                w = np.append(w, self.dahT.tone)
                w = np.append(w, self.element_spaceZ)
            if c == ":":
                w = np.append(w, self.char_spaceZ)
            if c == " ":
                w = np.append(w, self.word_spaceZ)

        wav_wave = np.array(self.gain * w, dtype=np.int16)
        sd.play(wav_wave, self.sample_rate)
        status = sd.wait()
        if status:
            print('Error: ' + str(status))
