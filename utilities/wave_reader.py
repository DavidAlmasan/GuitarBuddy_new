##################################################################
#
# (C) GuitarBuddy 2018
# You should be working too, niggas
#
##################################################################
import wave
import numpy as np

class WaveReader():
    """Reads a wave file and remembers some parameters"""
    def __init__(self, waveName, debug=False):
        self.debug = debug
        self.wf = wave.open(waveName, 'rb')
        self.paramNames = ['nchannels', 'sampwidth', 'framerate',
                           'nframes', 'comptype', 'compname']
        self.getParams()
        self.getFrames()

    def getParams(self):
        """
        Gets and prints the parameters of the wav file
        """
        self.params = self.wf.getparams()
        if (self.debug):
            for self.paramName, self.param in zip(self.paramNames, self.params):
                print(str(self.paramName) + ": " + str(self.param))

    def getFrames(self):
        """
        Reads the frames of the source wav file
        """
        self.frames = self.wf.readframes(-1)
        self.frameRate = self.wf.getframerate()

        ### Transform from string to Int16
        self.frames = np.fromstring(self.frames, 'Int16')
