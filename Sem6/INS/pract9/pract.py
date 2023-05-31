import random

def isPrimeNumber(n):
	num = [x for x in range(2, n)]

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

def primitiveRoot(q):
	qSet = set(
		[i for i in range(1, q)]
	)

	alpha = 1
	while(True):
		l = []

		for i in range(1, q):
			l.append(
				(alpha ** i) % q
			)

		if(qSet == set(l)):
			break

		alpha += 1

#	print("l: ", l)
#	print("Alpha: ", alpha)
	return alpha

def privateKeyGeneration(q):
	return random.randint(1, (q-1))

def publicKeyGeneration(alpha, x, q):
	return (
		(alpha ** x) % q
	)

def secretKey(x, y, q):
	return (
		(y ** x) % q
	)

if __name__ == "__main__":
	while(True):
		q = int(input("Enter a prime number: "))
		if(isPrimeNumber(q)):
			break

	alpha = primitiveRoot(q)

	xa = privateKeyGeneration(q)
	xb = privateKeyGeneration(q)

	ya = publicKeyGeneration(alpha, xa, q)
	yb = publicKeyGeneration(alpha, xb, q)

	ka = secretKey(xa, yb, q)
	kb = secretKey(xb, ya, q)

	print("xa: ", xa)
	print("ya: ", ya)
	print("")

	print("xb: ", xb)
	print("yb: ", yb)
	print("")

	print("ka: ", ka)
	print("kb: ", kb)
	print("")

	if(ka == kb):
		print("Perfect!")
	else:
		print("Oops! error")
