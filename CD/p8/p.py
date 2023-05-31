import sys

def getIndex(lol, lol_match):
	for i in range(0, len(lol)):
		if lol[i][0] == lol_match:
			return i

	return -1

def firstSet(txt):
	txt2 = []

	# Get First Character...
	for t in txt:
		list_txt = []
		for i in range(0, len(t[1])):
			list_txt.append(t[1][i][0])

		txt2.append([t[0], list_txt])

	print(">>>>>>>>> first character <<<<<<<<<<<<")
	print(txt2)
	print("~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("")

	# Update...

	for i in range(0, len(txt2)):
		mainIndex = txt2[i][0]
		mainList = [t for t in txt2[i][1]]
		print(mainIndex)
		print(mainList)

		print("-----------------------------------------")

		j = 0
		while j < len(mainList):
			get_index = getIndex(txt2, mainList[j])

			if get_index != -1:
				for fj in txt2[get_index][1]:
					mainList.append(fj)

			j += 1

		# Clean...

		mainList = [mL for mL in mainList if not mL.isupper()]
		txt2[i][1] = mainList

		print(mainIndex)
		print(mainList)
		print("\n\n")

#	print(txt2)

	return txt2

if __name__ == "__main__":
#	print(sys.argv)
#	print(sys.argv[1])

	f = open(sys.argv[1], "r")
	txt = f.read()
	f.close()

	print(txt)

	txt = txt.split('\n')

	while '' in txt:
		txt.remove('')

	for i in range(0, len(txt)):
		txt[i] = txt[i].split('->')

	for i in range(0, len(txt)):

		txt[i][1] = txt[i][1].split('|')

#	print(">> ", txt[1][1].split('|'))

#	print(txt)
	print("---------------")

	res = firstSet(txt)

	for ri in res:
		print("First(", ri[0], "): ", set(ri[1]))
