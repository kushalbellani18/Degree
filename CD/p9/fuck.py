import sys

def firstSet(txt):
	txt2 = []

	for t in txt:
		txt_list = []

		for tii in t[1]:
			txt_list.append(tii[0])

		i = 0
		while(i < len(txt_list)):
			for ti in range(0, len(txt)):
				if txt_list[i] == txt[ti][0]:
					for tii in txt[ti][1]:
						txt_list.append(tii[0])

			i += 1

		txt2.append([t[0], [ml for ml in txt_list if not ml.isupper()]])

	return txt2

def firstSet_index(fs_r, match):
	for fsr in fs_r:
		if fsr[0] == match:
			return fsr[1]

def followSet(txt):
	txt2 = []

	for t in txt:
		txt_list = []

		for tt in txt:
			if t[0] != tt[0]:
				for i in range(0, len(tt[1])):
					if t[0] in tt[1][i]:
						txt_list.append(tt[1][i])

		txt2.append([t[0], txt_list])

	#print(txt2)

	firstSet_result = firstSet(txt)

	txt3 = []
	for i in range(0, len(txt2)):
		txt3.append([txt2[i][0], []])

		if i == 0:
			txt3[-1][1].append("$")

		for t2 in txt2[i][1]:
			for t2_index in range(0, len(t2)):
				if txt3[-1][0] == t2[t2_index]:
					t2_index += 1

					if t2_index < len(t2):
						if t2[t2_index].isalnum() == False or t2[t2_index].islower == True or t2[t2_index].isdigit() == True:
							txt3[-1][1].append(t2[t2_index])
						else:
							res = firstSet_index(firstSet_result, t2[t2_index])

							for r in res:
								txt3[-1][1].append(r)
					else:
						pass

	print(txt3)

if __name__ == "__main__":
	f = open(sys.argv[1], "r")
	txt = f.read()
	f.close()

	print("+----------------------+")
	print(txt)
	print("+----------------------+")

	txt = txt.split()

	while '' in txt:
		txt.remove('')

	for i in range(0, len(txt)):
		txt[i] = txt[i].split("->")
		txt[i][1] = txt[i][1].split("|")

	followSet(txt)
