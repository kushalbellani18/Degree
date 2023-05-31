import sys

def transition(a, table, symbol):
	s = ""

	for ai in a:
		for ti in table:
			if ai == ti[0]:
				s += ti[symbol+1]
				break

	return s

def getIndex(ans, arr):
	t = ""

	for ai in ans:
		for i in range(0, len(arr)):
			if ai in arr[i]:
				t += str(i)

	return t

def update(a, ansIndex, arr):
	if len(set(ansIndex)) == 1:
		return False, a

	else:
		hmmSet = list(set(ansIndex))
		updateData = []

		for hS in hmmSet:
			t = ""

			for iA in range(0, len(ansIndex)):
				if hS == ansIndex[iA]:
					t += a[iA]

			updateData.append(t)

		return True, updateData

def optimizationDFA(arr, table):
	print(arr)
	while True:
		arr2 = []

		for a in arr:
			print(a)
			for i in range(0, 2):
				ans = transition(a, table, i)
				ansIndex = getIndex(ans, arr)

				print(str(i) + ": ", end=" ")
				print(ans, end= " -> ")
				print(ansIndex)

				isUpdate, updateData = update(a, ansIndex, arr)

				if isUpdate == True:
					for uD in updateData:
						arr2.append(uD)

					if a in arr2:
						arr2.remove(a)

					break
				else:
					arr2.append(updateData)

			arr2 = list(set(arr2))
			print("")

		if(set(arr) == set(arr2)):
			break

		print(arr2)

		arr = arr2.copy()

	print("Final ans: ", arr2)
	return arr2

def whereTable(lol, t):
	for l in range(0, len(lol)):
		if t in lol[l]:
			return l

def reduceTable(arr, table):
	table2 = []

	arr2 = ["Q"+str(i) for i in range(1, len(table)+1)]

	for i in range(0, len(arr)):
		t = [arr2[i]]

		for ti in table:
			if ti[0] == arr[i][0]:
				index = whereTable(arr, ti[1])
				t.append(arr2[index])

				index = whereTable(arr, ti[2])
				t.append(arr2[index])

			table2.append(t)

	cleanTable2 = []
	for t2 in table2:
		if t2 not in cleanTable2:
			cleanTable2.append(t2)

	print(cleanTable2)
	return cleanTable2

if __name__ == "__main__":
	f = open(sys.argv[1], "r")
	lol = f.read()
	f.close()

	lol = lol.split("\n")
	while "" in lol:
		lol.remove("")

	for i in range(0, len(lol)):
		lol[i] = lol[i].split(",")

	print(lol)

	finalState = input("Enter a final state: ")

	allState = "".join(l[0] for l in lol)

	arr = []
	arr.append("".join(aS for aS in allState if aS not in finalState))
	arr.append("".join(aS for aS in allState if aS in finalState))


	arr2 = optimizationDFA(arr, lol)
	lol2 = reduceTable(arr2, lol)
