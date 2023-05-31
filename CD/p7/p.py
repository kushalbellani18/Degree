import os

def addTokenToFile(t, index):
	f = open("blah2.py", "a")

	f.write("def " + t[0] + "():\n")
	f.write("\tglobal inputSymbol\n")
	f.write("\tglobal box, top\n\n")
	blah = 0
	s = 0

	isEpsilon = 0
	print(t[1])
	if "epsilon" in t[1]:
		isEpsilon = 1
		t[1].remove("epsilon")

	for ti in t[1]:
		space = 1 + s
		for tii in ti:

			if blah == 1:
				f.write("\t" * (space - 1))
				f.write("else:\n")
				blah = 0

			f.write("\t" * space)

			if tii.isupper():
				f.write(tii + "()\n")
			else:
				f.write("if inputSymbol == \'" + tii + "\':\n")
				space += 1

				if tii in "({[":
					f.write("\t" * space)
					f.write("box.append(\'" + tii + "\')\n")
					f.write("\t" * space)
					f.write("top += 1\n")

					f.write("\t" * space)
					f.write("advance()\n")

				elif tii in ")}]":
					f.write("\t" * space)
					f.write("\tif top != -1:\n")
					f.write("\t" * space)

					if tii == ")":
						f.write("\t\tif box[top] == \'(\':\n")
					elif tii == "}":
						f.write("\t\tif box[top] == \'{\':\n")
					elif tii == "]":
						f.write("\t\tif box[top] == \'[\':\n")

					f.write("\t" * space)
					f.write("\t\t\tbox.pop()\n")
					f.write("\t" * space)
					f.write("\t\t\ttop -= 1\n")

					f.write("\t" * space)
					f.write("\t\t\tadvance()\n")
				else:
					f.write("\t" * space)
					f.write("advance()\n")

		f.write("\n")
		blah = 1
		s = 1

	f.write("\n")

	if index == 0:
		f.write("\n")
		f.write("\tif inputSymbol == \'$\':\n")
		f.write("\t\tprint(\"Successfully!\\n\")\n")

		f.write("\telse:\n")
		f.write("\t\tprint(\"Failed!\\n\")\n")

	if isEpsilon == 0:
		f.write("\treturn")
	else:
		f.write("\tadvance(1)")

	f.write("\n\n")

	f.close()

if __name__ == "__main__":
	txt = []

	while True:
		lol = input("> ")

		if lol.lower() == "end":
			break

		lol = lol.split("->")
		if len(lol) == 1:
			lol[1] = [lol[1]]
		else:
			lol[1] = lol[1].split("|")

		txt.append(lol)

	print(txt)

	if os.path.exists("blah2.py"):
		os.remove("blah2.py")

	f = open("blah2.py", "x")
	f.write("# " + str(txt) + "\n\n")
	f.write("top = -1\nbox = []\n\n")
	f.close()

	# Append each token to a file
	for t in range(0, len(txt)):
		addTokenToFile(txt[t], t)

	f = open("blah2.py", "a")
	f.write("def advance(isEpsilon=0):\n")
	f.write("\tglobal index\n")
	f.write("\tglobal st\n")
	f.write("\tglobal inputSymbol\n\n")
	f.write("\tglobal top, box\n\n")

	f.write("\tif isEpsilon == 0:\n")
	f.write("\t\tindex += 1\n")

	f.write("\tif index < len(st):\n")
	f.write("\t\tinputSymbol = st[index]\n")
	f.write("\telif index > len(st) or len(box) != 0:\n")
	f.write("\t\tinputSymbol = \'!\'\n")
	f.write("\telse:\n")
	f.write("\t\tinputSymbol = \'$\'\n")

	f.write("\treturn\n\n")

	f.write("st=input(\">>> \")\n")
	f.write("index=0\n")
	f.write("inputSymbol=st[index]\n\n")

	f.write(str(txt[0][0]) + "()")

	f.close()
