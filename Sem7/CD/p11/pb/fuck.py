import sys

def isOperator(op):
	if op in ['+', '-', '/', '*']:
		return True

	return False

def str2Arr(str):
	arr = []
	temp = ""

	i = 0
	while(True):
		if str[i] == "$":
			if temp != '': arr.append(temp)
			break
		if isOperator(str[i]):
			if temp != '': arr.append(temp)
			temp = ''

			arr.append(str[i])
		else:
			temp += str[i]

		i += 1

	return arr

def type_checking(arr):
	for i in range(0, len(arr)):
		if isOperator(arr[i]) == True:
			if i == -1:
				if arr[i] == '*' or arr[i] == '/':
					return False

				if not arr[i+1].isdigit():
					return False

			elif i == len(arr) - 1:

				return False

			else:
				if arr[i] != '+':
					if not arr[i-1].isdigit() or not arr[i+1].isdigit():
						return False

	return True

if __name__ == "__main__":
	s = sys.argv[1] + "$"

	a = str2Arr(s)
#	print(a)

	print("The operator is ", type_checking(a))
