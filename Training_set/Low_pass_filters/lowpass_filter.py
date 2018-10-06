import numpy as np
from numpy.fft import *
import matplotlib.pyplot as plt

def sinc(x):
    try:
        return np.sin(x) / x
    except (e):
        return 1

def center(arr):
    d = len(arr) // 2
    newarr = np.zeros(len(arr))
    for i in range(len(arr)):
        if i-d < 0:
            newarr[i] = arr[i-d  + len(arr)]
        else:
            newarr[i] = arr[i-d]
    return newarr
def lowpass_filter():
    BW = 1000                         # Hz - bandwidth of FFT
    BW *= 2 * np.pi                 # convert to rad / s
    l = 4.                          # ratio of fs to BW
    root = 50                 # max value of BW * X (so that sinc curve has the same shape)
    b = root / BW                   # max value of X
    N = int(l * root / np.pi + 1)   # number of samples
    Ts = 2* b / (N - 1)             # sampling period
    fs = 1 / Ts                     # sampling frequency

    #print("BW (Hz): ", BW / 2 / np.pi)
    #print("range(-", b, ", ", b, ")")
    #print("# of points: ", N)
    #print("fs(Hz): ", fs, " Ts: ", Ts)
    X = np.linspace(-b, b, N)
    n = np.arange(N)
    window = 0.42 - 0.5 * np.cos(2 * np.pi * n / (N - 1)) + 0.08 * np.cos(4 * np.pi * n / (N - 1))
    Y = 2 * BW * sinc(BW * X)
    Y = Y * window
    #plt.plot(X, Y)
    #plt.figure()
    #fY =  np.abs(fft(Y))
    #fY = center(fY)
    #offset = (N//2)
    #plt.plot((np.arange(N) - offset) * fs / N, fY)
    #plt.show()
    return Y
if __name__ == "__main__":
    plt.plot(np.abs(np.fft.fft(lowpass_filter())))
    plt.show()
