if __name__ == "__main__":
	arr = []
	posArr =[]
	negArr = []

	n = int(input("Enter a number of items: "))
	for i in range(0, n):
		arr.append(int(input("Enter item - " + str(i+1) + ": ")))

		if(arr[i] >= 0):
			posArr.append(arr[i])
		else:
			negArr.append(arr[i])

	tot = []
	for i in range(0, len(posArr)):
		for j in range(0, len(negArr)):
			tot.append([abs(posArr[i] + negArr[j]), posArr[i], negArr[j]])


	print(tot)
	print("Answer: " + str(min(tot)))
