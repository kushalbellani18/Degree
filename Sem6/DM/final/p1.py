import random

def dataGroup(choice):
	if choice == 1:
		data = [x for x in range(-10000, 10001)]
	elif choice == 2:
		data = [x for x in range(0, 10001)]
	else:
		data = [x for x in range(-10000, 1)]

	return data

def isMonoid(dataSet, a, b, op):
	if op == '+':
		if a in dataSet and b in dataSet and (a+b) in dataSet:
			return True

	if op == '-':
		if a in dataSet and b in dataSet and (a-b) in dataSet:
			return True

	if op == '*':
		if a in dataSet and b in dataSet and (a*b) in dataSet:
			return True

	if op == '/':
		if a in dataSet and b in dataSet and (a/b) in dataSet:
			return True

	return False

if __name__ == "__main__":
	print("1) Z*")
	print("2) Z+")
	print("3) Z-")
	print("")
	choice = int(input("Enter choice: "))

	dataSet = dataGroup(choice)

#	print("Dataset: ", dataSet)

	a = int(input("Enter a: "))
	b = int(input("Enter b: "))
	op = input("Enter op: ")

	if isMonoid(dataSet, a, b, op):
		print("Yes, it is Monoid!")
	else:
		print("No, it isn't Monoid!")
