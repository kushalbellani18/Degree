import sys

def getIndexList(txt, match_char):
	for i in range(0, len(txt)):
		if txt[i][0] == match_char:
			return i

	return None

def firstSet(txt):
	txt2 = []

	for t in txt:
		list_txt = []
		for i in range(0, len(t[1])):
			list_txt.append(t[1][i][0])

		txt2.append([t[0], list_txt])

	for i in range(0, len(txt2)):
		mainIndex = txt2[i][0]
		mainList = [t for t in txt2[i][1]]

		j = 0
		while j < len(mainList):
			get_index = getIndexList(txt2, mainList[j])

			if get_index != -1:
				for fj in txt2[get_index][1]:
					mainList.append(fj)

			j += 1

		mainList = [mL for mL in mainList if not mL.isupper()]
		txt2[i][1] = mainList

#	print(txt2)

def followSet(txt):
	txt2 = []

	for t in txt:
		txt_list = []

		for i in range(0, len(txt)):
			if t[0] != txt[i][0]:
				for j in range(0, len(txt[i][1])):
					if t[0] in txt[i][1][j]:
						txt_list.append(txt[i][1][j])

		txt2.append([t[0], txt_list])

#	print(txt2)

	txt3 = []
	for i in range(0, len(txt)):
		txt3.append([txt[i][0], []])

		if i == 0:
			txt3[i][1].append("$")

#		print(txt[i][0])
		for j in range(0, len(txt2[i][1])):
			for si in range(0, len(txt2[i][1][j])):
				if txt2[i][1][j][si] == txt2[i][0]:
					si += 1

					if si < len(txt2[i][1][j]):

						if txt2[i][1][j][si].islower() or txt2[i][1][j][si] in ")(}{][":
							txt3[-1][1].append(txt2[i][1][j][si])
						else:
							index = getIndexList(txt, txt2[i][1][j][si])
							if index != None:
								for ti in txt[index][1]:
									if "epsilon" != ti:
										txt3[-1][1].append(ti[0])
									else:
										txt3[-1][1].append("epsilon")

							# Check Epsilon
							if "epsilon" in txt3[-1][1]:
								si += 1

								if si < len(txt2[i][1][j]):
#									print("~~> ", txt2[i][1][j][si])
									if txt2[i][1][j][si].islower():
										txt3[-1][1].append(txt2[i][1][j][si])
									else:
#										print("---> ", txt2[i][1][j][si])
										firstSet(txt2[i][1][j][si])

									txt3[-1][1].remove("epsilon")
								else:
									t = []
									for ti in txt:
										if txt2[i][1][j] in ti[1]:
											t.append(ti[0])

#									print(txt3[-1][0], ": ", t)
									for ti in t:
										index = getIndexList(txt3, ti)

										for f in txt3[index][1]:
											txt3[-1][1].append(f)

									txt3[-1][1].remove("epsilon")

					else:
						t = []
						for ti in txt:
							if txt2[i][1][j] in ti[1]:
								t.append(ti[0])

#						print(txt3[-1][0], ": ", t)
						for ti in t:
							index = getIndexList(txt3, ti)

							for f in txt3[index][1]:
								txt3[-1][1].append(f)

#		print("")
#	print(txt3)
	return txt3


if __name__ == "__main__":
	f = open(sys.argv[1], "r")
	txt = f.read()
	f.close()

	print(txt)

	txt = txt.split('\n')

	while True:
		if '' in txt:
			txt.remove('')

		if '' not in txt:
			break

	for i in range(0, len(txt)):
		txt[i] = txt[i].split('->')

	for i in range(0, len(txt)):
		txt[i][1] = txt[i][1].split('|')

#	print(txt)

	txt = followSet(txt)

	for i in range(0, len(txt)):
		print("Follow ( " + txt[i][0] + " ): ", set(txt[i][1]))
