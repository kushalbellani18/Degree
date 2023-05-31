def minDistanceIndex(d, vI):
	min = float('inf')
	minIndex = -1

	for i in range(0, len(d)):
		if(d[i] < min and vI[i] == False):
			min = d[i]
			minIndex = i

	return minIndex

def dijkastraAlgo(arr, startVertex):
	d = [float('inf') for i in range(0, len(arr))]
	d[startVertex] = 0
	visitedIndex = [False for i in range(0, len(arr))]

	for i in range(0, len(arr)):
		x = minDistanceIndex(d, visitedIndex)

		if x == -1:
			print("Oops!")
			break

		visitedIndex[x] = True
		for y in range(0, len(arr)):
			if(arr[x][y] != None and visitedIndex[y] == False and d[y] > d[x] + arr[x][y]):
				d[y] = d[x] + arr[x][y]

	print("Source Vertex to every Vertex: ")
	for i in range(0, len(d)):
		print(str(startVertex) + " --> " + str(i) + ": " + str(d[i]))

if __name__ == "__main__":

	arr = [
		[None, 3, 3, None, None, None, None, None],
		[3, None, None, 4, None, None, None, None],
		[3, None, None, None, 4, 5, 7, None],
		[None, 3, None, None, None, None, None, None],
		[None, 4, None, None, None, None, 9, 1],
		[None, 4, 5, None, None, None, 8, 5],
		[None, None, 7, None, 9, 8, None, None],
		[None, None, None, None, 1, 5, None, None]
	]

	startVertex = int(input("Enter a start vertex: "))

	dijkastraAlgo(arr, startVertex)
