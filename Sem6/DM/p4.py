def dijkstraAlgo(inital, goal, arr):
	current = inital
	q1 = []
	q2 = []
	history = []

	q2.append(current)
	history.append(None)

	while(True):
		if(current == goal):
			print("FOUND!")
			print("q2: ", q2)
			print("history: ", history)

			s = []
			index = -1
			s.append(q2[index])

			while(True):
				if(history[index] == None):
					break

				# Get index
				for i in range(0, len(q2)):
					if(q2[i] == history[index]):
						index = i
						break

				s.append(q2[index])

			print(">> s: ", s)
			break

		for i in range(0, len(arr[current])):
			print(">>>>>>>> " + str(arr[current][i][1]) + " not in " + str(q2) + " = " + str(arr[current][i][1] not in q2)) 
			if(arr[current][i][1] not in q2):
				c = arr[current][i]
				c.append(current)

				q1.append(c)

		q1.sort()

		print("\n Before Sort: ")
		print("Q1: ", q1)
		print("Q2: ", q2)
		print("_____________")

		c = q1.pop(0)
		current = c[1]
		q2.append(current)
		history.append(c[2])

		print("\n After Sort: ")
		print("Q1: ", q1)
		print("Q2: ", q2)
		print("_____________")

	i = len(s) - 1
	totEdge = 0
	while(i >= 0):
		print(s[i], end=" ")

		if((i-1) != -1):
			for lol in range(0, len(arr[s[i]])):
				if( s[i-1] == arr[s[i]][lol][1] ):
					totEdge += arr[s[i]][lol][0]

					break

		i -= 1

	print("")
	print("Total Edge: ", totEdge)

if __name__ == "__main__":
	arr = {
		0: [[3,1], [3,2]],
		1: [[3,0], [3,3], [4,5]],
		2: [[3,0], [5,5], [4,4], [7,6]],
		3: [[3,1]],
		4: [[4,2], [9,6], [1,7]],
		5: [[4,1], [5,2], [8,6]],
		6: [[9,4], [7,2], [8,5]],
		7: [[1,4], [5,5]]
	}

	#print(arr)

	initial = int(input("Enter initial: "))
	goal = int(input("Enter goal: "))

	dijkstraAlgo(initial, goal, arr)

