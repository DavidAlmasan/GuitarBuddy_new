import csv
import sys
import os
import wave
sys.path.append(os.path.join(os.path.dirname(__file__)), "../utilities")
from constants import chordToIndex

class DatasetCreator():
    """Creates a dataset to be fed to the neural network."""
    def __init__(self):
        self.chordFolder = os.path.join(os.path.dirname(__file__), "../Splitter/IndividualChords/")
        self.coordNames = os.listdir(self.chordFolder)
        self.bufferSize = 1024
        self.datasetPath = os.path.join(os.path.dirname(__file__), "./dataset.csv")

    def createDataset(self):
        with open(self.datasetPath, 'a') as editCsv:
            writer = csv.writer(editCsv)

            for chord in self.coordNames:
                chordPath = os.path.join(self.chordFolder, chord)
                for chordInstance in os.listdir(chordPath)
                    chordInstance = os.path.join(chordPath, chordInstance)
                    self.wf = wave.open(chordInstance, 'rb')

                    self.getParams()
                    self.getFrames()





    def getParams(self):
        """
        Gets and prints the parameters of the wav file
        """
        self.params = self.wf.getparams()
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

