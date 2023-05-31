from tabulate import tabulate # convert raw data to table

def confTruthTable(res):
	# For Transpose Table
	data = []

	for i in range(0, len(res[0])):
		t = []
		for j in range(0, len(res)):
			t.append(res[j][i])

		data.append(t)

	return data

def implication(a, b):
	# a => b formula
	result = []

	for i in range(0, len(a)):
		if(a[i] == b[i] or b[i] == True):
			result.append(True)
		else:
			result.append(False)

	return result

def doubleImplication(a, b):
	# a <=> b formula
	result = []

	for i in range(0, len(a)):
		if(a[i] == b[i]):
			result.append(True)
		else:
			result.append(False)

	return result

def no(a):
	return [not x for x in a]

if __name__ == "__main__":
	p = [True, True, True, True, False, False, False, False]
	q = [True, True, False, False, True, True, False, False]
	r = [True, False, True, False, True, False, True, False]

	z = implication(r, q)
	p2 = no(p)
	ans = doubleImplication(p2, z)

	labelName = ["p", "q", "r", "!p", "r => q", "(!p) <=> (r => q)"]
	result = [p, q, r, p2, z, ans]

	result = confTruthTable(result)

	table = tabulate(result, headers=labelName, tablefmt="pretty")

	print(table)

