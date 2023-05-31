import sys

def whereIndex(indexValue, txt):
	li = []

	for i in range(0, len(txt)):
		if indexValue in txt[i] and indexValue == txt[i][0]:
			li.append(i)

	return li

def leftRecursionElimination(txt):
	li = whereIndex(txt[0][0], txt[1])

	if(len(li) == 0):
		return txt, 0

	root = [[txt[0][0] + "\'"], ["NULL"]]
	t = 0
	for index in li:
		index -= t

		txtPop = txt[1].pop(index)
		txtPop = txtPop[1:]
		txtPop = txtPop + txt[0][0] + "\'"

		root[1].append(txtPop)

		t += 1


	for i in range(0, len(txt[1])):
		txt[1][i] = txt[1][i] + txt[0][0] + "\'"

#	print("+-------------------------------+")
#	print(root)
#	print(txt)
#	print("+-------------------------------+")

	return [txt, root], 1

if __name__ == "__main__":
#	print(sys.argv)
	print(sys.argv[1])

	txt = sys.argv[1].split("->")

	for i in range(0, len(txt)):
		txt[i] = txt[i].split("|")

	print(txt)

	txt, isChange = leftRecursionElimination(txt)
	for t in txt:
		print(">> ", t)

	print("")

	if isChange == 0:
		print("No change!!!")
		exit(0)

	res = []
	for ti in txt:
		ti[0] = "".join(ti[0])
		ti[1] = "|".join(ti[1])

		ti = "->".join(ti)

		res.append(ti)

	print("")
	for ri in res:
		print(ri)
