import random

def invG(g, op):
	if op == "+":
		return (1-g)
	elif op == "-":
		return (1 + g)
	elif op == "*":
		return (1/g)
	elif op == "/":
		return (1*g)

def isNormalSubgroup(n, g, op):
	selected_n = n[random.randint(0, len(n)-1)]
	selected_g = g[random.randint(0, len(g)-1)]
	inv_g = invG(selected_g, op)

	print("n: ", selected_n)
	print("g: ", selected_g)
	print("inv_g: ", inv_g)
	print("op: ", op)

	if op == '+':
		res = selected_g + selected_n + inv_g
	elif op == '-':
		res = selected_g - selected_n - inv_g
	elif op == '*':
		res = selected_g * selected_n * inv_g
	elif op == '/':
		res = selected_g / selected_n / inv_g

	print("")
	print(">>> ", res)

	return (res in n)

if __name__ == "__main__":
	n = ([1, -1], '*')
	g = ([1, -1, 1j, -1j], '*')

	print(isNormalSubgroup(n[0], g[0], n[-1]))

	print("")
	print("-----------------------------------------------------------------------")
	print("")

	n = ([1], '*')
	g = ([1, -1], '*')

	print(isNormalSubgroup(n[0], g[0], n[-1]))
