import sys

def findOperator(s, op):
	for i in range(0, len(s)):
		if s[i] == op:
			return i

	return None

def dead_code(txt):
	new_txt = []

	for t in txt:
		sign_index = findOperator(t, '=')

		temp = t[sign_index+1:]
		len_temp = 0
		for te in temp:
			if te in [chr(x) for x in range(ord('a'), ord('z')+1)] or te in [chr(x) for x in range(ord('A'), ord('Z')+1)] or te in ['+', '*', '/', '-']:
				len_temp += 1

		if len_temp == len(temp):
			new_txt.append(t)

#	print(new_txt)
	return new_txt

def copy_propagation(txt):
	for i in range(0, len(txt)):
		sign_index_i = findOperator(txt[i], "=")
		temp_i = txt[i][sign_index_i+1:]
		front_temp_i = txt[i][:sign_index_i]

		for j in range(i+1, len(txt)):
			sign_index_j = findOperator(txt[j], "=")
			temp_j = txt[j][sign_index_j+1:]
			front_temp_j = txt[j][:sign_index_j]

			if temp_i == temp_j:
				for ij in range(0, len(txt)):
					txt[ij] = txt[ij].replace(front_temp_j, front_temp_i)

#	print(txt)
	return txt

def common_subexpression_elimination(txt):
	return list(set(txt))

def display(txt):
	for t in txt:
		print(t)

	print("")

if __name__ == "__main__":
	file = open(sys.argv[1], "r")
	txt = file.read()

	file.close()

	txt = txt.split('\n')

	while '' in txt:
		txt.remove('')

	print("Intermediate code")
	display(txt)

	txt = dead_code(txt)
	print("Dead Code")
	display(txt)

	txt = copy_propagation(txt)
	print("Copy Propagation")
	display(txt)

	txt = common_subexpression_elimination(txt)
	print("Common Subexpression Elimination")
	display(txt)
