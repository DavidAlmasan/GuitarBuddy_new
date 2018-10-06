#!/usr/bin/env python3

##################################################################
#
# (C) GuitarBuddy 2018
# You should be working too, niggas
#
##################################################################
import numpy as np
import argparse
import matplotlib.pyplot as plt
import wave
import pyaudio
import sys
import os
"""
Changes needed
- start, stop variables need more specific names


"""

class Splitter():
	"""
	Class that takes a wav file that contains multiple iterations 
	of the same chord, then splits it into wav files that contain
	only one iteration of the chord
	"""
	def __init__(self, sourceName, chordName):
		self.sourceName = sourceName
		self.paramNames = ['nchannels', 'sampwidth', 'framerate', 
							'nframes', 'comptype', 'compname']
		self.wf = wave.open(self.sourceName, 'rb')

		#For splitting into wav files that contain ONE chord
		self.bufferSize = 4096 
		self.thr = 500
		self.pa = pyaudio.PyAudio()
		self.chordIndex = 0
		self.chordName = chordName###Not essentially a chord name, but it also sets the main 
																#IndividualChords Folder
		self.chordFolder = 'IndividualChords/' +chordName + '/'
		self.path = os.path.join(os.path.dirname(os.path.realpath(__file__)), self.chordFolder)

	def changeChordIndex(self, path):
		"""
		Returns the number of files in a folder given by <path>
		"""
		numOfExistingFiles = len(os.listdir(path))
		self.chordIndex += numOfExistingFiles

		print(self.chordIndex)

	def getParams(self):
		"""
		Gets and prints the parameters of the wav file
		"""
		self.params = self.wf.getparams()
		for self.paramName, self.param in zip(self.paramNames, self.params):
			print (str(self.paramName) + ": " + str(self.param))

	def getFrames(self):
		"""
		Reads the frames of the source wav file
		"""
		self.frames = self.wf.readframes(-1)
		self.frameRate = self.wf.getframerate()

		### Transform from string to Int16
		self.frames = np.fromstring(self.frames, 'Int16')

	def getPowerSpectrum(self):
		"""
		Creates a list that contains the power of the sound file
		"""
		self.power = np.zeros(len(self.frames)- self.bufferSize +1)
		self.power[0] = sum([frame**2 for frame in self.frames[:self.bufferSize]]) / self.bufferSize
		
		#Populating the power spectrum vector
		for powerFrameIndex in range(1, len(self.frames)-self.bufferSize + 1):
			self.power[powerFrameIndex] = self.power[powerFrameIndex-1] + (self.frames[powerFrameIndex + self.bufferSize - 1]**2- self.frames[powerFrameIndex - 1]**2) / self.bufferSize

		self.power = np.sqrt(self.power)

		#If power is < threshhold, make it zero
		self.power = [0 if powerFrame < self.thr else powerFrame for powerFrame in self.power]

	def plotFramesAndPower(self):
		"""
		Plots frames and power frames for debugging reasons
		"""
		plt.plot(self.frames)
		plt.figure()
		plt.plot(self.power)
		plt.show()

	def createSoundFile(self, individualFileFrames, individualFileName):
		"""
		Create folder for individual chords, if exists, adds to files 
		"""

		try:
			os.makedirs(self.path)	
		except:
			#Folder exists
			pass
		individualFileName = self.path + individualFileName
		self.wf = wave.open(individualFileName, 'wb')
		self.wf.setnchannels(1)
		self.wf.setsampwidth(self.pa.get_sample_size(pyaudio.paInt16))
		self.wf.setframerate(self.frameRate)
		self.wf.writeframes(b''.join(individualFileFrames))
		self.wf.close()

	def generateSoundFiles(self):
		"""
		Generates the individual sound files using the createSoundFile method
		"""
		#Adjust chord index by number of existing files
		print (self.path)
		try:
			self.changeChordIndex(self.path)
		except:
			#Folder doesn't exist yet
			pass

		start = 0
		while start < len(self.power) - 1:
			if self.power[start] == 0 and self.power[start + 1] != 0:
				startIndex = start + 1
				stop = start + 1
				while stop < len(self.power) -1:
					if self.power[stop] != 0 and self.power[stop + 1] ==0:
						stopIndex = stop + 1
						self.individualChordName = self.chordName + 'chord_' + str(self.chordIndex) + '.wav'
						self.createSoundFile(self.frames[startIndex: stopIndex], self.individualChordName)
						self.chordIndex += 1
						print(self.individualChordName)
						break
					stop += 1
			start += 1

	def splitSoundFile(self, plotOn = False):
		"""
		Main splitting structure
		"""
		self.getParams()
		self.getFrames()
		self.getPowerSpectrum()
		if plotOn:
			self.plotFramesAndPower()
		self.generateSoundFiles()

def parseArgs():
	parser = argparse.ArgumentParser(description = "Splits a sound file into individual files containing only one iteration of the chord")
	parser.add_argument('-src', help = "Path to sound file to be split",
						default = "Ggg.wav")
	parser.add_argument('-name', help = "Name of chord: <A>\n<Am>\n<B>\n<Bm>\n<C>\n<Cm>\n<D>\n<Dm>\n<E>\n<Em>\n<F>\n<Fm>\n<G>\n<Gm>\n",
						default = 'G')
	return parser.parse_args()
if __name__== "__main__":
	args = parseArgs()

	example = Splitter(args.src, args.name)
	example.splitSoundFile()