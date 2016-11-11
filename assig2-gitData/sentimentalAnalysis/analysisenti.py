from __future__ import division
import numpy as np
import subprocess
import pandas as pd
import matplotlib.pyplot as plt
from pymongo import MongoClient
from collections import OrderedDict

class Comparison:

	''' Function to compare the java library usage across the 200 websites '''

	def compareLabels(self):

		labels=['pos','neg','neutral']
		sapCounts = []
		mmCounts = []
		dataCount = []
		totalComments = []
		
		devPosCount = MongoClient().devopsDB.dataVizSenti.find({"label" : "pos"}).count()+1
		devPosnegCount = MongoClient().devopsDB.dataVizSenti.find({"label" : "neg"}).count()
		devPosneutralCount = MongoClient().devopsDB.dataVizSenti.find({"label" : "neutral"}).count()

		mmPosCount = MongoClient().devopsDB.mm16Senti.find({"label" : "pos"}).count() +1
		mmnegCount = MongoClient().devopsDB.mm16Senti.find({"label" : "neg"}).count()
		mmneutralCount = MongoClient().devopsDB.mm16Senti.find({"label" : "neutral"}).count()

		sapPosCount = MongoClient().devopsDB.sapSenti.find({"label" : "pos"}).count()
		sapnegCount = MongoClient().devopsDB.sapSenti.find({"label" : "neg"}).count()
		sapneutralCount = MongoClient().devopsDB.sapSenti.find({"label" : "neutral"}).count() 

		noOfCmtDev = subprocess.check_output(['wc', '-l', '/home/manick/devopsAssig/assig2-gitData/data/datedata.log' ])
		noOfCmtDev = noOfCmtDev.split(" ")[0]
		
		noOfCmtMm = subprocess.check_output(['wc', '-l', '/home/manick/devopsAssig/assig2-gitData/data/datemm.log' ])
		noOfCmtMm = noOfCmtMm.split(" ")[0]

		noOfCmtSap = subprocess.check_output(['wc', '-l', '/home/manick/devopsAssig/assig2-gitData/data/datesap.log' ])
		noOfCmtSap = noOfCmtSap.split(" ")[0]

		# print noOfCmtSap,noOfCmtMm,noOfCmtDev
		totalComments.append(noOfCmtSap)
		totalComments.append(noOfCmtMm)
		totalComments.append(noOfCmtDev)

		# print sapPosCount,sapnegCount,sapneutralCount
		# print mmPosCount,mmnegCount,mmneutralCount
		# print devPosCount,devPosnegCount,devPosneutralCount
		sapCounts.append(sapPosCount)
		sapCounts.append(sapnegCount)
		sapCounts.append(sapneutralCount)

		mmCounts.append(mmPosCount)
		mmCounts.append(mmnegCount)
		mmCounts.append(mmneutralCount)

		dataCount.append(devPosCount)
		dataCount.append(devPosnegCount)
		dataCount.append(devPosneutralCount)



		per_sap = [i / int(totalComments[0]) * 100 for  i in sapCounts]
		per_mm = [i / int(totalComments[1]) * 100 for  i in mmCounts]
		per_data = [i / int(totalComments[2]) * 100 for  i in dataCount]

		positive_per = []
		positive_per.append(per_sap[0])
		positive_per.append(per_mm[0])
		positive_per.append(per_data[0])
		

		negative_per = []
		negative_per.append(per_sap[1])
		negative_per.append(per_mm[1])
		negative_per.append(per_data[1])
		

		neutral_per = []
		neutral_per.append(per_sap[2])
		neutral_per.append(per_mm[2])
		neutral_per.append(per_data[2])
		
		return positive_per,negative_per,neutral_per


if __name__ == '__main__':
	compare = Comparison()
	positive_per,negative_per,neutral_per = compare.compareLabels()
	measures = ['pos','neg','neutral']
	repo = ['SAP','MM16','DATAViZ']
	n_groups = len(measures)

	# create plot
	fig,ax = plt.subplots()
	index = np.arange(n_groups)
	bar_width = 0.4
	opacity = 1.0

	rects1 = plt.bar(index , positive_per, bar_width,alpha=opacity,color='#144100',label='Positive',linewidth=0)
	rects2 = plt.bar(index + 0.25, negative_per, bar_width,alpha=opacity,color='#FE0101',label='Negative',linewidth=0)
	rects3 = plt.bar(index +0.45, neutral_per, bar_width,alpha=opacity,color='#FEFE01',label='Neutral',linewidth=0)

	plt.xlabel('Measures',fontweight='bold',fontsize=15)
	plt.ylabel('Percentage',fontweight='bold',fontsize=15)
	plt.title('Sentimental Analysis',fontweight='bold',fontsize=15)


	plt.xticks(index + bar_width, repo,rotation=90,fontweight='bold',fontsize=10)
	ax.set_axis_bgcolor('#E7E9FF')
	plt.legend(loc='upper centre')
	plt.tight_layout()
	plt.show()

