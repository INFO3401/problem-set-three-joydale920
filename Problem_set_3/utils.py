import pandas as pd
import matplotlib.pyplot as plt 


def loadAndCleanData(filename):
	data = pd.read_csv(filename)
	fixed_data = data.fillna(0)
	return fixed_data

def computerPDF(sD,data):
	data[sD].plot.kde()
	plt.show()

	# generate KDE plot for each feature in data
	# [sD] access specific column in the dataframe
	# call my graph 
	# data[sD].plot.kde()
	# show my graph
	# plt.show()


def viewDistribution(column,data):
	data[column].plot.hist()
	plt.show()

#def viewLogDistribution --> help

def computeBins(column, data):
	dfcut = pd.qcut(data[column],q=3, duplicates = "drop")
	catList = dfcut.cat.categories.tolist()
	return catList


def computeDefaultRisk(column,bin,sD,data):
	data = data[(data[sD] >= bin[0]) & (df[feature] <=bin[1])]
	rating_probs = data.groupby(column).size().div(len(data))
	print(rating_probs)


# Office hours for 11-18 =(


	
