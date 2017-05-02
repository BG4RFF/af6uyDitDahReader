import math
import re

import morsestring as ms


class Morse:
    wpm = 25
    ms = math.pow(10, -3)
    ms_per_min = 60 / ms
    char_space = ":"

    def setWPM(self, _wpm, _farnsworth=-1.0):
        if _farnsworth > _wpm | | _farnsworth <= 0.0:
            _farnsworth = _wpm
        self.wpm = _wpm
        # paris is 50 dits (word used to define a word)
        _paris = 50.0
        self.dit = self.ms_per_min / (_paris * wpm)
        self.dah = 3.0 * self.dit
        self.dit_farns = self.ms_per_min / (_paris * _farnsworth)
        self.element_space = self.dit
        self.char_space = self.dit_farns * 3.0
        self.word_space = self.dit_farns * 7.0

    def __init__(self, _wpm=25, _farnsworth=-1.0, _sample_rate=8000.0):
        self.setWPM(self, _wpm, _farnsworth)
        self.sample_rate = _sample_rate

    def translate(self, text):
        """translate from english text to string of dits (.) and dahs (-).
          Character space is a ':'.  Word space is ' '.

          >>> m = Morse()
          >>> m.translate("a book")
          '.- -...:---:---:-.-'
          >>> m.translate("AF6UY")
          '._:..-.:-....:..-:-.--'
        """
        rtn = ""
        for c in text:
            if c == " ":
                rtn = rtn + " "
            else:
                rtn = rtn + ms.morse_dict[c] + self.char_space

        rtn = re.sub(": ", " ", rtn)  # remove extra : at end of each word
        return re.sub(":$", "", rtn)  # remove last : if it is there
