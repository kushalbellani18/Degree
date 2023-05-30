import math
import random

def isPrime(n):
	ch = [x for x in range(2, 10)]

	isPrime = True

	if(len(str(n)) == 1):
		if n not in [2, 3, 5, 7]:
			isPrime = False
	else:
		for c in ch:
			if n % c == 0:
				isPrime = False
				break

	return isPrime

def relativeFunction(eucler):
	e = []

	for i in range(2, eucler):
		if(math.gcd(i, eucler) == 1):
			e.append(i)

	print("e: ", e)
	return e

def getD(e, eTF):
	d = 1
	while(True):
		if( (d*e) % eTF == 1):
			break
		d += 1

	print("d: ", d)
	return d

def encrypt(m, e, n):
	return (m**e % n)

def decrypt(c, d, n):
	return (c**d % n)

if __name__ == "__main__":
	while(True):
		p = int(input("Enter a prime number of p: "))

		if(isPrime(p)):
			break

	print("")

	while(True):
		q = int(input("Enter a prime number of q: "))

		if(isPrime(q) and p != q):
			break

	n = p * q
	eucler = (p-1) * (q-1)

	e = relativeFunction(eucler)
	e1 = e[
		random.randint(0, len(e) - 1)
	]

	print("e1: ", e1)

	d = getD(e1, eucler)

	print("Public key: ", (e1, n))
	print("Private key: ", (d, n))

	m = random.randint(1, 100)
	print("Original Message: ", m)

	c = encrypt(m, e1, n)
	m1 = decrypt(c, d, n)

	print("Cipher message: ", c)
	print("Answer message: ", m1)
