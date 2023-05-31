def stringToList(s):
	a = []

	for si in s:
		a.append(si)

	return a

def scanB(s):
	for i in range(0, len(s)):
		if(s[i] == 'b'):
			return i

	return -1

def check(s):
	sList = stringToList(s)
	sSetLen = len(set(sList))

	if sSetLen > 2:
		return False

	# First find 'b' in given string
	# if 'a' is found after 'b', it must be return 'False'

	bIndex = scanB(s)
	if bIndex != -1:
		for i in range(bIndex + 1, len(s)):
			if s[i] == 'a':
				return False

	if bIndex == -1 and len(s) != 1:
		return False

def whichRE(s):
	if len(s) == 1:
		if s[0] == 'b':
			return "b*, a*b+"
		else:
			return "a"

	if s == "abb":
		return "a*b+, abb"

	if s[0] == 'b':
		return "b*"

	return "a*b+"

if __name__ == "__main__":
	s = input("Enter a string: ")

	if(check(s) == False):
		print("Sorry! your string is not allowing under my expression... \n")

		exit(0)

	print("Perfect!")

	print("Welcome your string! Under the condition \'", whichRE(s), "\'")
