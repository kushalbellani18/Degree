import sys

def replaceBy_T(a):
	if a.isdigit():
		return "t"+a

	return a

def intermediate_code(s):
	arr = [[], [], []]

	t = 1

	ops = ["/", "*", "+", "-"]
	for op in ops:
		i = 0
		while(i < len(s)):
			if(s[i] == op):
				arr[0].append(s[i])
				arr[1].append(replaceBy_T(s[i-1])+s[i]+replaceBy_T(s[i+1]))
				arr[2].append("t"+str(t))

				o = s[i-1]+s[i]+s[i+1]
				o2 = str(t)
				t += 1

				s = s.replace(o, o2)
				#print(s)

				i = -1

			i += 1

	s = "t" + s

	return s, arr

def table(arr, s):
	for i in range(0, len(arr[0])):
		print(arr[0][i], "\t", arr[1][i], "\t", arr[2][i])

	print("Final: ", s)

if __name__ == "__main__":
	s = sys.argv[1]

	s, arr = intermediate_code(s)

	table(arr, s)
