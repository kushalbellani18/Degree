def maximum(a, b):
	if(a >= b):
		return a
	return b

def knapscakProblem(n, w, profile, weight):
	arr = []

	for r in range(0, n+1):
		arr.append([])
		for c in range(0, w+1):
			arr[r].append(None)

	for i in range(0, n+1):
		for j in range(0, w+1):
			if(i == 0 or j == 0):
				arr[i][j] = 0
			elif(j < weight[i-1]):
				arr[i][j] = arr[i-1][j]
			elif(j >= weight[i-1]):
				arr[i][j] = maximum(arr[i-1][j], profile[i-1] + arr[i-1][(j-weight[i-1])])

	print("-----------------------------")
	print("  =|> Display <|=  ")
	for r in range(0, n+1):
		print("  ", end="  ")
		for c in range(0, w+1):
			print(arr[r][c], end=" ")

		print("")
	print("-----------------------------\n")

	i = len(weight) - 1
	d = w
	l = []
	while i>0 and d>0:
		print("")
		print("------ " + str(i) + " <-> " + str(d) + " ------")
		print(str(arr[i][d]) + " vs " + str(arr[i-1][d]))
		if arr[i][d] != arr[i-1][d]:
			l.append(profile[i-1])
			i -= 1
			d -= weight[i]
			print(">>>>>>", weight[i])
		else:
			i -= 1

	return arr[n][w], l

if __name__ == "__main__":
	'''n = int(input("Enter a number of artifacts: "))
	w = int(input("Enter a limited capacity: "))
	profile = []
	weight = []

	for i in range(0, n):
		c = int(input("P " + str(i + 1) + ": "))
		profile.append(c)

		while(1):
			c = int(input("W " + str(i + 1) + ": "))

			if(c <= w):
				weight.append(c)
				break
			print("No way! it should be less than or equal to ", w, " kgs")
	'''

	n = 4
	w = 5
	profile = [3, 4, 5, 6]
	weight = [2, 3, 4, 5]

	a, l = knapscakProblem(n, w, profile, weight)

	print("Answer: ", a)
	print("List: ", l)
