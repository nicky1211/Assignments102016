import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame.from_csv('/home/manick/devopsAssig/assig2-gitData/data/hourlyCOunt.csv')

#Create lists to store the values
labelslst = ['DATAVIZ','MM16','SAP']
timeList = []
dataCountList= []
mm16CountList = []
sapCountList = []

#Read the Time into a list
for each in df['Time']:
	timeList.append(each)
#Read DataVizCounts
for each in df['DataViz']:
	dataCountList.append(each)
#Read MM16
for each in df['MM16']:
	mm16CountList.append(each)
#Read SAP
for each in df['SAP']:
	sapCountList.append(each)

n_groups = len(timeList)
# create plot
fig,ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.4
opacity = 1

rects1 = plt.bar(index, dataCountList, bar_width,alpha=opacity,color='#7B0000',label='DataViz',linewidth=0)
rects2 = plt.bar(index+0.35, mm16CountList, bar_width,alpha=opacity,color='#FDFF71',label='MM16',linewidth=0)
rects3 = plt.bar(index+0.25, sapCountList, bar_width,alpha=opacity,color='#FF7171',label='SAP',linewidth=0)

plt.xlabel('Categories',fontweight='bold',fontsize=15)
plt.ylabel('Count',fontweight='bold',fontsize=15)
plt.title('Comit COmparison',fontweight='bold',fontsize=15)


plt.xticks(index + bar_width, timeList,rotation=90,fontweight='bold',fontsize=10)
ax.set_axis_bgcolor('#E7E9FF')
plt.legend(loc="upper left")
plt.tight_layout()
plt.show()
