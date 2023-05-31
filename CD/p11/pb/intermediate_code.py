import sys

def findOperator(s, op):
	for i in range(0, len(s)):
		if s[i] == op:
			return i

	return -1

def is_num(a):
	if a in "0123456789":
		a = "t" + a

	return a

def intermediate_code(s):
	arr = [[], [], []]

	t = 1

	ops = ['/', '*', '+', '-']
	for op in ops:
		i = 0
		while(i < len(s)):
			if s[i] == op:
				arr[0].append(s[i])
				arr[1].append(is_num(s[i-1])+s[i]+is_num(s[i+1]))
				arr[2].append("t" + str(t))

				o = s[i-1] + s[i] + s[i+1]
				o2 = str(t)

				s = s.replace(o, o2)
				t += 1

				i = -1

			i += 1


	s = "t" + s

	return s, arr

def table(arr):
	for i in range(0, len(arr[0])):
		print(arr[0][i], "\t", arr[1][i], "\t", arr[2][i])

	print("")

if __name__ == "__main__":
	s = sys.argv[1]

	s, arr = intermediate_code(s)

	table(arr)
	print("Final: ", s)
