if __name__ == "__main__":
	a = input("Enter elements for set A: ")
	A = set(a.split(' '))
	print("")

	b = input("Enter elements for set B: ")
	B = set(b.split(' '))
	print("")

	c = input("Enter elements for set C: ")
	C = set(c.split(' '))
	print("")

	print("--------- OUTPUT ---------")
	print("Original set elements:")
	print("A: ", A)
	print("B: ", B)
	print("C: ", C)
	print("")

	print("The intersection of two sets A & B: ", A.intersection(B))
	print("")

	print("The union of two sets A & B: ", B.union(A))
	print("")

	print("The difference of A & B: ", A.difference(B))
	print("The difference of B & A: ", B.difference(A))
	print("")

	print("The symmetric difference of A & B: ", (A.difference(B)).union(B.difference(A)) )
	print("")

	print("Is set A a subset of set B? ", A.issubset(B))
	print("Is set C a subset of set B? ", C.issubset(B))
