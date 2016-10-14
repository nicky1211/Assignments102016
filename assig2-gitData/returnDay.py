import datetime
import properties
import subprocess
import pandas as pd

class returnDateInfo:


	def __init__(self):
		self._actualweekDays = ['Mon ','Tue ','Wed ','Thu ','Fri ']
		self._actualweekEnds = ['Sat ','Sun ']
		self._obtainedweekdays = []
		self._obtainedweekends = []
		self._listofDates = []
		self._listofDays = []

	def getDaysList(self,inF):

		p = subprocess.Popen("grep -i 'Date' %s"%inF, stdout=subprocess.PIPE, shell=True ) 
		for line in iter(p.stdout.readline,''):
			self._listofDates.append(line)
		p.communicate( b"input data\n" )
		for line in self._listofDates:
			self._listofDays.append(line[8:12])
			
		return self._listofDays

	def getNumberOfWeekDaysandWeekEnds(self,inF):
		days_lst = self.getDaysList(inF)
		for day in days_lst:
			if day in self._actualweekDays:
				self._obtainedweekdays.append(day)
			else:
				self._obtainedweekends.append(day)

		return len(self._obtainedweekdays),len(self._obtainedweekends)

if __name__ == '__main__':

	returnDateInfo = returnDateInfo()
	
	inF_dataViz = properties.dataViz_output_file
	inF_sap = properties.dataViz_output_file
	inF_mm16 = properties.dataViz_output_file

	dataViz_count = returnDateInfo.getNumberOfWeekDaysandWeekEnds(inF_dataViz)
	dataViz_countWeekDays = dataViz_count[0]
	dataViz_countWeekEnds = dataViz_count[1]

	sap_count = returnDateInfo.getNumberOfWeekDaysandWeekEnds(inF_sap)
	sap_countWeekDays = sap_count[0]
	sap_countWeekEnds = sap_count[1]

	mm16_count = returnDateInfo.getNumberOfWeekDaysandWeekEnds(inF_mm16)
	mm16_countWeekDays = mm16_count[0]
	mm16_countWeekEnds = mm16_count[1]


	raw_data = {'NumberOfWeekDays': [dataViz_countWeekDays,sap_countWeekDays,mm16_countWeekDays],'NumberOfWeekEnds': [dataViz_countWeekEnds,sap_countWeekEnds,mm16_countWeekEnds]}
	df = pd.DataFrame(raw_data, columns = ['NumberOfWeekDays', 'NumberOfWeekEnds'], index = ['DataViz','SAP','MM16'])
	df.to_csv('example.csv')



