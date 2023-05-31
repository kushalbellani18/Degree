import sys

def isOperator(p):
	if p in ['+', '-', '/', '*']:
		return 1

	return 0

def str2Arr(s):
	arr = []

	temp = ""
	i = 0
	while(s[i] != '$'):
		#print("|", i, "|-> ", s[i], " = ", isOperator(s[i]))
		if(isOperator(s[i]) == 1):
			if temp != '': arr.append(temp)
			temp = ""

			arr.append(s[i])
		else:
			temp += s[i]

		i += 1

	#print("~~> ", temp)
	arr.append(temp)

	return arr

def check_num(arr):
	for ai in arr:
		if ai not in "0123456789.":
			return False

	return True

def type_checking(arr):
	for i in range(0, len(arr)):
		if(isOperator(arr[i]) == 1):
#			print("i-1: ", i-1, " -> ", arr[i-1])
#			print("i: ", i, " -> ", arr[i])
#			print("i+1: ", i+1, " -> ", arr[i+1])

			if i-1 == -1 or i+1 == len(arr):
				if arr[i] == '*' or arr[i] == '/':
					return False

				# Check a number
				if(check_num(arr[i+1]) == False):
					return False

				if arr[i+1] == '':
					return False

			else:
				if arr[i] != '+':
					if check_num(arr[i-1]) == False or check_num(arr[i+1]) == False:
						return False

#		print("")

	return True

if __name__ == "__main__":
	s = sys.argv[1] + '$'
#	print(" ---> ", s, " <---")

	arr = str2Arr(s)

#	print(arr)

	if type_checking(arr) == True:
		print("Type checking is TRUE")
	else:
		print("Type checking is ERROR")
