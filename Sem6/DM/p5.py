import networkx as nx
import matplotlib.pyplot as plt

def copyData(arr):
	arr2 = []
	for i in range(0, len(arr)):
		t = []
		for j in range(0, len(arr[i])):
			t.append(arr[i][j])

		arr2.append(t)

	return arr2

def bipartitle(arr, index):
	x = []
	y = []
	a = []
	lol = 0

	for i in range(0, len(arr)):
		t = []
		for j in range(0, len(arr[i])):
			if(arr[i][j] == 1):
				t.append(index[j])

		a.append(t)

	x = [0]
	indexX = []
	for es in range(0, len(a)):
		if(x[0] in a[es]):
			for e in a[es]:
				x.append(e)
			indexX.append(es)
		else:
			for iX in x:
				if(iX in a[es]):
					for e in a[es]:
						x.append(e)

					indexX.append(es)
					break

	indexY = []
	for es in range(0, len(a)):
		if(es not in indexX):
			for e in a[es]:
				y.append(e)
			indexY.append(es)

	print("Y: ", list(set(y)))
	#print(indexY)

	print("X: ", list(set(x)))
	#print(indexX)

	count = 0
	for i in x:
		for j in y:
			if i == j:
				count += 1

	if(count == 0):
		print("Bipartitle")
	else:
		print("Failed!")

	# ---------->>>> Display a graph with the help of networkx library <<<<----------

	colorMap = []
	for i in range(0, len(index)):
		if index[i] in x:
			#print(index[i])
			colorMap.append('green')
		else:
			colorMap.append('blue')

	g = nx.Graph()

	# Add nodes
	g.add_nodes_from([i for i in index])

	# Add edges
	for i in range(0, len(a)):
		for j in a[i]:
			print(str(i) + ", " + str(j))
			g.add_edge(i, j)

	nx.draw_circular(g, node_color=colorMap, with_labels=True)
	plt.show()

if __name__ == "__main__":
	n = int(input("Enter a number of node: "))

	data = []
	index = []

	for i in range(0, n):
		data.append(
			list(map(int, input().split()))
		)

		index.append(i)

	#print(data)
	data2 = copyData(data)
	bipartitle(data, index)
