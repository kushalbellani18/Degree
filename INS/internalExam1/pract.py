import random

def matrix(arr):
	a = []

	for ai in arr:
		a.append(
			ord(ai) - ord('A')
		)

	print(a)
	return a

def partition(arr):
	a = []

	i = 0
	while(i < len(arr)):
		#if(i+1 < len(arr)):
		a.append(
			[arr[i], arr[i+1]]
		)

		i += 2

	print(a)
	return a

def encryptHillCipher(pt, key):
	arr = []

	for p in pt:
		str = ""
		for i in range(0, len(key)):
			ans = key[i][0] * p[0] + key[i][1] * p[1]
			ans = ans % 26

			str += chr(ans + ord('A'))

		arr.append(str)

	#print(arr)
	return ''.join(arr)

if __name__ == "__main__":
	while(True):
		plaintext = input(">> ").upper()
		if(len(plaintext) % 2 == 0):
			break

	key = "".join([
		chr(random.randint(ord('A'), ord('Z'))) for x in range(0, 4)
	])

	#print(plaintext)
	print(key)

	plaintextMatrix = matrix(plaintext)
	keyMatrix = matrix(key)

	ptMatrix = partition(plaintextMatrix)
	keyMatrix = partition(keyMatrix)

	res = encryptHillCipher(ptMatrix, keyMatrix)
	print(res)
