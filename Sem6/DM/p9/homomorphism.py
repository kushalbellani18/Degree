import random

def function(x):
	return (
		2 ** x
	)

def calculate(op, x1, x2, ch='LHS'):
	if(ch == 'LHS'):
		if(op == '+'):
			ans = function(x1+x2)
		elif(op == '-'):
			ans = function(x1-x2)
		elif(op == '*'):
			ans = function(x1*x2)
		elif(op == '/'):
			ans = function(x1/x2)

	elif(ch == 'RHS'):
		if(op == '+'):
			ans = function(x1) + function(x2)
		elif(op == '-'):
			ans = function(x1) - function(x2)
		elif(op == '*'):
			ans = function(x1) * function(x2)
		elif(op == '/'):
			ans = function(x1) / function(x2)

	else:
		print("Error: invalid ", ch, " in ch variable.")
		return 'error'

	return ans

if __name__ == "__main__":
	op1 = input("Enter operator 1 for G: ")
	op2 = input("Enter operator 2 for G': ")

	x1 = random.randint(1, 100)
	x2 = random.randint(1, 100)

	print("x1: ", x1)
	print("x2: ", x2)

	res1 = calculate(op1, x1, x2)
	res2 = calculate(op2, x1, x2, 'RHS')

	if(res1 != 'error' or res2 != 'error'):
		print(res1 == res2)
