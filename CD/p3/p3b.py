import re

def comeOn(sC):
	keywords = [
		"auto", "break", "case", "char",
		"const", "continue", "default", "do",
		"double", "else", "enum", "extern",
		"float", "for", "goto", "if",
		"int", "long", "register", "return",
		"short", "signed", "sizeof", "static",
		"struct", "switch", "typedef", "union",
		"unsigned", "void", "volatile", "while"
	]

	op = ['+', '-', '=', '/', '*']

	for s in sC:
		if(re.match(r'#.*(<.h>)*', s)):
			print(s, " -->  PREPROCESSOR DIRECTIVE!")

		elif(s in keywords):
			print(s, " --> KEYWORD!")

		elif(re.match(r'^[a-zA-Z][a-zA-Z0-9]*\(', s)):
			print(s, " --> FUNCTION!")

		elif(re.match(r'^[a-zA-Z][a-zA-Z0-9]*', s)):
			print(s, " --> IDENTIFIER!")
		elif(s in op):
			print(s, " --> OPERATOR!")

if __name__ == "__main__":
	file = open("file/blah.c", "r")
	contents = file.read()

	splitCode = contents.split()

	print(splitCode)

	print("------------------------------------------")

	comeOn(splitCode)
