def bipartitile(arr, index):
	a = []

	for i in range(0, len(arr)):
		t = []
		for j in range(0, len(arr[i])):
			if(arr[i][j] == 1):
				t.append(index[j])
		a.append(t)

	#print(a)
	x = [a[0][0]]
	indexX = []
	for i in range(0, len(a)):
		if(x[0] in a[i]):
			for e in a[i]:
				x.append(e)
			indexX.append(i)
		else:
			for iX in x:
				if(iX in a[i]):
					for e in a[i]:
						x.append(e)
					indexX.append(i)
					break

	y = []
	indexY = []
	for j in range(0, len(a)):
		if(index[j] not in indexX):
			for e in a[j]:
				y.append(e)
			indexY.append(j)

	print("X: ", set(x))
	print("Y: ", set(y))

	count = 0
	for i in x:
		for j in y:
			if i == j:
				count += 1

	if(count == 0):
		print("Bipartitle")
	else:
		print("Not Bipartitle")

if __name__ == "__main__":
	n = int(input("Enter a number of nodes: "))

	data = []
	index = []

	for i in range(0, n):
		data.append(
			list(map(int, input().split()))
		)

		index.append(i)

	bipartitile(data, index)
