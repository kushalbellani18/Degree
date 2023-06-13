def min(a, b):
	if(a == None and b == None):
		return None
	elif(a == None):
		return (b+1)
	elif(b == None):
		return a

	if(a > (b+1)):
		return (b+1)
	return a

def findCharges(arr, coins):
	i = len(arr)

	mark = []

	i -= 1
	j = len(arr[i]) - 1
	while(j >= 0 and i >= 0):
		# print(i, "  ", j, " -> ", arr[i][j])
		mark.append(arr[i][j])
		if(arr[i][j] != arr[i-1][j]):
			j -= coins[i]
		else:
			i -= 1

	return mark

def getResult(coins, c):
	arr = []
	for x in range(0, len(coins)):
		a = []
		for y in range(0, c):
			a.append(None)
		arr.append(a)

	i = 0
	while(i < len(coins)):
		j = 0
		while(j < c):
			if(j == 0):
				arr[i][j] = 0
			else:
				if(i == 0):
					if((j - coins[i]) < 0):
						arr[i][j] = None
					else:
						if(arr[i][j-coins[i]] != None):
							arr[i][j] = 1 + arr[i][(j-coins[i])]
						else:
							arr[i][j] = None
				else:
					if(j < coins[i]):
						arr[i][j] = arr[i-1][j]
					else:
						arr[i][j] = min(arr[i-1][j], arr[i][j-coins[i]])

			j += 1
		i += 1

	return arr

def findCoins(givenCharges, coins, nCharges, index):
	extraCharges = givenCharges
	index -= 1
	answer = []
	indexTough = len(coins) - 1

	if(index == -1):
		print("+------------------+")
		print("  Failed!  ")
		print("+------------------+")

	extraCharges -= coins[index]
	answer.append(coins[index])

	for i in range(1, nCharges):
		if(extraCharges < coins[indexTough]):
			indexTough -= 1

		extraCharges -= coins[indexTough]
		answer.append(coins[indexTough])


		if(extraCharges <= -1):
			break


	if(givenCharges != sum(answer)):
		findCoins(givenCharges, coins, nCharges, index)
	else:
		print("+-----------------------+")
		print("|  |> Final Answer <|   |")
		print("   >> " + str(answer) + " <<")
		print("|                       |")
		print("+-----------------------+")


if __name__ == "__main__":
	n = int(input("Enter a number of coins: "))
	coins = []
	for i in range(0, n):
		c = int(input("Coins " + str(i + 1) + ": "))
		coins.append(c)

	charge = int(input("Enter a charge: "))

	arr = getResult(coins, charge+1)

	print("----------------------------------")
	print("")

	for r in range(0, len(arr)):
		for c in range(0, len(arr[r])):
			print(arr[r][c], end=" | ")
		print("")

	print("")
	print(" --------------- ")
	print("")

	m = findCharges(arr, coins)
	ma = m[0] # <-- Finally, get value very well...
	print("Number of Charges: " + str(ma))
	print("")
	print(" --------------- ")
	print("")

	findCoins(charge, coins, ma, len(coins))
