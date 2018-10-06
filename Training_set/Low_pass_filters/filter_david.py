import numpy as np 
import matplotlib.pyplot as plt

def sincc():
	fc = 4000 #frequency cutoff
	b = fc * 4 * np.pi
	t = np.linspace(-10,10, int(b/2))
	#global t, b, fc
	sinc_fn = b/2/np.pi * np.sinc(t*b/2/np.pi)
	N = int(b/2)
	n = np.arange(N)
	window = 0.42 - 0.5 * np.cos(2 * np.pi * n / (N - 1)) + 0.08 * np.cos(4 * np.pi * n / (N - 1))
	#sinc_fn = np.sinc(t)
	return sinc_fn *window

if __name__ == "__main__":
	fc = 4000 #frequency cutoff
	b = fc * 4 * np.pi
	t = np.linspace(-10,10, int(b/2))
	tt = np.arange(len(t))
	plt.plot(tt, np.abs(np.fft.fft(sincc())))
	#plt.plot(t, sinc())
	plt.show()