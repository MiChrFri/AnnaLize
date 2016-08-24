import sys
from Crypto.Hash import SHA256

user = "p1"
filename = user + "_Volume.txt"

mapToo = float(91)

def main():

	with open(filename) as f:

		lines = f.readlines()

		numberOfLines = float(len(lines))

		singleLine = mapToo/numberOfLines

		for idx, line in enumerate(lines):
			print((idx+1)*singleLine)
		

if __name__ == "__main__":

    main()
