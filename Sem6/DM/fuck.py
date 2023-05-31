def algo(inital, goal, arr):
	current = initial
	q1 = []
	q2 = []
	history = []

	q2.append(current)
	history.append(None)

	while(True):
		if(current == goal):
			print("BOOM! Successfully!")
			break

		for i in range(0, len(arr[current])):
			if arr[current][i][1] not in q2:
				c = arr[current][i]
				c.append(current)

				q1.append(c)

		q1.sort()

		c = q1.pop()
		current = c[1]
		q2.append(current)
		history.append(c[2])

	print(history)

if __name__ == "__main__":
	arr = {
		0: [ [3, 1], [3, 2] ],
		1: [ [3, 3], [4, 5] ],
		2: [ [3, 2], [5, 5], [4, 4], [7, 6] ],
		3: [ [3, 1] ],
		4: [ [4, 2], [9, 6], [1, 7] ],
		5: [ [4, 1], [5, 2], [8, 6], [5, 7] ],
		6: [ [8, 5], [9, 4], [7, 2] ],
		7: [ [5, 5], [1, 4] ]
	}

	initial = int(input("Enter an initial: "))
	goal = int(input("Enter a goal: "))

	algo(initial, goal, arr)
