def copyData(arr):
	a = []

	for i in range(0, len(arr)):
		t = []
		for j in range(0, len(arr[i])):
			t.append(arr[i][j])
		a.append(t)

	return a

def display(arr):
	print("+==============+\n")

	for r in range(0, len(arr)):
		for c in range(0, len(arr[r])):
			print(arr[r][c], end=" ")
		print("")

	print("\n+==============+\n")

def scanZero(arr):
	x = 0

	while(x < len(arr)):
		y = 0
		while(y < len(arr[x])):
			if(arr[x][y] == 0):
				return x, y
			y += 1
		x += 1

def bfs(initialState, goalState):
	frontier = []
	exploredSet = []

	frontier.append(initialState)
	exploredSet.append(initialState)

	t = 0
	while(True):
		t += 1

		if(exploredSet[-1] == goalState):
			t += 1
			print(">>>>>>>>>>>> Woohoo! Success! <<<<<<<<<<<<<")
			print("Time: ", t)
			print("Number of states: ", len(exploredSet))
			break

		t += 1

		a = copyData(exploredSet[-1])
		b = copyData(a)
		i, j = scanZero(a)
		t += 3

		# Move Left side
		if( (j-1) >= 0):
			t += 1

			a[i][j], a[i][j-1] = a[i][j-1], a[i][j]
			t += 1

			if(a not in exploredSet):
				frontier.append(a)
				t += 2

			a = copyData(b)
			t += 1

		# Move Right side
		if( (j+1) < 3):
			t += 1

			a[i][j], a[i][j+1] = a[i][j+1], a[i][j]
			t += 1

			if(a not in exploredSet):
				frontier.append(a)
				t += 2

			a = copyData(b)
			t += 1

		# Move Upward direction
		if( (i-1) >= 0):
			t += 1

			a[i][j], a[i-1][j] = a[i-1][j], a[i][j]
			t += 1

			if(a not in exploredSet):
				frontier.append(a)
				t += 2

			a = copyData(b)
			t += 1

		# Move Downward direction
		if( (i+1) < 3):
			t += 1

			a[i][j], a[i+1][j] = a[i+1][j], a[i][j]
			t += 1

			if(a not in exploredSet):
				frontier.append(a)
				t += 2

			a = copyData(b)
			t += 1

		fine = frontier.pop(0)
		exploredSet.append(fine)
		t += 2

def dfs(initialState, goalState):
	frontier = []
	exploredSet = []

	frontier.append(initialState)
	exploredSet.append(initialState)

	t = 0
	while(True):
		t += 1

		if(exploredSet[-1] == goalState):
			t += 1
			print(">>>>>>>>>>>> Woohoo! Success! <<<<<<<<<<<<<")
			print("Time: ", t)
			print("Number of states: ", len(exploredSet))
			break

		a = copyData(exploredSet[-1])
		b = copyData(a)
		i, j = scanZero(a)
		t += 3

		# Move Left side
		if( (j-1) >= 0):
			t += 1

			a[i][j], a[i][j-1] = a[i][j-1], a[i][j]
			t += 1

			if(a not in exploredSet):
				frontier.append(a)
				t += 2

			a = copyData(b)
			t += 1

		# Move Right side
		if( (j+1) < 3):
			t += 1

			a[i][j], a[i][j+1] = a[i][j+1], a[i][j]
			t += 1

			if(a not in exploredSet):
				frontier.append(a)
				t += 2

			a = copyData(b)
			t += 1

		# Move Upward direction
		if( (i-1) >= 0):
			t += 1

			a[i][j], a[i-1][j] = a[i-1][j], a[i][j]
			t += 1

			if(a not in exploredSet):
				frontier.append(a)
				t += 2

			a = copyData(b)
			t += 1

		# Move Downward direction
		if( (i+1) < 3):
			t += 1

			a[i][j], a[i+1][j] = a[i+1][j], a[i][j]
			t += 1

			if(a not in exploredSet):
				frontier.append(a)
				t += 2

			a = copyData(b)
			t += 1

		fine = frontier.pop()
		exploredSet.append(fine)
		t += 2

def ids(initialState, goalState):
	frontier = []
	exploredSet = []
	node = 0
	maxNode = int(input("Enter a maximum number of node: "))

	frontier.append(initialState)
	exploredSet.append(initialState)

	t = 0
	while(True):
		if(exploredSet[-1] == goalState):
			t += 1
			print(">>>>>>>>>>>>>>>> Wohoo! Success <<<<<<<<<<<<<<<<")
			print("Time: ", t)
			print("Number of states: ", len(exploredSet))
			break

		# Let add data to frontier, if level should be less than 3.
		if(node <= maxNode):
			t += 1

			a = copyData(exploredSet[-1])
			b = copyData(a)
			i, j = scanZero(a)
			t += 3

			# Move left side
			if( (j-1) >= 0):
				t += 1

				a[i][j], a[i][j-1] = a[i][j-1], a[i][j]
				t += 1

				if(a not in exploredSet):
					frontier.insert(1, a)
					t += 2

				a = copyData(b)
				t += 1

			# Move right side
			if( (j+1) < 3):
				t += 1

				a[i][j], a[i][j+1] = a[i][j+1], a[i][j]
				t += 1

				if(a not in exploredSet):
					frontier.insert(1, a)
					t += 2

				a = copyData(b)
				t += 1

			# Move upward side
			if( (i-1) >= 0):
				t += 1

				a[i][j], a[i-1][j] = a[i-1][j], a[i][j]
				t += 1

				if(a not in exploredSet):
					frontier.insert(1, a)
					t += 2

				a = copyData(b)
				t += 1

			# Move downside side
			if( (i+1) < 3):
				t += 1

				a[i][j], a[i+1][j] = a[i+1][j], a[i][j]
				t += 1

				if(a not in exploredSet):
					frontier.insert(1, a)
					t += 2

				a = copyData(b)
				t += 1

			node += 1
			t += 1

		if(len(frontier) != 0):
			fine = frontier.pop()
			exploredSet.append(fine)

			t += 3
		else:
			t += 1
			print(">>>>>>>>>>>>> Oops! Not found! <<<<<<<<<<<<<<")
			print("Time: ", t)
			print("Number of states: ", len(exploredSet))
			break

if __name__ == "__main__":
	initialState = [[0, 2, 3], [1, 4, 5], [8, 7, 6]]
	goalState = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

	print("	------------|> Initial State <|------------")
	display(initialState)
	print("	------------|> Goal State <|------------")
	display(goalState)

	print("	------------|> BFS <|------------ ")
	bfs(initialState, goalState)
	print("----------------------------------------------")
	print("	------------|> DFS <|------------ ")
	dfs(initialState, goalState)
	print("------------------------------------------------")
	print("	------------|> IDS <|------------ ")
	ids(initialState, goalState)
