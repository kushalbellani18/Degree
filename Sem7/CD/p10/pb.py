import sys

def getIndex(lol, lol_match):
	for i in range(0, len(lol)):
		if lol[i][0] == lol_match:
			return i

	return None

if __name__ == "__main__":
	f = open(sys.argv[1], "r")
	txt = f.read()
	f.close()

	print(txt)

	txt = txt.split("\n")

	while '' in txt:
		txt.remove('')

	for i in range(0, len(txt)):
		txt[i] = txt[i].split('->')

		txt[i][-1] = txt[i][-1].split('|')

#	print(txt)

	stack = ["$"]

	stack.insert(0, txt[0][0])
	#print(stack)

	string = input("Enter a string: ")
	string += '$'
#	print(string)

	V = [chr(i) for i in range(ord('A'), ord('Z') + 1)] # For variable symbol

	while len(stack) != 0 and stack[0] != '$':
		top = stack[0]
		r = string[0]

		print(stack)

		print(top)
		print(r)

		print("")

		if r == '$':
			index = getIndex(txt, top)

			if index == None:
				print("Error")
				exit(0)

			if 'epsilon' in txt[index][-1]:
				stack.pop(0)
				continue
			else:
				print("Error")
				exit(0)

		# Check terminal or '$'
		if(top not in V or top == "$"):
			if(top == r):
				stack.pop(0)
				string = string[1:]
			else:
				print("Error")
				exit(0)

		# Check Terminal and add to stack before pop it.
		elif(top in V):
			index = getIndex(txt, top)

			if index == None:
				print("Error")
				exit(0)

			stack.pop(0)

			index_list = txt[index][-1] # Get list of index, means A->B1B2...Bk

			lol = []

			if 'epsilon' in index_list:
				for iL in index_list:
					if iL != 'epsilon':
						for ll in iL:
							lol.append(ll)

			else:
				for ll in index_list[0]:
					lol.append(ll)

			lol.reverse()
			print("LOL: ", lol)

			for l in lol:
				stack.insert(0, l)

	print("Boom! Successfully...")
