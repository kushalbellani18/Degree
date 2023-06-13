def findIndex(min, list):
	i = 0
	while(i < len(list)):
		if(min == list[i]):
			return i

		i += 1

def matrixChainMultiplication(p, n):
	m = []
	s = []

	i = n - 1
	while(i >= 0):
		j = n - 1
		t = []
		t1 = []
		while(j >= i):
			t.append(None)
			t1.append(None)
			j -= 1

		s.append(t1)
		m.append(t)
		i -= 1

	l = n - 1
	x = 0
	while(x < n):
		i = 0
		j = i + x

		while(j < n):
			if(i == j):
				m[i][j] = 0
			else:
				t = []
				tk = []
				k = i

				while(k < j):
					t.append( m[l-i][l-k] + m[l-(k+1)][l-j] + (p[i] * p[k+1] * p[j+1]) )
					tk.append(k+1)
					k += 1

				m[l-i][l-j] = min(t)
				s[l-i][l-j] = tk[findIndex(min(t), t)]

			i += 1
			j += 1
		x += 1

	print("========|> Display <|========")
	print("")
	for r in range(0, n):
		for c in range(0, r+1):
			print("  ",m[r][c], end= " ")
		print("")
	print("")

	print("---")

	for r in range(1, n):
		for c in range(0, r):
			print("  ", s[r][c], end=" ")
		print("")

	print("")
	print("----------------------------")

	print("Answer: ", m[n-1][0])

	optimalParens(s, 3, 0, n)

def optimalParens(s, i, j, n):
	if (i==j):
		print("A"+str(n-i), end=" ")
	else:
		print("(", end="")
		optimalParens(s, i, n - (s[i][j]), n)
		optimalParens(s, n - (s[i][j] + 1), j, n)

		print(")", end="")

if __name__ == "__main__":
	n = int(input("Enter a number of items: "))
	p = []

	for i in range(0, n):
		print("---> Matrix " + str(i+1) + " <---")
		if(i == 0):
			r = int(input("Enter row: "))
			p.append(r)
		else:
			print("Enter row: " + str(p[i]))

		r = int(input("Enter columns: "))
		p.append(r)

	print(p)

	matrixChainMultiplication(p, n)
