import random

def isClosure(z, op):
	lol = [i for i in range(-10000, 10001)]

	a = z[random.randint(0, len(z)-1)]
	while(True):
		b = z[random.randint(0, len(z)-1)]
		if (b != a):
			break

#	print("a: ", a)
#	print("b: ", b)

	if op == '-':
		if( (a-b) in lol):
			return True
	elif op == '+':
		if( (a+b) in lol):
			return True
	elif op == '*':
		if( (a*b) in lol):
			return True
	elif op == '/':
		if( (a/b) in lol):
			return True

	return False

def isAssociative(z, op):
	#lol = [i for i in range(-10000, 10001)]

	a = z[random.randint(0, len(z)-1)]
	while(True):
		b = z[random.randint(0, len(z)-1)]
		if (b != a):
			break

	while(True):
		c = z[random.randint(0, len(z)-1)]
		if (c != a & c != b):
			break

#	print("a: ", a)
#	print("b: ", b)
#	print("c: ", c)

	if op == '-':
		if( (a - b) - c == a - (b - c) ):
			return True
	elif op == '+':
		if( (a + b) + c == a + (b + c) ):
			return True
	elif op == '*':
		if( (a * b) * c == a * (b * c) ):
			return True
	elif op == '/':
		if( (a / b) / c == a / (b / c) ):
			return True

	return False

def isIdentity(z, op):
	a = z[random.randint(0, len(z)-1)]

#	print("a: ", a)

	if op == '-':
		e = a - a
	elif op == '+':
		e = a - a
	elif op == '/':
		e = a * a
	elif op == '*':
		e = a / a

	return e

def isInverse(z, op, e):
	a = z[random.randint(0, len(z)-1)]
	print("a: ", a)

	if op == '-':
		aInv = a - e
	elif op == '+':
		aInv = e - a
	elif op == '/':
		aInv = a / e
	elif op == '*':
		aInv = e / a

	return aInv

def subGroup(sg, g):
	lol = [i for i in range(-10000, 10001)]

#	print("g: ", g)
#	print("sg: ", sg)

	for i in range(0, len(sg)):
		if sg[i] not in g:
			return False

	return True


if __name__ == "__main__":
	lowerLimit = int(input("Enter a lower limit of first Integer: "))
	upperLimit = int(input("Enter a upper limit of first Integer: "))

	z1 = [i for i in range(lowerLimit, upperLimit + 1)]

	print("")
	print("G: ", z1)

	op = input("Enter a opertor: ")

	c1 = isClosure(z1, op)
	c2 = isAssociative(z1, op)

	if(c1 == True and c2 == True):
		e = isIdentity(z1, op)
		print("e(Identity): ",e)

		print("")
		print("a^-1: ", isInverse(z1, op, e))

		z2 = [z for z in z1 if z % 2 == 0]

		isGroup = subGroup(z2, z1)
		s = "" if isGroup else "not"

		print("")
		print("-> ", z2, " is " + s + " sub-group of ", z1)

	else:
		print("Sorry due to either of Closure or Asssociative is false")

	# Z Cross is coming soon!
