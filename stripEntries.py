import sys
from Crypto.Hash import SHA256

filename = "data_MiChrFri_VOLUME.txt"

def main():
	resultStr = ""
	with open(filename) as f:

		lines = f.readlines()


		timeprefix = 0
		prefixCounter = 0
		prefixEntries = 0

		for line in lines:

			array = line.split('||', 1) 
			time = array[0].replace("\n","")
			entry = array[1].replace("\n","")

			
			if str(time.split('.', 1)[0]) == str(timeprefix):
				#print(time + " : " + entry)
				prefixCounter += 1
				prefixEntries += float(entry)

			else:
				print("(" + str(timeprefix) + " , " + str(prefixEntries) + ")")
				timeprefix += 1
				prefixCounter = 0
				prefixEntries = 0

		print("(" + str(timeprefix) + " , " + str(prefixEntries) + ")")	


		#print(test)
		# 	print(line)

	# with open("data_" + filename, 'r+') as the_file:
	# 	the_file.write(resultStr)


if __name__ == "__main__":
    main()
