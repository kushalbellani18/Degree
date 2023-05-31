if __name__ == "__main__":
	r = int(input("Enter a radius: "))
	arr = []

	x = -r
	while(x <= r):
		y = -r
		while(y <= r):
			if( (x**2 + y**2) == r**2):
				arr.append(
					[x, y]
				)

			y += 1
		x += 1

	print("Arr: ", arr)
	print("Length of arr: ", len(arr))
