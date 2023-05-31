import sys

def copyData(arr):
	a = []
	for ai in arr:
		a.append(ai)

	return a

def prefix(arr):
	matchList = []

	for i in range(1, len(arr)):
		matchStr = ""
		for j in range(0, min(len(arr[i-1]), len(arr[i]))):
			if arr[i-1][j] == arr[i][j]:
				matchStr += arr[i][j]

		if matchStr != '':
			matchList.append(matchStr)

	return matchList

def getHighestPoint(arr):
	arrUnique = list(set(arr))
	arrUnique_count = []

	for aui in arrUnique:
		t = 0
		for ai in arr:
			if aui == ai:
				t += 1

		arrUnique_count.append(t)

	# Find highest point
	maxCountIndex = 0
	for i in range(1, len(arrUnique)):
		if arrUnique_count[maxCountIndex] < arrUnique_count[i]:
			maxCountIndex = i

	return arrUnique[maxCountIndex]

def leftFactoringElimination(txt):
	print(txt)
	matchList = []
	backupList = []

	matchList = prefix(txt[1])
	backupList = copyData(matchList)

	while(True):
		matchList += prefix(matchList)
		print("matChLiSt>> ", matchList)
		print("baCkUpliST>> ", backupList)
		print("")

		if(set(matchList) == set(backupList)):
			break

		backupList = copyData(matchList)

#	print("MatChLiSt>> ", set(matchList))

	# -----------------------------------------------------------------
	alpha = getHighestPoint(matchList)
	print("Alpha: ", alpha)
	beta = []

	# >>>>>>>>>>. Add to Beta .<<<<<<<<<<<<
	for t in txt[1]:
		if alpha in t:
			beta.append(t[len(alpha):])

	# >>>>>>>>>. Remove .<<<<<<<<<<<
	for b in beta:
		if((alpha + b) in txt[1]):
			txt[1].remove(alpha + b)

	# >>>>>>>>>. Replace '' with NULL .<<<<<<<<<<<
	if '' in beta:
		for i in range(0, len(beta)):
			if beta[i] == '':
				beta[i] = "NULL"

	txt[1].append(alpha + txt[0] + "\'")

	txt2 = [txt[0] + "\'"]
	txt2.append(beta)

	return [txt, txt2]

def display(lol):
	print("+----------------------------------------------+")
	for i in range(0, len(lol)):
		for li in lol[i]:
			print(li, end=" ")
		print("")

	print("+----------------------------------------------+")
	print("\n\n")

if __name__ == "__main__":
	txt = sys.argv[1]

	print(txt)

	txt = txt.split("->")
	txt[1] = txt[1].split("|")
	txt[1].sort()

#	print(txt)
	print("")

	res = leftFactoringElimination(txt)
	display(res)
#	res1 = leftFactoringElimination(res[-1])
#	display(res1)
#	res2 = leftFactoringElimination(res1[0])
#	display(res2)

#	print("+--------------------------------------------------+")
	for ri in range(0, len(res)):
#		print(">> ", ri)
		res[ri][1] = "|".join(res[ri][1])
		res[ri] = "->".join(res[ri])

		print(res[ri])
#	print("+--------------------------------------------------+")
