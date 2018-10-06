# -*- coding: utf-8 -*-
##################################################################
#
# (C) GuitarBuddy 2018
#
##################################################################

import numpy as np
import sys
import os
from numpy.fft import fft
sys.path.append(os.path.join(os.path.dirname(__file__), "../utilities"))
from wave_reader import WaveReader

class FFT:
    """
    Finds the core frequencies of sound signals
    """
    
    def __init__(self, data, samplingRate = 44100):
        """
        The constructor
        
        Keyword arguments:
            samplingRate: The sampling rate to be used by the FFT
            (default: 44100)
            data: The data to be processed
        """
        self.samplingRate = samplingRate
        self.data = data
        
    def findFrequencies(self):
        """
        Finds the frequency of the sound signal data
        """
        x = np.abs(fft(self.data))
        return np.abs(fft(x.frames))
        
if __name__ == '__main__':
    path = os.path.join(os.path.dirname(__file__), "../Splitter/IndividualChords/A/Achord_0.wav")
    x = WaveReader(path)
    freqFinder = FFT(x.frames)
    freqFinder.findFrequencies()
