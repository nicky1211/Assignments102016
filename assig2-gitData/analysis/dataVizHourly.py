import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pymongo import MongoClient
import matplotlib.ticker as ticker

#Plot Subplot For DataViz on all days

hour = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
index = np.arange(len(hour))
mondayCount = []
tuesdayCount = []
wednesdayCount = []
thursdayCount = []
fridayCount = []
saturdayCount = []
sundayCount = []

df = pd.read_csv("/home/manick/devopsAssig/assig2-gitData/data/dataViz/dataVizMonday.csv")
saved_column = df['Count']
for count in saved_column:
	mondayCount.append(count)

df = pd.read_csv("/home/manick/devopsAssig/assig2-gitData/data/dataViz/dataVizTuesday.csv")
saved_column = df['Count']
for count in saved_column:
	tuesdayCount.append(count)

df = pd.read_csv("/home/manick/devopsAssig/assig2-gitData/data/dataViz/dataVizWednesday.csv")
saved_column = df['Count']
for count in saved_column:
	wednesdayCount.append(count)

df = pd.read_csv("/home/manick/devopsAssig/assig2-gitData/data/dataViz/dataVizThursday.csv")
saved_column = df['Count']
for count in saved_column:
	thursdayCount.append(count)

df = pd.read_csv("/home/manick/devopsAssig/assig2-gitData/data/dataViz/dataVizFriday.csv")
saved_column = df['Count']
for count in saved_column:
	fridayCount.append(count)

df = pd.read_csv("/home/manick/devopsAssig/assig2-gitData/data/dataViz/DataVizSaturday.csv")
saved_column = df['Count']
for count in saved_column:
	saturdayCount.append(count)

df = pd.read_csv("/home/manick/devopsAssig/assig2-gitData/data/dataViz/dataVizSunday.csv")
saved_column = df['Count']
for count in saved_column:
	sundayCount.append(count)

fig = plt.figure() 
fig.suptitle('Hourly Commit Comparison on Daily basis - Data Visualization', fontsize=18)


ax = fig.add_subplot( 2, 4, 1 )
width = 0.5
ax.bar(index, sundayCount, width,color='#AF6604',linewidth=0)
plt.xticks(range(0,len(hour)),hour,fontsize=8)
ax.annotate("Sunday",xy=(1,1),xytext=(1,1.8))
plt.xlabel('Hour')
plt.ylabel("Commit Count")


ax2 = fig.add_subplot( 2, 4, 2 )
width = 0.5
ax2.bar(index, mondayCount, width,color='#E6E6FA',linewidth=0)
plt.xticks(range(0,len(hour)),hour,fontsize=8)
ax2.annotate('Monday', xy=(1, 1), xytext=(1, 0.9))
plt.xlabel('Hour')


ax3 = fig.add_subplot(2,4,3)
width = 0.5 
rect2 = plt.bar(index, tuesdayCount, width,color='#FFA500',linewidth=0)
plt.xticks(range(0,len(hour)),hour,fontsize=8)
ax3.annotate('Tuesday', xy=(1, 1), xytext=(1, 1.8))
plt.xlabel('Hour')

ax4 = fig.add_subplot(2,4,4)
width = 0.5
rect2 = plt.bar(index , wednesdayCount, width,color='green',linewidth=0)
plt.xticks(range(0,len(hour)),hour,fontsize=8)
plt.annotate('Wednesday', xy=(1, 1), xytext=(1, 0.9))
plt.xlabel('Hour')

ax5 = fig.add_subplot(2,4,5)
width = 0.5
rect2 = plt.bar(index, thursdayCount, width,color='yellow',linewidth=0)
plt.xticks(range(0,len(hour)),hour,fontsize=8)
plt.annotate('Thursday', xy=(1, 1), xytext=(1, 3.8))
plt.xlabel('Hour')
plt.ylabel("Commit Count")

ax6 = fig.add_subplot(2,4,6)
width = 0.5
rect2 = plt.bar(index, fridayCount, width,color='#6AAEF9',linewidth=0)
plt.xticks(range(0,len(hour)),hour,fontsize=8)
plt.annotate('Friday', xy=(1, 1), xytext=(1, 1.8))
plt.xlabel('Hour')

ax6 = fig.add_subplot(2,4,7)
width = 0.5 
rect2 = plt.bar(index, saturdayCount, width,color='#05356A',linewidth=0)
plt.xticks(range(0,len(hour)),hour,fontsize=8)
plt.annotate('Saturday', xy=(1, 1), xytext=(1, 0.8))
plt.xlabel('Hour')


plt.show()
