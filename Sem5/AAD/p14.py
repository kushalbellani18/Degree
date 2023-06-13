if __name__ == "__main__":
	data = [ [0, 1, None, 4, None, None, None],
		 [1, 0, 2, 6, 4, None, None],
		 [None, 2, 0, None, 5, 6, None],
		 [4, 6, None, 0, 3, None, 4],
		 [None, 4, 5, 3, 0, 8, 7],
		 [None, None, 6, None, 8, 0, 3],
		 [None, None, None, 4, 7, 3, 0]
	]

	while(True):
		source = int(input("Enter data position: ")) - 1
		if(source <= len(data)):
			break

		print("Enter atmost " + str(len(data)) + "!")

	node = [source]
	edges = []
	totalEdges = 0

	while (len(node) < len(data)):
		for i in range(0, len(data[source])):
			if(data[source][i] != None and data[source][i] != 0 and i not in node):
				edges.append([data[source][i], source, i])

		edges.sort()

		x = 0
		while(x <= len(edges)):
			if(edges[x][2] not in node):
				print(edges[x][1] + 1, " - ", edges[x][2] + 1, " = ", edges[x][0])
				node.append(edges[x][2])
				totalEdges += edges[x][0]
				f = [data[edges[x][1]][edges[x][2]], edges[x][1], edges[x][2]]
				edges.remove(f)

				source = node[-1]

				break

			x += 1

	print([x + 1 for x in node])
	print("Total Edges = ", totalEdges)
