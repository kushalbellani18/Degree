import math
import random

def isPrimeNumber(n):
	num = [x for x in range(2, 10)]

	isPrime = True

	if(len(str(n)) == 1):
		if(n not in [2, 3, 5, 7]):
			isPrime = False

	else:
		for ni in num:
			if(n % ni == 0):
				isPrime = False
				break

	return isPrime

def relativePrime(n):
	e = []
	for i in range(2, n):
		if(math.gcd(i, n) == 1):
			e.append(i)

#	print("e: ",e)
	return e

def getAnswer(e, eTF):
	d = 1
	while(True):
		if( (d*e) % eTF == 1):
			break

		d += 1

#	print("d: ", d)
	return d

def encryption(e, n, m):
	return (m ** e) % n

def decryption(d, n, c):
	return (c ** d) % n

if __name__ == "__main__":
	while(True):
		p = int(input("Enter a p: "))

		if(isPrimeNumber(p)):
			break

		print("Try Again!")

	while(True):
		q = int(input("Enter a q: "))

		if(isPrimeNumber(q) and p != q):
			break

		print("Try Again!")

	n = p * q
	eulerTotientFunction = (p-1) * (q-1)

	e = relativePrime(eulerTotientFunction)
	e1 = e[
		random.randint(0, len(e)-1)
	]
#	print(" >> e1: ", e1)
	d = getAnswer(e1, eulerTotientFunction)

	print("Public key: ", (e1, n))
	print("Private key: ", (d, n))

	print("+---------------------------------------+")
	print("")

	m = random.randint(1, n)

	print("Original Message: ", m)

	c = encryption(e1, n, m)
	print("Cipher Message: ", c)

	ans = decryption(d, n, c)
	print("Answer Message: ", ans)

	if(ans == m):
		print("Great one!")
	else:
		print("Oops!")

	print("")
	print("+---------------------------------------+")
