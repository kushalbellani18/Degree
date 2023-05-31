import random

# Random key of length '8'
def getKey():
	str = ""

	for i in range(0, 8):
		str += chr(random.randint(
			ord('A'), ord('Z')
		))

#	print(str)
	return str

# Convert String to Bits
def strToBit(str):
	bits = ""

	for s in str:
		bits += format(ord(s), '08b')

#	print(bits)
#	print(len(bits))
#	print("")
	return bits

def bitToStr(bit):
	s = ""

	i = 0
	while(i < len(bit)):
		s += chr(int(bit[i:i+8], 2))

		i += 8

	return s

# Convert key of length 64 to key of length 56
# Compression P-Box
def reductionKeyBits(key64):
	key56 = ""

#	print("key: ", len(key64))

	i = 0
	while(i < len(key64)):
		key56 += key64[i:i+7]

		i += 8

#	print("key 2: ", len(key56))
#	print(key56)
	return key56

# Straight P-Box for Index
def pBoxPermutationForIndex(n):
	index = [x for x in range(0, n)]
	index2 = []

	for i in range(0, n):
		while(True):
			lol = random.randint(0, n)
			if(lol in index):
				index2.append(lol)
				index.remove(lol)

				break

#	print(index2)
	return index2

# Straight P-Box
def pBoxPermutation(str, index):
	str2 = ""

	for i in index:
		str2 += str[(i) % len(index)]

	#print(str2)
	return str2

# Expansion Permutation
def expansionPermutation(bit):
	bit2 = ""

	i = 0
	while(True):
		#print(">>>>>>>>>>>>>>>> " + str(i) + " -> " + str(i+4))
		l = bit[i-1]
		r = bit[((i+4)+1) % len(bit)]

		bit2 += l + bit[i:i+4] + r
		i += 4

		if(i >= 32):
			break

#	print(bit2)
	return bit2

def keyGeneration(key, shift):
	keyL = key[0:28]
	keyR = key[28:]

#	print("M: ", len(key))
#	print("L: ", len(keyL))
#	print("R: ", len(keyR))

#	print("Old Key", key)

	index = [x-shift for x in range(0, len(keyL))]
	extraStr = [None for x in range(0, len(keyL))]
	for i in range(0, len(index)):
		extraStr[index[i]] = keyL[i]

	keyL = "".join(extraStr)

	# ------------------------------------------------------

	extraStr = [None for x in range(0, len(keyR))]
	for i in range(0, len(index)):
		extraStr[index[i]] = keyR[i]

	keyR = "".join(extraStr)

#	print("New Key: ", (keyL + keyR))

	key = reductionKeyBits((keyL + keyR))
	key = key[1:] # Just remove first bit

#	print("")
	return key, keyL+keyR

# S-Boxes
def sBox(res):
	# Save data storage in S-BOX
	s = [
		[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
		[0, 15, 7, 4, 14, 2, 13, 10, 3, 6, 12, 11, 9, 5, 3, 8],
		[4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
		[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
	]

	arr = []
	i = 0
	while(i < len(res)):
		arr.append(res[i:i+6])

		i += 6

	res2 = ""

	for a in arr:
		x = int(str(a[0]) + str(a[-1]), 2)
		y = int(a[1:-1], 2)

		res2 += str(
				format(s[x][y], '04b')
			)

#	print(res2)
#	print("len: ", len(res2))
	return res2

def xor(a, b):
	c = ""

	for i in range(0, len(a)):
		if a[i] == b[i]:
			c += '0'
		else:
		 	c += '1'

	return c

def encryptionDES(key, pt):
	print("+--------------------------------------+")
	print("")
	index = pBoxPermutationForIndex(len(pt))

	# Just write to a file ('index.txt')
	f = open("file/index.txt", "w")

	for i in index:
		f.write(str(i))
		f.write("\n")

	f.close()

	# Initial Permutation
#	print("--------> Initial Permutation <---------")
	res = pBoxPermutation(pt, index)

	# ROUND FUNCTION (16 ROUND)
	for i in range(0, 16):
#		print(">>>>>>>>>> ", i, " <<<<<<<<<<<")
		resL = res[0:32]
		resR = res[32:]

		# Expansion Permutation
#		print("--------> Expansion Permutation <---------")
		resR = expansionPermutation(resR)

#		print("Expansion Permutation: ", resR)
#		print("len: ", len(resR))

		# Shift of Key
		if(i == 0 | i == 1 | i == 8 | i == 15):
			key2, key = keyGeneration(key, 1)
		else:
			key2, key = keyGeneration(key, 2)

#		print("lenK: ", len(key))
#		print("Old res: ", res)
#		print("Key: ", key)

		# XOR with resR and key, store in resR of size 48
		resR = xor(key2, resR)
#		print("XOR with resR and key : ", resR)
#		print("X-or: ", len(resR))

		# S-Box
		resR = sBox(resR)

#		print("S-BOX: ", resR)

		# Straight P-Box
#		print("Main: ", len(index))
#		print("resR: ", len(resR))
#		print("index: ", len(index[len(resR):]))
		resR = pBoxPermutation(resR, index[len(resR):])

#		print("Straight P-BOX: ", resR)

		# XOR with resR and resL, store in resL of size 32
		resL = xor(resL, resR)

		# Swapper resR and resL
		resL, resR = resR, resL


	# END ROUND FUNCTION

	# Final Permutation
#	print("--------> Final Permutation <---------")
	res = resL + resR
	res = pBoxPermutation(res, index)

#	print("RESULT: ", res)
#	print("LENGTH: ", len(res))
	lol = bitToStr(res)
	kLol = bitToStr(key)
	print("STRING: ", lol)
#	print("STRING LEN: ", len(lol))
#	print("")
	print("KEY: ", kLol)
#	print("KEY LEN: ", len(kLol))

#	for l in lol:
#		print(l, " --> ", ord(l))

	# ---------------- Just write to a file -------------------
	f = open("file/msg.txt", "w")

	f.write(lol)

	f.close()

	f = open("file/key.txt", "w")

	f.write(kLol)

	f.close()

	print("")
	print("+-----------------------------------------+")

if __name__ == "__main__":
	while(True):
		pt = input("Enter any 8 characters: ")
		if(len(pt) % 8 == 0):
			break

	pt = pt.upper()
	key = getKey()

	pt = strToBit(pt)
	key = strToBit(key)

#	print(">>>>> key: ", len(key))
	key = reductionKeyBits(key)
#	print(">>>>> Red key: ", len(key))

	res = encryptionDES(key, pt)
