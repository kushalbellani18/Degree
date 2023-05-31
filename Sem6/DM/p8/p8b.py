import random

def crossData(a, b):
	arr = []

	for ai in a:
		for bi in b:
			arr.append([ai, bi])

	return arr

def isClosure(z, op):
	lol = [i for i in range(-10000, 10001)]

	index = random.randint(0, len(z)-1)
	za0 = z[index][0]
	za1 = z[index][1]

	while(True):
		index2 = random.randint(0, len(z)-1)
		if(index != index2):
			zb0 = z[index2][0]
			zb1 = z[index2][1]
			break

	if op == '-':
		if( (za0 - zb0) in lol and (za1 - zb1) in lol ):
			return True
	elif op == '+':
		if( (za0 + zb0) in lol and (za1 + zb1) in lol ):
			return True
	elif op == '/':
		if( (za0 / zb0) in lol and (za1 / zb1) in lol ):
			return True
	elif op == '*':
		if( (za0 * zb0) in lol and (za1 * zb1) in lol ):
			return True

	return False

def isAssociative(z, op):
	index = random.randint(0, len(z)-1)
	za0 = z[index][0]
	za1 = z[index][1]

	while(True):
		index2 = random.randint(0, len(z)-1)
		if(index != index2):
			zb0 = z[index2][0]
			zb1 = z[index2][1]
			break

	while(True):
		index3 = random.randint(0, len(z)-1)
		if(index != index2 & index != index3):
			zc0 = z[index3][0]
			zc1 = z[index3][1]
			break

	if op == '-':
		if( (za0-zb0)-zc0 == za0-(zb0-zc0) and (za1-zb1)-zc1 == za1-(zb1-zc1) ):
			return True
	elif op == '+':
		if( (za0+zb0)+zc0 == za0+(zb0+zc0) and (za1+zb1)+zc1 == za1+(zb1+zc1) ):
			return True
	elif op == '/':
		if( (za0/zb0)/zc0 == za0/(zb0/zc0) and (za1/zb1)/zc1 == za1/(zb1/zc1) ):
			return True
	elif op == '*':
		if( (za0*zb0)*zc0 == za0*(zb0*zc0) and (za1*zb1)*zc1 == za1*(zb1*zc1) ):
			return True

	return False

def subGroup(sg, g):
	for i in range(0, len(sg)):
		if sg[i] not in g:
			return False
	return True

if __name__ == "__main__":
	z3 = [x for x in range(0, 3)]
	z4 = [x for x in range(0, 4)]

	z = crossData(z3, z4)
	print(z)

	op = input("Enter an opertor: ")

	c1 = isClosure(z, op)
	c2 = isAssociative(z, op)

	if(c1 == True and c2 == True):
		z2 = [[0,0], [0,1], [0,2], [0,3]]

		isGroup = subGroup(z2, z)
		s = "" if isGroup else "not"

		print("")
		print("--> ", z2, " is ", s, " sub-group of ", z)
	else:
		print("Sorry due to either of closure or associative is false")
