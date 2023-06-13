re = []

def display(arr):
	print("---------------------------------")
	for i in range(0, len(arr)):
		for j in range(0, len(arr[i])):
			print(arr[i][j], end="\t")
		print("")
	print("---------------------------------")

def set(t):
	global re

	for i in range(0, len(t)):
		r = []
		for j in range(0, len(t[i])):
			r.append(t[i][j])

		re.append(r)

def reset(t):
	global re

	for i in range(0, len(re)):
		for j in range(0, len(re[i])):
			t[i][j] = re[i][j]

	return t

def update(t):
	global re

	for i in range(0, len(t)):
		for j in range(0, len(t[i])):
			re[i][j] = t[i][j]

def setNone(t, index):
	# For Row wise
	for i in range(0, len(index) - 1):
		for x in range(0, len(t)):
			t[index[i]][x] = None

	# For Column wise
	for i in range(1, len(index)):
		for y in range(0, len(t)):
			t[y][index[i]] = None

	for i in range(1, len(index)):
		t[index[i]][index[0]] = None

	return t

def travelingSalesProblem(a, path, costs):
	global re
	index = [i for i in range(0, len(a)) if i not in path]

	if(len(index) == 0):
		path.append(path[0])
	else:
		c = []

		for i in range(0, len(index)):
			path.append(index[i])
			a = setNone(a, path)

			row = 0
			col = 0

			for x in range(0, len(a)):
				ct = []
				for y in range(0, len(a[x])):
					if(a[x][y] != None):
						ct.append(a[x][y])

				if(len(ct) != 0):
					row += min(ct)

			for x in range(0, len(a)):
				ct = []
				for y in range(0, len(a[x])):
					if(a[y][x] != None):
						ct.append(a[y][x])

				if(len(ct) != 0):
					col += min(ct)

			a = reset(a)

			c.append(costs[-1] + (row + col) + re[path[-2]][path[-1]])

			path.remove(index[i])

		minimumIndex = 0
		minimumValue = c[minimumIndex]
		for i in range(1, len(c)):
			if(minimumValue > c[i]):
				minimumValue = c[i]
				minimumIndex = i

		path.append(index[minimumIndex])
		costs.append(minimumValue)

		travelingSalesProblem(a, path, costs)


if __name__ == "__main__":
	mainArr = [
		[None, 12, 10, 0, 0, 0, 12],
		[12, None, 8, 12, 0, 0, 0],
		[10, 8, None, 11, 3, 0, 9],
		[0, 12, 11, None, 11, 10, 0],
		[0, 0, 3, 11, None, 10, 7],
		[0, 0, 0, 10, 6, None, 9],
		[12, 0, 9, 0, 7, 9, None]
	]

	arr = [
		[None, 12, 10, 0, 0, 0, 12],
		[12, None, 8, 12, 0, 0, 0],
		[10, 8, None, 11, 3, 0, 9],
		[0, 12, 11, None, 11, 10, 0],
		[0, 0, 3, 11, None, 10, 7],
		[0, 0, 0, 10, 6, None, 9],
		[12, 0, 9, 0, 7, 9, None]
	]

	display(mainArr)

	rowReduction = 0
	for i in range(0, len(arr)):
		a = []
		for j in range(0, len(arr[i])):
			if(arr[i][j] != None):
				a.append(arr[i][j])

		rowReduction += min(a)

		for j in range(0, len(arr[i])):
			if(arr[i][j] != None):
				arr[i][j] -= min(a)

	colReduction = 0
	for i in range(0, len(arr)):
		a = []
		for j in range(0, len(arr)):
			if(arr[i][j] != None):
				a.append(arr[j][i])

		colReduction += min(a)

		for j in range(0, len(arr[i])):
			if(arr[j][i] != None):
				arr[j][i] -= min(a)

	display(arr)

	t = []
	for i in range(0, len(arr)):
		a = []
		for j in range(0, len(arr[i])):
			a.append(arr[i][j])
		t.append(a)

	set(t)

	path = [0]
	cost = [rowReduction + colReduction]
	travelingSalesProblem(t, path, cost)

	print("Path: ", path)
	print("Cost: ", cost[-1])

	print("Routie")
	for i in range(1, len(path)):
		print(path[i-1], ' -> ', path[i], ': ', mainArr[path[i-1]][path[i]])
