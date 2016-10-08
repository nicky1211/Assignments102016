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

if __name__ == '__main__':

	gt = fileOperation()


	#For the dataViz repo
 	gt.getcommitMessageFromLog(properties.dataViz_output_file,"/home/manick/devopsAssasination/assig2-gitData/data/datvizfile1.txt")
 	gt.removeEmptyLines("/home/manick/devopsAssasination/assig2-gitData/data/datvizfile1.txt","/home/manick/devopsAssasination/assig2-gitData/data/dataviz_empty_lines_removed.txt")
 	gt.removeUnwantedSpaces("/home/manick/devopsAssasination/assig2-gitData/data/dataviz_empty_lines_removed.txt","/home/manick/devopsAssasination/assig2-gitData/data/dataviz_clean.txt")

 	#For the SAP repo

 	gt.getcommitMessageFromLog(properties.sap_output_file,"/home/manick/devopsAssasination/assig2-gitData/data/sapfile1.txt")
 	gt.removeEmptyLines("/home/manick/devopsAssasination/assig2-gitData/data/sapfile1.txt","/home/manick/devopsAssasination/assig2-gitData/data/sap_empty_lines_removed.txt")
 	gt.removeUnwantedSpaces("/home/manick/devopsAssasination/assig2-gitData/data/sap_empty_lines_removed.txt","/home/manick/devopsAssasination/assig2-gitData/data/sap_clean.txt")


 	#For the mm16 repo
 	gt.getcommitMessageFromLog(properties.mm16_output_file,"/home/manick/devopsAssasination/assig2-gitData/data/mmfile1.txt")
 	gt.removeEmptyLines("/home/manick/devopsAssasination/assig2-gitData/data/mmfile1.txt","/home/manick/devopsAssasination/assig2-gitData/data/mm16_empty_lines_removed.txt")
 	gt.removeUnwantedSpaces("/home/manick/devopsAssasination/assig2-gitData/data/mm16_empty_lines_removed.txt","/home/manick/devopsAssasination/assig2-gitData/data/mm16_clean.txt")