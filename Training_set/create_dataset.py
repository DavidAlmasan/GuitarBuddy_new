##################################################################
#
# (C) GuitarBuddy 2018
# You should be working too, niggas
#
##################################################################
import csv
import sys
import os
import numpy as np
sys.path.append(os.path.join(os.path.dirname(__file__), "../utilities"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../FFT_solution"))
import fft
import constants
import wave_reader


class DatasetCreator():
    """Creates a dataset to be fed to the neural network."""
    def __init__(self, useFFT = True):
        self.chordFolder = os.path.join(os.path.dirname(__file__), "../Splitter/IndividualChords/")
        self.coordNames = os.listdir(self.chordFolder)
        self.bufferSize = 1024
        self.datasetPath = os.path.join(os.path.dirname(__file__), "./dataset.csv")

        self.useFFT = useFFT

        self.createDataset()

    def createDataset(self):
        with open(self.datasetPath, 'a', newline = "") as editCsv:
            writer = csv.writer(editCsv)

            for chord in self.coordNames:
                chordPath = os.path.join(self.chordFolder, chord)
                for chordInstance in os.listdir(chordPath):
                    chordInstance = os.path.join(chordPath, chordInstance)

                    waveFile = wave_reader.WaveReader(chordInstance)
                    # sampleIndex runs through waveFile and creates the samples that will be loaded into dataset.csv
                    sampleIndex = 0
                    while sampleIndex < len(waveFile.frames) - 1024:
                        row = waveFile.frames[sampleIndex:sampleIndex+1024]

                        if self.useFFT:
                            fftData = fft.FFT(row, samplingRate = waveFile.frameRate)
                            row = fftData.findFFT()
                        row = np.append(row, constants.chordToIndex(chord))
                        writer.writerow(row)
                        sampleIndex += 1024




if __name__ == "__main__":
    DatasetCreator()




