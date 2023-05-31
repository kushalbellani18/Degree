# [['E', ['TX']], ['X', ['+TX', 'epsilon']], ['T', ['FY']], ['Y', ['*FY', 'epsilon']], ['F', ['(E)', 'z']]]

top = -1
box = []

def E():
	global inputSymbol
	global box, top

	T()
	X()



	if inputSymbol == '$':
		print("Successfully!\n")
	else:
		print("Failed!\n")
	return

def X():
	global inputSymbol
	global box, top

	if inputSymbol == '+':
		advance()
		T()
		X()


	advance(1)

def T():
	global inputSymbol
	global box, top

	F()
	Y()


	return

def Y():
	global inputSymbol
	global box, top

	if inputSymbol == '*':
		advance()
		F()
		Y()


	advance(1)

def F():
	global inputSymbol
	global box, top

	if inputSymbol == '(':
		box.append('(')
		top += 1
		advance()
		E()
		if inputSymbol == ')':
				if top != -1:
					if box[top] == '(':
						box.pop()
						top -= 1
						advance()

	else:
		if inputSymbol == 'z':
			advance()


	return

def advance(isEpsilon=0):
	global index
	global st
	global inputSymbol

	global top, box

	if isEpsilon == 0:
		index += 1
	if index < len(st):
		inputSymbol = st[index]
	elif index > len(st) or len(box) != 0:
		inputSymbol = '!'
	else:
		inputSymbol = '$'
	return

st=input(">>> ")
index=0
inputSymbol=st[index]

E()