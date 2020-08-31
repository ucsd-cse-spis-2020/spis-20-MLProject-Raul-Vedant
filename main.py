print(__doc__)

# Author: Nelle Varoquaux <nelle.varoquaux@gmail.com>
#         Alexandre Gramfort <alexandre.gramfort@inria.fr>
# License: BSD

# Imports the following modules in order to establish a graph
import matplotlib.pyplot as plt
import csv
import pandas as pd
import random




def dataPoints():
	'''
	Opens, reads, and prints day and player data from the csv file
	'''
	pd.read_csv("chart.csv")
	dataFile = "chart.csv"

	# Opens the csv file
	# Accounts for any errors in the file
	with open(dataFile, 'r') as csvfile:
		
		# Begins to read the csv file 
		# Skips the column headers
		pointreader = csv.reader(csvfile)
		next(pointreader)
		
		# Loops through each row of the csv file 
		# Displays date/time and number of players
		for row in pointreader:
			print(row[0], row[1] + " players")
	

		


#dataPoints()


def graph():
	'''
	Creates a graph based on recorded data and predictive data 
	'''
	# Creates a list for the x and y coordinates
	x = []
	y = []
	
	# Begins after the csv file has been processed
	# Each value is a day after recorded data
	i = 1
	n = 300
	
	# Creates a list of potential events which would affect the behavior of the predictive model, each in their different ways
	events = ['normal', 'server failure', 'game changing update']
	
	# Creates a list multiNum containing the number of days that correspond to each event in events list occurring
	multiNum = [362, 1, 2]
	c = sum([[s] * n for s, n in zip(events, multiNum)], [])
	
	# Opens the csv file to read it
	# Distinguishes between date/time and player count
	with open('chart.txt','r') as csvfile:
		
		# Reads csv file and splits up data between axis, with a comma acting as the boundary 
		plots = csv.reader(csvfile, delimiter=',')
		next(csv.reader(csvfile))
		
		# For each row of data in plots, append the time and day values to list x, with the number of concurrent players per day being appended to list y
		for row in plots:
			x.append((row[0]))
			y.append(int(row[1]))
		
		# Loops as long as the given day does not pass the total number of days specififed
		while i < n:
			
			# Certain behavoir triggers based on the event the computer randomly chose
			randEvent = random.choice(c)
			
			if randEvent == 'normal':
				x.append(str(i) + ' days after data')
				y.append(y[-1] * random.uniform(0.97, 1.02))
			if randEvent == 'game changing update':
				x.append(str(i) + ' days after data')
				y.append(y[-1] * random.uniform(0.99, 1.05))
			if randEvent == 'server failure':
				x.append(str(i) + " days after data")
				y.append(y[-1] * 0.15)
				# Prevents the program from plotting points that are dependent from the server failure
				# 'Recovery' state allows the program to plot reasonable points again
				x.append('recovery')
				y.append(y[-2])
			# Increases to indicate the next day after recorded data
			i += 1
		
		# Plots the data (both from the csv file along with the predictive model); Labels each axis, title, and legend, and sets a boundary line defining where the original csv data ends and the prediction begins
		plt.plot(y, label='new') #x parameter was taken out
		plt.axvline(x = 3031, ymin = 0, ymax = 1, label = 'start of prediction', color = 'red')
		plt.xlabel('Days After Launch')
		plt.ylabel('Concurrent Players (Hundred Thousands)')
		plt.title('Number of Concurrent Players per Day\n Counter Strike Global Offensive')
		plt.legend()
		plt.show()

# Calls the f
graph()


# STUFF TO DO:
# Add more key events
# 
# Extend predictive reliability for greater than 1 year
# Import a picture for the picture of game for the corresponding data
# Account for different trends based on video game/genre; different genres would have different long-term numbers


