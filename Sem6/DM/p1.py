if __name__ == "__main__":
	print("Create a new set: ")
	mySet = set()
	print(mySet)
	print(type(mySet))

	print("")

	print("Create a non empty set: ")
	l = []
	print("Enter any 5 numbers: ")
	for i in range(0, 5):
		b = int(input())
		l.append(b)

	mySet2 = set(l)
	print(mySet2)
	print(type(mySet2))

	print("")

	print("Using a literal: ")
	msg = input("Enter a string value with space: ")
	l = msg.split(' ')
	l2 = list(mySet2)

	l2 += l

	mySet3 = set(l2)
	print(mySet3)
	print(type(mySet3))

	print("")

	print("New Member in the set: ")
	msg = input("Enter: ")

	mySet3.add(msg)

	print(mySet3)
	print(type(mySet3))

