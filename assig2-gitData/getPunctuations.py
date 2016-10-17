import properties
from collections import Counter

class Punctuations:

	def __init__(self):
		self._listOfPunc = ["\'",":","\,","-","!",".","?","\"",";"]
		self._foundPunc = []

	def getPunk(self,file):
		with open(file, 'r') as f:
			for line in f:
				for word in line:
					for char in word:
						if char in self._listOfPunc:
							self._foundPunc.append(char)

		counts = Counter(self._foundPunc)
		print(dict(counts))


if __name__ == '__main__':
	punc = Punctuations()
	file = "/home/manick/devopsAssasination/assig2-gitData/data/dataviz_clean.txt"
	punc.getPunk(file)
	print("******************************************************************************")
	file = "/home/manick/devopsAssasination/assig2-gitData/data/mm16_clean.txt"
	punc.getPunk(file)
	print("******************************************************************************")
	file = "/home/manick/devopsAssasination/assig2-gitData/data/sap_clean.txt"
	punc.getPunk(file)