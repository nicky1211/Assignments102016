import properties
import subprocess
import os,glob

class Operationsongit:

	'''

	getLog takes 2 arguments
	1. The path of the repo whose logs are required
	2. Path where those logs need to be stored

	'''

	def getLog(self,repoPath,OutputFile):
		os.chdir(repoPath)

		f = open(OutputFile, "w")
		subprocess.call(["git","log"], stdout=f)

		assert(os.stat(OutputFile).st_size != 0)

	def gitPull(self,repoPath):
		os.chdir(repoPath)
		p= subprocess.Popen("git pull", stdin=subprocess.PIPE, shell=True )
		print "Please wait : Updating repository......."
		p.communicate()

if __name__ == '__main__':

	op = Operationsongit()

	""" Update the local repositories using git pull before extracting the logs"""

	op.gitPull(properties.dataViz_repo_path)
	op.gitPull(properties.mm16_repo_path)
	op.gitPull(properties.sap_repo_path)


	'''
	Get the git log from each of the checked out repositories
	i.e. DataViz ,mm16 ,SAP

	'''

	op.getLog(properties.dataViz_repo_path,properties.dataViz_output_file)
	op.getLog(properties.mm16_repo_path,properties.mm16_output_file)
	op.getLog(properties.sap_repo_path,properties.sap_output_file)
	