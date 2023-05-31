import sys

def getIndex(txt, match):
	for i in range(0, len(txt)):
		if txt[i] == match:
			return i

	return None

def deadcode(txt):
	new_txt = []

	for i in range(0, len(txt)):
		sign_index = getIndex(txt[i], "=")

		temp = txt[i][sign_index+1:]
		temp_len = 0

		for ii in range(0, len(temp)):
			if( (ord(temp[ii]) >= ord('a') and ord(temp[ii]) <= ord('z')) or (ord(temp[ii]) >= ord('A') and ord(temp[ii]) <= ord('Z')) or (temp[ii] in ['+', '-', '/', '*']) ):
				temp_len += 1

		if temp_len == len(temp):
			new_txt.append(txt[i])

	return new_txt

def copy_propagation(txt):
	for i in range(0, len(txt)):
		sign_index_i = getIndex(txt[i], "=")
		temp_i = txt[i][sign_index_i+1:]

		for j in range(i+1, len(txt)):
			sign_index_j = getIndex(txt[j], "=")
			temp_j = txt[j][sign_index_j+1:]

			if temp_i == temp_j:
				for ij in range(0, len(txt)):
					txt[ij] = txt[ij].replace(txt[j], txt[i])

	return txt

def common_subexpression_elimination(txt):
	return list(set(txt))

def display(txt):
	for t in txt:
		print(t)
	print("")

if __name__ == "__main__":
	f = open(sys.argv[1], "r")
	txt = f.read()
	f.close()

	txt = txt.split('\n')
	while '' in txt:
		txt.remove('')

	print("Intermediate code")
	display(txt)

	txt = deadcode(txt)
	print("Dead Code")
	display(txt)

	txt = copy_propagation(txt)
	print("Copy Propagation")
	display(txt)

	txt = common_subexpression_elimination(txt)
	print("Common Subexpression Elimination")
	display(txt)
