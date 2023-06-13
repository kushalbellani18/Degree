if __name__ == "__main__":
	data = [ [0, 1, None, 4, None, None, None],
		 [1, 0, 2, 6, 4, None, None],
		 [None, 2, 0, None, 5, 6, None],
		 [4, 6, None, 0, 3, None, 4],
		 [None, 4, 5, 3, 0, 8, 7],
		 [None, None, 6, None, 8, 0, 3],
		 [None, None, None, 4, 7, 3, 0]
	]

	edges = []
	totalEdges = 0
	node = [0]

	'''for i in range(0, len(data)):
		for j in range(0,len(data[i])):
			if(data[i][j] != 0 and data[i][j] != None):
				if([data[i][j], j, i] not in edges):
					edges.append([data[i][j], i, j])
	'''

	print("============================")

	x = 0
	while(x < len(data)):
		for i in range(0, len(node)):
			for j in range(0, len(data[node[i]])):
				if(data[node[i]][j] != 0 and data[node[i]][j] != None):
					if([data[node[i]][j], j, node[i]] not in edges):
						edges.append([data[node[i]][j], node[i], j])


		edges.sort()

		for y in range(0, len(edges)):
			if(edges[y][1] not in node or edges[y][2] not in node):

				print(edges[y][1] + 1, " - ", edges[y][2] + 1, " ==> ", edges[y][0])

				if(edges[y][1] not in node):
					node.append(edges[y][1])
				if(edges[y][2] not in node):
					node.append(edges[y][2])

				totalEdges += edges[y][0]
				edges.remove([edges[y][0], edges[y][1], edges[y][2]])

				break

		x += 1

	print(node)
	print(totalEdges)
