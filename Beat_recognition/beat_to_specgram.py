import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../utilities"))
import wave_reader
# for mpl plt issues
import matplotlib as mpl
mpl.use('tkagg')
import matplotlib.pyplot as plt

class BeatRecognition():
    def __init__(self):
        self.pathToBeats = os.path.join(os.path.dirname(__file__), "../voice_recorder_samples/beats")
        self.soundSamples = os.listdir(self.pathToBeats)

        self.filtering()

    def filtering(self):
        for sample in self.soundSamples:
            samplePath = os.path.join(self.pathToBeats, sample)
            waveFile = wave_reader.WaveReader(samplePath)
            print(waveFile.frameRate)
            spectrum, freq, t, image = plt.specgram(waveFile.frames, NFFT= 1024, Fs = waveFile.frameRate, noverlap = 0)
            plt.show()



if __name__ == "__main__":
    BeatRecognition()