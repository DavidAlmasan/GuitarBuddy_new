import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../utilities"))
import wave_reader

wave_reader.WaveReader("../voice_rec")

