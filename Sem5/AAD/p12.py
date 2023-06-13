def max(a, b):
	if(a >= b):
		return a, "-"
	return b, "|"

def compute_lcs(p, q):
	m = len(q)
	n = len(p)

	arr = []
	d = []

	i = 0
	while(i <= n):
		j = 0

		t1 = []
		t2 = []

		while(j <= m):
			if(j == 0 or i == 0):
				t1.append(0)
			else:
				t1.append(None)

			t2.append(None)

			j += 1
		arr.append(t1)
		d.append(t2)

		i += 1

	i = 1
	while(i <= n):
		j = 1
		while(j <= m):
			if(p[i-1] == q[j-1]):
				arr[i][j] = arr[i-1][j-1] + 1
				d[i][j] = "\\"
			else:
				arr[i][j], d[i][j] = max(arr[i][j-1], arr[i-1][j])

			j += 1
		i += 1

	print(" + ======================= + ")

	for x in range(0, n+1):
		for y in range(0, m+1):
			print(arr[x][y], end=" ")
		print("")

	print(" + ======================= + ")

	for x in range(0, n+1):
		for y in range(0, m+1):
			print(d[x][y], end=" ")
		print("")

	return arr, d

a = []
def display_lcs(arr, d, i, j):
	global a

	if(i == 0 or j == 0):
		return

	if(d[i][j] == "\\"):
		a.append(j-1)
		display_lcs(arr, d, i-1, j-1)
	elif(d[i][j] == "|"):
		display_lcs(arr, d, i-1, j)
	elif(d[i][j] == "-"):
		display_lcs(arr, d, i, j-1)

if __name__ == "__main__":
	pc = input("Enter a character: ")
	qc = input("Enter another character: ")

	p = [c for c in pc]
	q = [c for c in qc]

	arr, d = compute_lcs(p, q)

	display_lcs(arr, d, len(arr)-1, len(arr[0])-1)

	print(" + ======================= + ")

	print(a)

	print(" + ======================= + ")

	x = len(a) - 1
	while(x >= 0):
		print(q[a[x]], end="")

		x -= 1
