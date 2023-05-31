# [['E', ['TX']], ['T', ['+TX', 'epsilon']], ['X', ['(E)', 'z']]]

top = -1
box = []

def E():
	global inputSymbol
	global top, box

	T()
	X()


	if inputSymbol == '$':
		print("Successfully!")
	else:
		print("Failed")
	return

def T():
	global inputSymbol
	global top, box

	if inputSymbol == '+':
		advance()
		T()
		X()


	advance(1)

def X():
	global inputSymbol
	global top, box

	if inputSymbol == '(':
		top += 1
		box.append(()
		E()
		if inputSymbol == ')':
				if top != -1:
					if box[top] == '(':
						box.pop()
						top -= 1

	else:
		if inputSymbol == 'z':
			advance()


	return

