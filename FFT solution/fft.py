# -*- coding: utf-8 -*-
##################################################################
#
# (C) GuitarBuddy 2018
#
##################################################################

import numpy as np
from numpy.fft import fft
from ..utilities import wave_reader

class FFT:
    """
    Finds the core frequencies of sound signals
    """
    
    def __init__(self, samplingRate = 44100):
        """
        The constructor
        
        Keyword arguments:
            samplingRate: The sampling rate to be used by the FFT
            (default: 44100)
        """
        self.samplingRate = samplingRate
        
    def findFrequencies(self, data):
        """
        Finds the frequency of the sound signal data
        
        Keyword arguments:
            data: The data to be processed
        """
        x = fft(data)
        print(x)
        
if __name__ == '__main__':
    freqFinder = FFT()
    freqFinder.findFrequencies([0,1,0,-1])
