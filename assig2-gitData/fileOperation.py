import fileinput
import os
import subprocess
import properties

class fileOperation:

	def getcommitMessageFromLog(self,inFile,outFile):


		p = subprocess.Popen("grep -Ev 'commit|Author|Date' %s > %s" %(inFile, outFile), stdin=subprocess.PIPE, shell=True )
		p.communicate( b"input data\n" )


	def removeEmptyLines(self,inF,outF):
		with open(outF, 'a') as f:
			for line in fileinput.FileInput(inF,inplace=1):
				if line.rstrip():
					f.write(line)

	def removeUnwantedSpaces(self,inFile,outFile):

		p = subprocess.Popen("sed -e 's/^[ \t]*//' %s > %s"%(inFile,outFile), stdin=subprocess.PIPE, shell=True )
		p.communicate( b"input data\n" )

# if __name__ == '__main__':

# 	gt = fileOperation()

# 	"""
	

# 	"""

#  	#gt.getcommitMessageFromLog(properties.dataViz_output_file,"/home/manick/devopsAssasination/assig2-gitData/data/outFile.txt")
#  	#gt.removeEmptyLines("/home/manick/devopsAssasination/assig2-gitData/data/outFile.txt","/home/manick/devopsAssasination/assig2-gitData/data/outFile_formated.txt")
#  	gt.removeUnwantedSpaces("/home/manick/devopsAssasination/assig2-gitData/data/outFile_formated.txt","/home/manick/devopsAssasination/assig2-gitData/data/clean.txt")