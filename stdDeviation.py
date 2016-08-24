import sys

import numpy

from Crypto.Hash import SHA256

entry = "LIGHT"
filename = "data_JC_"+ entry +".txt"

def main():
	resultStr = ""
	with open(filename) as f:

		lines = f.readlines()
		values 	= []


		timeprefix = 0
		prefixCounter = 0
		prefixEntries = 0

		for line in lines:

			array = line.split('||', 1) 
			time = array[0].replace("\n","")
			entry = array[1].replace("\n","")
			
			if str(time.split('.', 1)[0]) == str(timeprefix):
				prefixCounter += 1
				prefixEntries += float(entry)

			else:
				if prefixCounter != 0:
					values.append(float(prefixEntries/prefixCounter))
					timeprefix += 1
					prefixCounter = 0
					prefixEntries = 0
		
		# if prefixCounter != 0:
		# 	values.append(float(prefixEntries/prefixCounter))

		# for value in values:
		# 	print(value)

		average = sum(values) / float(len(values))
		print("avg: " + str(average))

		stdDeviation = float(numpy.std(values))
		print("dev: " + str(stdDeviation))

		maxPeek = average + stdDeviation
		minPeek = average - stdDeviation

		print("min " + str(minPeek))
		print("max " + str(maxPeek))

		print("count " + str(len(values)) + "\n")
		for value in values:

			if value < minPeek:
			 	#print("minPeek " + str(value))
			 	minPer = (100/minPeek)*value
			 	print(str(abs(100-minPer)))
			if value > maxPeek:
				#print("maxPeek " + str(value))
				maxPer = (100/minPeek)*value
				print(str(abs(100-maxPer)))


if __name__ == "__main__":
    main()
