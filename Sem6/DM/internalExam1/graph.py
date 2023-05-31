def display(arr):
	print("+------------------------------+")
	for i in range(0, len(arr)):
		for j in range(0, len(arr[i])):
			print(arr[i][j], end=" ")

		print("")

	print("+------------------------------+")

def cyclicGraph(arr):
	print("So sad! Opening soon!")

	return False

if __name__ == "__main__":
	arr = [
		[0, 1, 0, 0, 0, 0],
		[-1, 0, 1, 0, -1, 0],
		[0, -1, None, 1, 0, 0],
		[0, 0, -1, None, 1, 1],
		[0, 1, 0, -1, None, 0],
		[0, 0, 0, -1, 0, None]
	]

	display(arr)

	ans = cyclicGraph(arr)
