##################################################################
#
# (C) GuitarBuddy 2018
# You should be working too, niggas
#
##################################################################
import csv
import sys
import os
import wave
sys.path.append(os.path.join(os.path.dirname(__file__), "../utilities"))
import constants
import wave_reader


class DatasetCreator():
    """Creates a dataset to be fed to the neural network."""
    def __init__(self):
        self.chordFolder = os.path.join(os.path.dirname(__file__), "../Splitter/IndividualChords/")
        self.coordNames = os.listdir(self.chordFolder)
        self.bufferSize = 1024
        self.datasetPath = os.path.join(os.path.dirname(__file__), "./dataset.csv")

        self.createDataset()

    def createDataset(self):
        with open(self.datasetPath, 'a') as editCsv:
            writer = csv.writer(editCsv)

            for chord in self.coordNames:
                chordPath = os.path.join(self.chordFolder, chord)
                for chordInstance in os.listdir(chordPath):
                    chordInstance = os.path.join(chordPath, chordInstance)

                    waveFile = wave_reader.WaveReader(chordInstance)
                    break



if __name__ == "__main__":
    DatasetCreator()




