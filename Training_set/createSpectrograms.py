#!/usr/bin/env python3

##################################################################
#
# (C) GuitarBuddy 2018
# You should be working too, niggas
# 
##################################################################
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as matplt
import wave
import pyaudio
import sys
import os
import csv
import cv2
from Low_pass_filters.filter_david import *
from sklearn.preprocessing import normalize

"""
def graphSpecgram(snippet, graphIndex, chordName):

	###TODO
	###Im to lazy to do this now. its basically nonfunctional
	fix, ax = plt.subplots(1)
	ax.axis('off')
	vectorContent, freqs, bins, im = ax.specgram(x = snippet, 
		Fs = 44100, noverlap = 128, NFFT = 1024, sides = 'onesided',
		pad_to = 2048, scale_by_freq = 'True', mode = 'magnitude')
	plt.close()
	plt.figure(figsize = (5, 5))
	#### at i = 557 our of 1024 freq cutoff at 12kHz
    cutOff = 200
    vectorContent = vectorContent[:cutOff, :] #lowpass filter at 12kHz
    vectorContent = vectorContent / vectorContent.max(axis = 0) #normalising by collumn
    vectorContent = vectorContent * 255
    vectorContent = cv2.resize(vectorContent, (512, 1024), interpolation = 0)

    cv2.imwrite("path/to/output/folder")
"""


class toSpecgram():
    """
	Class to take all samples of wav files that contain ONE chord instance
	and creates a set of specgrams from it
	"""

    def __init__(self):
        self.pa = pyaudio.PyAudio()

        self.sampleFolder = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                         "../Splitter/Individualchords")
        self.sampleChordFolders = os.listdir(self.sampleFolder)
        self.chunk = 1024 * 8
        self.paramNames = ['nchannels', 'sampwidth',
                           'framerate', 'nframes', 'comptype', 'compname']
        self.specgramIndex = 0

    def getChordInstances(self):
        """
		Returns the path to each chord instance i.e AChord_0.wav, BmChord_0.wav, ...
		"""
        for sampleChordFolder in self.sampleChordFolders:
            self.path = os.path.join(self.sampleFolder, sampleChordFolder)  # Path to chord folders
            self.chordInstances = os.listdir(self.path)
            for chordInstance in self.chordInstances:
                self.pathToInstance = os.path.join(self.path, chordInstance)
                yield self.pathToInstance


if __name__ == "__main__":
    example = toSpecgram()
    ion = example.getChordInstances()
    for i in ion:
        print(i)
