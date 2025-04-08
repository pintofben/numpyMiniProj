# Ben Pintof
# numpy/matplotlib Mini Project
# Scientific Computing

import numpy as np
from numpy import random

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of chairs per row: "))

if __name__=='__main__':
	grid = np.array ( [] )
	nameList = ["Ben", "Nate", "Ella", "Gabriella", "Nathaniel", "Benjamin", "Ethan", "Brown", "Elliot", "Harry", "Harrison", "Jerry",
			"Hannah", "Andrew", "Geneen", "Jeff", "Samantha", "Joey", "Juliana", "Griff", "Dan", "Daniel", "John", "Mike",
			"Michael", "Eugene", "Bob", "Robert", "Sofia", "Karly", "Kole", "Kerry", "Matt", "Edward", "Eddie", "Rohn", "Jack",
			"Owen", "Shane", "Aiden", "Molly", "Sara", "Sarah", "Abby", "Paul"]
	# HARDCODING a 2x3 grid filled with randomly selected name
	for i in range(rows):
		for j in range(columns):
			num = f'({i}, {j})'
			randName = random.choice(nameList)
			NameNum = f'{randName} {num}'
			# append randName to grid
			grid = np.append(grid,NameNum)
			# remove randName from randList
			nameList.remove(randName)
        # done with the grid and pring the 1D grid
	grid = grid.reshape(rows,columns)

	for s in range(rows):
		for l in range(columns):
			if l < columns - 1:
				print(grid[s, l], end = '            ')
			else:
				print(grid[s, l], end ='\n \n')
