import sys
from Crypto.Hash import SHA256

filename = "ANUJ_VALUES.txt"
directory = "ANUJ/"


def timeInMinutes(time):
	tr = time.split(':', 2)

	h = float(tr[0])*60
	m =	float(tr[1])
	s =	float(tr[2])/60

	return h + m + s

def main():
	resultStr = ""
	with open(directory + filename) as f:

		result = []

		lines = f.readlines()
		dates = []

		first = 1

		entry = []
		for line in lines:
		 	if line != "---------------\n":
		 		if first == 1:
		 			date = line.split(' ', 1)[0].replace("\n","")
		 			time = line.split(' ', 1)[1].replace("\n","")

		 			if date not in dates:
		 				dates.append(date)
		 			entry.append(date)
		 			entry.append(time)

		 			first = 0
		 		else:
		 			entry.append(line.replace("\n",""))
		 	else:
		 		first = 1
		 		result.append(entry)
		 		entry = []
	

	startTime = timeInMinutes(result[0][1])

	for entry in result:
		if entry[0] == dates[0]:
			#print the data for readability
			print '{:20s} {:10s}'.format(str(timeInMinutes(entry[1])-startTime), entry[2])
			resultStr += str(timeInMinutes(entry[1])-startTime) + "||" + str(entry[2]) + "\n"
			#print the data for Latex
			#print("(" + str(timeInMinutes(entry[1])-startTime) + "\t\t" + entry[2] + ")")
	 	
	 	#print("\n")

	with open("data_" + filename, 'a') as the_file:
		the_file.write(resultStr)


if __name__ == "__main__":
    main()
