def sortData(p, w, index):
	if index == 0:
		for x in range(0, len(p)):
			t = -1
			sm = p[x]

			for y in range(x+1, len(p)):
				if(sm < p[y]):
					sm = p[y]
					t = y

			if(t != -1):
				p[t], p[x] = p[x], p[t]
				w[t], w[x] = w[x], w[t]

			t = -1
	elif index == 1:
		for x in range(0, len(w)):
			t = -1
			sm = w[x]

			for y in range(x+1, len(w)):
				if(sm < w[y]):
					sm = w[y]
					t = y

			if(t != -1):
				p[t], p[x] = p[x], p[t]
				w[t], w[x] = w[x], w[t]

			t = -1

	else:
		div = [p[i]/w[i] for i in range(0, len(p))]

		for x in range(0, len(div)):
			t = -1
			sm = div[x]

			for y in range(x+1, len(div)):
				if(sm < div[y]):
					sm = div[y]
					t = y

			if(t != -1):
				div[t], div[x] = div[x], div[t]
				p[t], p[x] = p[x], p[t]
				w[t], w[x] = w[x], w[t]
			t -= 1

	return p, w

def getValue(p, w, m):
	totalProfile = 0
	totalWeight = 0

	for i in range(0, len(p)):
		if(m < w[i]):
			break

		totalWeight += w[i]
		totalProfile += p[i]

		m -= w[i]

	if(m != 0):
		totalProfile += (p[i] * m/w[i])
		totalWeight += (w[i] * m/w[i])

		m -= w[i]

	print(totalProfile)
	print(totalWeight)

	return totalProfile

def greedyByProfile(p, w, m):
	print(" =========| Profile |=========")

	p, w = sortData(p, w, 0)
	print(p)
	print(w)

	print("\t |----------| ")

	return getValue(p, w, m)

def greedyByWeight(p, w, m):
	print(" =========| Weight |=========")

	p, w = sortData(p, w, 1)
	print(p)
	print(w)

	print("\t |----------| ")

	return getValue(p, w, m)

def greedyByProWei(p, w, m):
	print(" =========| Profile / Weight |=========")

	p, w = sortData(p, w, -1)
	print(p)
	print(w)
	print([p[x]/w[x] for x in range(0, len(p))])

	print("\t |----------| ")

	return getValue(p, w, m)

if __name__ == "__main__":
	n = int(input("Enter a number of items: "))

	p = []
	w = []

	for i in range(0, n):
		e = int(input("Enter P" + str(i+1) + ": "))
		p.append(e)
		e = int(input("Enter W" + str(i+1) + ": "))
		w.append(e)
		print(" \t -------- ")

	print("")

	maxW = int(input("Enter a maximum of weight: "))

	arr = []

	arr.append(greedyByProfile(p, w, maxW))
	print("")
	arr.append(greedyByWeight(p, w, maxW))
	print("")
	arr.append(greedyByProWei(p, w, maxW))
	print("")

	print("\t\t+------------Result------------+")
	print("\t\t [Sort Profile, Sort Weight, Sort Profile/Weight]")
	print("\t\t", arr)
	print("\t\t+------------------------------+")

	print("Maximum Profile: ", max(arr))
