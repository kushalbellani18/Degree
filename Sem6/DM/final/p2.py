import random

def dataGroup():
	return [
		(1+0j),
		(-1+0j),
		(1j),
		(-1j)
	]

def isMonoid(dataSet):
	a = dataSet[random.randint(0, len(dataSet) - 1)]

	while(True):
		b = dataSet[random.randint(0, len(dataSet) - 1)]
		if (a != b):
			break

	if a in dataSet and b in dataSet and (a*b) in dataSet:
		print(">> Successfully Monoid!")
		return True

	print(">> Failed, Monoid!")
	return False

def isSemiGroup(dataSet):
	a = dataSet[random.randint(0, len(dataSet) - 1)]

	while(True):
		b = dataSet[random.randint(0, len(dataSet) - 1)]
		print("a : ", a)
		print("b : ", b)
		if (a != b):
			break

	while(True):
		c = dataSet[random.randint(0, len(dataSet) - 1)]
		if (a != c and b != c):
			break

	if a * (b * c) == (a * b) * c:
		print(">> Successfully Semi-group!")
		return True

	print(">> Failed, Semi-group!")
	return False

def isIdentity(dataSet):
	a = dataSet[random.randint(0, len(dataSet) - 1)]

	e = a / a

	if e in dataSet:
		print(">> Successfully Identity!")
		return True, e

	print(">> Failed, Identity!")
	return False, None

def isGroup(dataSet, e):
	a = dataSet[random.randint(0, len(dataSet) - 1)]
	a_inv = e / a

	if a_inv in dataSet:
		print(">> Successfully Group!")
		return True

	print(">> Failed, Group!")
	return False

def isAbelian(dataSet):
	a = dataSet[random.randint(0, len(dataSet) - 1)]

	while(True):
		b = dataSet[random.randint(0, len(dataSet) - 1)]
		if (a != b):
			break

	if a * b == b * a:
		print(">> Successfully Abelian!")
		return True

	print(">> Failed, Abelian!")
	return False

def isSubGroup(h, g):
	for hi in h:
		if hi not in g:
			return False

	return True

if __name__ == "__main__":
	g = dataGroup()
#	print("Group: ", g)

	c1 = isMonoid(g)
	c2 = isSemiGroup(g)
	c3, e = isIdentity(g)
	c4 = isGroup(g, e)
	c5 = isAbelian(g)

	if c1 and c2 and c3 and c4 and c5:
		print("Yes, it is Abelian group.")
	else:
		print("No, it isn't Abelian group.")

	print("+--------------------------------------------------------------+")
	print(" >>>>>>>>>>>> Sub group <<<<<<<<<<<<<<")
	h = [1, -1]

	c1 = isMonoid(h)
	c3, e = isIdentity(h)
	c4 = isGroup(h, e)
	c5 = isAbelian(h)

	if c1 and c3 and c4 and c5:
		print("Yes, it is Sub-Group of G") if isSubGroup(h, g) else print("No, it isn't sub-group.")
	else:
		print("No, it isn't Sub-group.")
