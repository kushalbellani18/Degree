import os

def addTokenToFile(txt, index):
	f = open("blah2.py", "a")

	f.write("def " + txt[0] + "():\n")
	f.write("\tglobal inputSymbol\n")
	f.write("\tglobal top, box\n\n")

	isE = 0
	if "epsilon" in txt[1]:
		txt[1].remove("epsilon")

		isE = 1

	blah = 0
	s = 0

	for ti in txt[1]:
		space = s + 1

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

				if tii in "{[(":
					f.write("\t" * space)
					f.write("top += 1\n")
					f.write("\t" * space)
					f.write("box.append(" + tii + ")\n")
				elif tii in "}])":
					f.write("\t" * space)
					f.write("\tif top != -1:\n")

					if tii == "]":
						f.write("\t" * space)
						f.write("\t\tif box[top] == \'[\':\n")
						f.write("\t" * space)
						f.write("\t\t\tbox.pop()\n")
						f.write("\t" * space)
						f.write("\t\t\ttop -= 1\n")
					elif tii == "}":
						f.write("\t" * space)
						f.write("\t\tif box[top] == \'{\':\n")
						f.write("\t" * space)
						f.write("\t\t\tbox.pop()\n")
						f.write("\t" * space)
						f.write("\t\t\ttop -= 1\n")
					elif tii == ")":
						f.write("\t" * space)
						f.write("\t\tif box[top] == \'(\':\n")
						f.write("\t" * space)
						f.write("\t\t\tbox.pop()\n")
						f.write("\t" * space)
						f.write("\t\t\ttop -= 1\n")
				else:
					f.write("\t" * space)
					f.write("advance()\n")

		blah = 1
		s = 1
		f.write("\n")

	f.write("\n")

	if index == 0:
		f.write("\tif inputSymbol == \'$\':\n")
		f.write("\t\tprint(\"Successfully!\")\n")

		f.write("\telse:\n")
		f.write("\t\tprint(\"Failed\")\n")

	if isE == 0:
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
		lol[1] = lol[1].split("|")

		txt.append(lol)

#	print(txt)

	if os.path.exists("blah2.py"):
		os.remove("blah2.py")

	f = open("blah2.py", "x")
	f.write("# " + str(txt) + "\n\n")
	f.write("top = -1\nbox = []\n\n")
	f.close()

	for i in range(0, len(txt)):
		addTokenToFile(txt[i], i)
