import numpy as np
import sounddevice as sd


class Play:
    def __init__(self, _fs=8000.0):
        self.fs = _fs
        sd.default.samplerate = self.fs

    def play(self, wave, gain=10000):
        wav_wave = np.array(gain * wave, dtype=np.int16)
        sd.play(wave, self.fs)
        status = sd.wait()
        if status:
            print('Error: ' + str(status))
