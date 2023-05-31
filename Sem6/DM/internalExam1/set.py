def fact(a):
	ans = 1

	for i in range(0, a):
		ans *= (i+1)

	print(ans)
	return ans

def permutation(n, k):
	return fact(n-k) / fact(k)

if __name__ == "__main__":
	n = 1000

	buy_a = (40/100) * 1000
	buy_b = (20/100) * 1000
	buy_c = (10/100) * 1000

	buy_ab = (5/100) * 1000
	buy_bc = (3/100) * 1000
	buy_ac = (2/100) * 1000

	buy_abc = (2/100) * 1000

	totalNewspaper = (buy_a + buy_b + buy_c) - (buy_ab + buy_bc + buy_ac) + buy_abc
	print("Total: ", totalNewspaper)

	print("1) Number of families which buy all three newspapers: ", buy_abc)
	print("2) Number of families which buy newspaper B and C only: ", buy_bc)
	print("3) Number of families which buy at least 2 newspaper: ", (buy_ab + buy_bc + buy_ac + buy_abc))
	print("4) Number of families which buy exactly only one newspaper: ", (buy_a + buy_b + buy_c))
