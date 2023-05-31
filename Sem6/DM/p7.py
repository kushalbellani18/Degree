import math
import random

def calculateFormula(p, rate, t):
	print(p * (1 + (rate/100))**t)

	return (
		p * (1 + (rate/100))**t
	)

def functA(r):
	if(r >= 3):
		return (2 ** (-r)) + 5

	return 0

def functB(r):
	if(r >= 2):
		return (r+2)

	return (3 - (2**r))

def functC(r):
	if(r >= 0 and r <=1):
		return (3 - (2**r))
	elif(r == 2):
		return 4
	else:
		return ((2**-r) + r + 7)

def functD(r):
	if(r >= 3):
		return (
			(r * (2 ** -r)) + (2 ** (-r+1)) + (5*r) + 10
		)

	return 0

if __name__ == "__main__":
	# Solution-1
	print("For person A: \n")

	personAAmount = float(input("Enter Amount: "))
	personAInterestRate = float(input("Enter rate per year: "))
	personATotalYear = float(input("Enter a total year: "))
	print("")

	print("For person B: \n")

	personBAmount = float(input("Enter Amount: "))
	personBInterestRate = float(input("Enter rate per year: "))
	personBTotalYear = float(input("Enter a total year: "))
	print("")

	d = calculateFormula(personAAmount, personAInterestRate, personATotalYear) + calculateFormula(personBAmount, personBInterestRate, personBTotalYear)

	print("Result: " + str(d))

	print("\n-----------------------------------------------------------\n")
	# Solution-2
	print("Person A's interest earned: ", personAAmount * (personAInterestRate*personATotalYear/100))
	print("Person B's interest earned: ", personBAmount * (personBInterestRate*personBTotalYear/100))


	print("\n-----------------------------------------------------------\n")
	# Solution-3
	r = int(input("Enter r: "))
	a = functA(r)
	b = functB(r)

	c = functC(r)
	d = functD(r)

	print("a: ", a)
	print("b: ", b)
	print("c: ", c)
	print("d: ", d)


	print("\n-----------------------------------------------------------\n")
	# Solution-4
	n = int(input("Enter N: "))

	for i1 in range(0, 3):
		for i2 in range(0, 3):
			for i3 in range(0, 3):
				print(i3, i2 , i1)


	print("\n-----------------------------------------------------------\n")
	# Solution-5
	n = int(input("Enter n: "))
	r = int(input("Enter r: "))

	# n! = 1 * 2 * 3 * ... * n
	print("Combinatorial Selection: " + str(
		math.comb(n-1, r) + math.comb(n-1, r-1)
	))
