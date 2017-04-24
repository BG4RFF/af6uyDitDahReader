# -*- coding: utf-8 -*-
import numpy as np
import sounddevice as sd

fs = 8000.
sd.default.samplerate = fs


def playditdah:
  l = 1.  # second
  freq = 600.
  samples = np.arange(int(fs * l)) / fs
  wave = 10000 * np.sin(2 * np.pi * freq * samples)
  wav_wave = np.array(wave, dtype=np.int16)
  sd.play(wav_wave, blocking=True)
