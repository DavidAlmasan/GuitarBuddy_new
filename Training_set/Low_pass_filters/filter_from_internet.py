import numpy as np 
import matplotlib.pyplot as plt

def sinc():

	fc = 2000
	b = 0.08 #originally 0.08
	N = int(np.ceil((4 / b)))
	N = 100
	n = np.arange(N)
	if not N % 2: N += 1
	sinc_func = np.sinc(2 * fc * (n - (N - 1) / 2.))
	window = 0.42 - 0.5 * np.cos(2 * np.pi * n / (N - 1)) + 0.08 * np.cos(4 * np.pi * n / (N - 1))
	sinc_func = sinc_func * window
	sinc_func = sinc_func / np.sum(sinc_func)
	return sinc_func
	
def sinc2():
	fc = 0.1
	b = 0.08
	N = int(np.ceil((4 / b)))
	n = np.arange(N)
	if not N % 2: N += 1
	sinc_func = np.sinc(2 * fc * (n - (N - 1) / 2.))
	return sinc_func


if __name__ == "__main__":
	b = 0.08
	N = int(np.ceil((4 / b)))
	N = 100
	plt.plot(np.arange(N)*b/4, np.abs(np.fft.fft(sinc())))
	#plt.plot(sinc2())
	plt.figure()
	plt.plot(sinc())
	plt.show()
