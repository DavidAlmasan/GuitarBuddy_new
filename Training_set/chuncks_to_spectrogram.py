import numpy as np
import matplotlib.pyplot as plt
import matplotlib as matplt
import wave
import pyaudio
import sys
import csv
import cv2
#from Low_pass_filters.lowpass_filter import lowpass_filter
from Low_pass_filters.filter_david import *
from sklearn.preprocessing import normalize



    
CHORD = 'Gchord' #will soon change to be part of the dictionary above
N = 54
graph_index = 0



pa = pyaudio.PyAudio()

# Make a array to store the chord names
chords = []
for i in range(ord('A'), ord('G') + 1):
    chords.append(chr(i) + '_chord')
    chords.append(chr(i) + 'm_chord')
    # TODO
    # chords.append(chr(i) + '#_chord')
    # chords.append(chr(i) + '#m_chord')



def graph_spectrogram(data, chordName = CHORD):
    global graph_index
    #data = np.convolve(data, sincc())
    #a = 10 #subsampling factor
    #subsampleIndex = 0
    #subsampledVector = []
    #while subsampleIndex + a < len(data):
    #   subsampledVector.append(np.average(data[subsampleIndex:subsampleIndex+a]))
    #   subsampleIndex += a 

    fig,ax = plt.subplots(1)
    #fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
    ax.axis('off')
    vectorContent, freqs, bins, im = ax.specgram(x=data, Fs=44100, noverlap=128, NFFT=1024, sides='onesided', pad_to = 2048, scale_by_freq = "True", mode = "magnitude")
    plt.close()
    plt.figure(figsize = (5, 5))
    #### at i = 557 our of 1024 freq cutoff at 12kHz
    cutOff = 200
    vectorContent = vectorContent[:cutOff, :] #lowpass filter at 12kHz
    vectorContent = vectorContent / vectorContent.max(axis = 0) #normalising by collumn
    vectorContent = vectorContent *255
    vectorContent = cv2.resize(vectorContent, (512, 1024), interpolation = 0)
    #cv2.imshow("img", vectorContent)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()


    cv2.imwrite("./" + CHORD + "Colormap/" + str(graph_index) + ".jpg", vectorContent)


    # fix, ax = plt.subplots(1)
    # ax.axes.get_xaxis().set_visible(False)
    # ax.axes.get_yaxis().set_visible(False)
    # ax.set_frame_on(False)
    # ax.pcolormesh(vectorContent)
    # plt.savefig("./colormap/" + str(graph_index) + ".png", pad_inches = 0, bbox_inches='tight')




for no in range(N):
    wf = wave.open('./' + CHORD + '/' + CHORD + '_' + str(no) + '.wav', 'rb')



    CHUNK = 1024*8   # chunk size to be sent to graph_spectrogram function
    paramnames = ['nchannels', 'sampwidth', 'framerate', 'nframes', 'comptype', 'compname']
    p = wf.getparams()
    for i,j in zip(paramnames, p):
        print(str(i) + ': ' + str(j))
    Y = wf.readframes(-1)
    fs = wf.getframerate()
    wf.close()
    Y = np.fromstring(Y, 'Int16')
    index = 0
    # while index+CHUNK-1<len(Y):
    #     f = open("data_set.txt", 'a')
    #     f.write(str(Y[index:index+CHUNK])+'\n')
    #     index += CHUNK/8

    index = 0
    print("# of chucks: ", (len(Y)-1024*8) * 4 / (3*CHUNK))
    p = no / N * 100
    print(str(p) + " %")

    while index+ CHUNK < len(Y):
        snippet = Y[index:index+CHUNK] #snippet is the CHUNK over which we create a number of spectrograms using the graph_spectrogram function
        index += CHUNK
        graph_spectrogram(snippet)
        graph_index+=1




  
