import sys

def getIndex(lol, lol_match):
	for i in range(0, len(lol)):
		if lol[i][0] == lol_match:
			return i

	return None

def firstSet(txt):
	txt2 = []

	# Get First Character...
	for t in txt:
		list_txt = []
		for i in range(0, len(t[1])):
			list_txt.append(t[1][i][0])

		txt2.append([t[0], list_txt])

#	print(txt2)

	# Update...

	for i in range(0, len(txt2)):
		mainIndex = txt2[i][0]
		mainList = [t for t in txt2[i][1]]
#		print(mainIndex)
#		print(mainList)

#		print("-----------------------------------------")

		j = 0
		while j < len(mainList):
			get_index = getIndex(txt2, mainList[j])

			if get_index != None:
				for fj in txt2[get_index][1]:
					mainList.append(fj)

			j += 1

		# Clean...

		mainList = [mL for mL in mainList if not mL.isupper()]
		txt2[i][1] = mainList

#		print(mainIndex)
#		print(mainList)
#		print("\n\n")

#	print(txt2)

	return txt2

def firstSet_by_followSet(txt):
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
			get_index = getIndex(txt2, mainList[j])

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
							index = getIndex(txt, txt2[i][1][j][si])
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
										firstSet_by_followSet(txt2[i][1][j][si])

									txt3[-1][1].remove("epsilon")
								else:
									t = []
									for ti in txt:
										if txt2[i][1][j] in ti[1]:
											t.append(ti[0])

#									print(txt3[-1][0], ": ", t)
									for ti in t:
										index = getIndex(txt3, ti)

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
							index = getIndex(txt3, ti)

							for f in txt3[index][1]:
								txt3[-1][1].append(f)

#		print("")
#	print(txt3)
	return txt3

def ll_1_table(txt, first, follow):
	small_letter = set()
	for f in first:
		small_letter = small_letter.union(set(f[1]))

	for f in follow:
		small_letter = small_letter.union(set(f[1]))

	if 'e' in small_letter:
		small_letter.remove('e')

	small_letter = list(small_letter)

	# To find a first set
	ll = []
	ll_follow = [] # For saved follow
	for sl in small_letter:
		t = []

		for f in first:
			if sl in f[1]:
				index = getIndex(txt, f[0])

				if index != None:
					tt = []

					for ti in txt[index]:
						tt.append(ti)

					t.append(tt)

					if "epsilon" in t[-1][-1]:
						t[-1][-1].remove("epsilon")

						# Let's add to follow list
						ll_follow.append(t[-1][0])

					if len(t[-1][-1]) != 1:
						for i in range(0, len(t[-1][-1])):
							if t[-1][-1][i][0] == sl:
								t[-1][-1] = [t[-1][-1][i]]
								break


		ll.append([sl, t])


	for lf in ll_follow:
		for f in follow:
			if lf == f[0]:
				for lf_follow in f[1]:
					index = getIndex(ll, lf_follow)

					if index != None and [lf, ["epsilon"]] not in ll[index][-1]:
						ll[index][-1].append([lf, ["epsilon"]])

	for l in ll:
		print(l)

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

	first = firstSet(txt)
	follow = followSet(txt)

	for i in range(0, len(first)):
		print("First (" + first[i][0] + "): ", set(first[i][1]))

	print("")

	for i in range(0, len(follow)):
		print("Follow (" + follow[i][0] + "): ", set(follow[i][1]))


	print("\n\n")
	ll_1_table(txt, first, follow)
