import random
import hashlib

def invMultiplication(k, q):
	x = 1
	while(True):
		ans = k * x % q

#		print(x, " -> ", ans)

		if(ans == 1):
			break

		x += 1

	return x

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

#	print("+-----------------------------------------+")
#	print("qSet: ", qSet)
#	print("l: ", l)
#	print("alpha: ", alpha)
#	print("+-----------------------------------------+")

	return alpha

if __name__ == "__main__":
	# >>>>>>>>> Global Public-Key Components <<<<<<<<<<<
	print("")

	while(True):
		p = int(input("Enter a prime number: "))
		if(isPrimeNumber(p)):
			break

	q = primitiveRoot(p)

	for i in range(1, p):
		if( ((i ** (p-1)/q) % p) > 1):
			h = i
			break

	g = (h * (p-1)/q) % p

	p = 283
	q = 47
	g = 60

	print("p: ", p)
	print("q: ", q)
	print("g: ", g)
	print("")

	# >>>>>>>>>> User's private key, User's public key, and User's per-message secret number
	print("")
	x = random.randint(1, q-1)
	y = (g ** x) % p

	print("x: ", x)
	print("y: ", y)

	k = random.randint(1, q-1)

	print("k: ", k)
	print("")

	# >>>>>>>>> Signing <<<<<<<<<
	print("")
	r = ( (g**k) % p) % q
	lol = invMultiplication(k, q)

	msg = input("Enter a msg: ")
	h = hashlib.sha1()
	h.update(msg.encode())

	mi = int(h.hexdigest(), 16)
	print(" >>>>>>>>>> mi: ", mi)

	s = ( lol * (mi + (x*r)) ) % q

	print("r: ", r)
	print("s: ", s)
	print("")

	print("|--------------------------------------------------------------|")

	# >>>>>>>> verifying <<<<<<<<
	w = invMultiplication(s, q) % q

	h = hashlib.sha1()
	h.update(msg.encode())

	mi = int(h.hexdigest(), 16)

	u1 = (mi*w) % q
	u2 = (r*w) % q

	v = ( ( (g**u1) * (y**u2) ) % p ) % q

	print("")
	print("w: ", w)
	print("u1: ", u1)
	print("u2: ", u2)
	print("v: ", v)
	print("")

	if(v == r):
		print("Successfully!")
	else:
		print("Failed!")
