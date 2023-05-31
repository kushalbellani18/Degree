import sys

def copyData(arr):
	arr2 = []

	for i in range(0, len(arr)):
		arr2.append(arr[i])

	return arr2

def copyDataVersion2(arr):
	arr2 = []

	for i in range(0, len(arr)):
		t = []
		for j in range(0, len(arr[i])):
			t.append(arr[i][j])

		arr2.append(t)

def update(l, ansIndex, lol):
	if(len(set(ansIndex)) == 1):
		return l, False
	else:
		hmmSet = list(set(ansIndex))
		updateData = []

		for hS in hmmSet:
			t = ""
			for iA in range(0, len(ansIndex)):
				if hS == ansIndex[iA]:
					t += l[iA]

			updateData.append(t)

		return updateData, True

def getIndex(s, lol):
	lolIndex = ""

	for si in s:
		for i in range(0, len(lol)):
			if si in lol[i]:
				lolIndex += str(i)

	return lolIndex

def transtition(l, table, symbol):
	s = ""

	for li in l:
		for ti in table:
			if li == ti[0]:
				s += ti[symbol+1]
				break

	return s

def optimizationDFA(lol, table):

	while(True):
		lol2 = []

		for l in lol:
			print(l)
			for i in range(0, 2):
				ans = transtition(l, table, i)
				ansIndex = getIndex(ans, lol)

				print(str(i) + ": ", end=" ")
				print(ans, end= " ")
				print(ansIndex)

				updateData, isUpdate = update(l, ansIndex, lol)

				if isUpdate == True:
					print(" => ", updateData)
					for uD in updateData:
						lol2.append(uD)

					if l in lol2:
						lol2.remove(l)
					break
				else:
					lol2.append(updateData)

			lol2 = list(set(lol2))
			print("")

		if(set(lol) == set(lol2)):
			break

		print(lol2)

		lol = copyData(lol2)

	print("Final ans: ", lol2)
	return lol2

def whereIndex(lol, t):
	for l in range(0, len(lol)):
		if t in lol[l]:
			return l

def reduceTable(lol, table):
	table2 = []
	lol2 = ["Q"+str(i) for i in range(0, len(lol))]

	for i in range(0, len(lol)):
		print(lol[i], " --> ", lol2[i])

	print("--------------------")

	for i in range(0, len(lol)):
		t = [lol2[i]]

		for ti in table:
			if ti[0] == lol[i][0]:
				index = whereIndex(lol, ti[1])
				t.append(lol2[index])

				index = whereIndex(lol, ti[2])
				t.append(lol2[index])

			table2.append(t)

	# Reduce Multiple rows (duplicate) into single row
	cleanTable2 = []
	for t2 in table2:
		if t2 not in cleanTable2:
			cleanTable2.append(t2)

	return cleanTable2

def disTable(table):
	print("state\t0\t1\n")
	for t in table:
		print(t[0], "\t", t[1], "\t", t[2])

if __name__ == "__main__":
#	print("Enter a state (LabelName, TransitionOf0, TransitionOf1; so on)")
#	arr = list(input().upper().split(';'))

	f = open(sys.argv[1])
	arr = f.read()
	f.close()

	arr = arr.split('\n')

	for i in range(0, len(arr)):
		arr[i] = arr[i].split(',')

	print(arr)

	startState = input("Enter an initial state: ").upper()
	finalState = input("Enter a final state: ").upper()

	allState = ""
	allState = "".join([ai[0] for ai in arr])

	print(allState)

	lol = []
	lol.append("".join(ai for ai in allState if ai not in finalState)) # For non-final state
	lol.append("".join(ai for ai in allState if ai  in finalState)) # For final state

	print(lol)

	lol2 = optimizationDFA(lol, arr)
	arr2 = reduceTable(lol2, arr)

	print(arr2)

	disTable(arr)
	disTable(arr2)
