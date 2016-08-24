import sys
from Crypto.Hash import SHA256

filename = "ANUJgathered.txt"


def hashEmail(mail):
	return SHA256.new(mail).hexdigest()

def main():

	githubName 	= "anujsinghdm" 
	outputStr 	= "" 
	timestamps 	= []	 

	with open(filename) as f:
		start 	= 0
		end 	= 10

		lines = f.readlines()

		entriesArray = []

		while end <= len(lines):
			myHash = str(hashEmail(githubName))
			entryHash = str(lines[start].split()[0])

			if entryHash == myHash:
				entryStore = []
				timestamp = lines[start].split(' | ', 1)[-1]

				if timestamp not in timestamps:
					for index in range(start, end):
						entryIdx = index-start 

						if entryIdx == 0:
							entryStore.append(timestamp)
							timestamps.append(timestamp)

						# 1 -> light
						# 2 -> steps
						# 3 -> volume
						# 4 -> acc X
						# 5 -> acc Y
						# 6 -> acc Z
						# 7 -> lati
						# 8 -> longi
						selection = [3]

						if entryIdx in selection:
							entry = lines[index].split(' ', 1)[-1]
							entryStore.append(entry)
							
				 	entriesArray.append(entryStore)	

			start = end 
			end += 10

		for entry in entriesArray:
		  	for element in entry:
				outputStr += element
			outputStr += "---------------\n"

		with open(githubName + "_VOLUME" + ".txt", 'a') as the_file:
			the_file.write(outputStr)

if __name__ == "__main__":

    main()
