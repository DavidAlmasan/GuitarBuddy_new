# -*- coding: utf-8 -*-
##################################################################
#
# (C) GuitarBuddy 2018
#
##################################################################

import matplotlib.pyplot as plt
import numpy as np
import os
from numpy.fft import fft
from utilities.wave_reader import WaveReader


class FFT:
    """
    Finds the core frequencies of sound signals
    """

    def __init__(self, data, samplingRate=44100):
        """
        The constructor
        
        Keyword arguments:
            samplingRate: The sampling rate to be used by the FFT
            (default: 44100)
            data: The data to be processed
        """
        self.samplingRate = samplingRate
        self.data = data

    def findMaxFrequencies(self, n):
        """
        Finds the frequency of the sound signal data
        """
        fftData = np.abs(fft(self.data))
        peaks = []
        for i in range(len(fftData) // 2):
            if self.isPeak(fftData, i):
                peaks.append((fftData[i], i))
        peaks.sort(reverse=True)
        if len(peaks) > n:
            return peaks[:n]
        return peaks

    def isPeak(self, data, i):
        if i == 0:
            return data[i] > data[i + 1]
        if i == len(data) - 1:
            return data[i] > data[i - 1]
        return data[i] > data[i + 1] and data[i] > data[i - 1]


if __name__ == '__main__':
    path = os.path.join(os.path.dirname(__file__), "../Splitter/IndividualChords/A/Achord_0.wav")
    x = WaveReader(path)
    freqFinder = FFT(x.frames)
    res = freqFinder.findMaxFrequencies(10)
    print([k[1] for k in res])
