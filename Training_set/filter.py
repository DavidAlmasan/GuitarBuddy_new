import numpy as np
import matplotlib.pyplot as plt

def filter(chunkLength):
	b = 8* np.pi * 1000
	a = 1/2/np.pi
	x = np.linspace(-3, 3, 80)
	y = a*b*np.sinc(b*x/2/np.pi)
	y = np.sinc(x)
	y = np.abs(np.fft.fft(y))
	plt.plot(x, y)
	plt.show()

filter(8*1024)
