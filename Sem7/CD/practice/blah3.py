import sys

def getIndex(txt, match):
	for i in range(0, len(txt)):
		if match == txt[i][0]:
			return i

	return -1

def firstSet(txt):
	txt2 = []

	for t in txt:
		list_txt = []
		for i in range(0, len(t[1])):
			list_txt.append(t[1][i][0])

		txt2.append([t[0], list_txt])

	print(txt2)

	for i in range(0, len(txt2)):
		mainIndex = txt2[i][0]
		mainList = txt2[i][1].copy()

		j = 0
		while(j < len(mainList)):
			gi = getIndex(txt2, mainList[j])

			if gi != -1:
				for fj in txt2[gi][1]:
					mainList.append(fj)
			j += 1

		txt2[i][1] = mainList

	print(txt2)


if __name__ == "__main__":
	f = open(sys.argv[1], "r")
	txt = f.read()
	f.close()

	txt = txt.split("\n")

	while '' in txt:
		txt.remove('')

	for i in range(0, len(txt)):
		txt[i] = txt[i].split('->')

	for i in range(0, len(txt)):
		txt[i][1] = txt[i][1].split('|')

	firstSet(txt)
