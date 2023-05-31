def union(a, b):
	return (a.union(b))

def intersection(a, b):
	a = list(a)
	b = list(b)
	inter = []

	for i in range(0, len(a)):
		if(a[i] in b):
			inter.append(a[i])

	return set(inter)

def difference(a, b):
	return a - b

def symDiff(a, b):
	n1 = difference(a, b)
	n2 = difference(b, a)

	ans = union(n1, n2)
	return ans

def powerSet(a):
	return (2 ** len(a))

def complement(a, b):
	return difference(b, a)

def cartProd(a, b):
	a = list(a)
	b = list(b)
	ans = []

	for i in range(0, len(a)):
		for j in range(0, len(b)):
			ans.append((a[i],b[j]))

	return set(ans)

if __name__ == "__main__":
	a = {4, 5, 6, 8, 0, 3, 12}
	b = {4, 12, 0, 9, 38, 14, 1, 2}

	print("Union: ", union(a,b))
	print("Intersection: ", intersection(a,b))
	print("Difference: ", difference(a, b))
	print("Symmetric Difference: ", symDiff(a, b))
	print("Power set: ", powerSet(a))
	print("Complement: ", complement(a, b))
	print("Cartesian Product: ", cartProd(a, b))

	print('-----')
	print("A: ", a)
	print("B: ", b)
