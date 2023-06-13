def getFood(d, index):
	print("+==================+")
	print("|                  |")
	print("| " + str(d[index][1]) + " by " + " |")
	print("|\t " + str(d[index][0]) + " |")
	print("|                  |")
	print("+==================+")

	tot = 0
	t = int(input("---> Presentation: "))
	tot += t
	t = int(input("---> Taste: "))
	tot += t
	t = int(input("---> Hygiene: "))
	tot += t

	return [tot, index]

def enterData():
	name = input("What your name? ")
	food = input("What your cook food name? ")
	print("")

	return [name, food]

if __name__ == "__main__":
	print("\t\t=========|> MasterChef <|========")
	data = []
	arr = []

	for i in range(0, 2):
		data.append(enterData())

	for j in range(0, 2):
		arr.append(getFood(data, j))

	resultIndex = max(arr)

	print("\t Winner is: " + str(data[resultIndex[1]]))
