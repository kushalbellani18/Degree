def bitToStr(bit):
	s = ""

	i = 0
	while(i < len(bit)):
		s += chr(int(bit[i:i+8], 2))

		i += 8

	return s

def strToBit(str):
	bits = ""

	for s in str:
		bits += format(ord(s), '08b')

	return bits

def pBoxPermutationForIndex():
	f = open("file/index.txt", "r")
	arr = []

	rl = f.readline()
	while(rl):
		arr.append(int(rl))
		rl = f.readline()

#	print("Index of P-BOX: ", arr)
	return arr

def pBoxPermutation(str, index):
	arr = []
	for i in range(0, len(str)):
		arr.append(None)

	for a in range(0, len(index)):
		arr[a] = str[index[a] % len(index)]

	return ''.join(arr)

def expansionPermutation(bit):
	bit2 = ""

	i = 0
	while(True):
		l = bit[i-1]
		r = bit[((i+4)+1) % len(bit)]

		bit2 += l + bit[i:i+4] + r
		i += 4

		if(i >= 32):
			break

	return bit2

def reductionKeyBits(key64):
	key56 = ""

	i = 0
	while(i < len(key64)):
		key56 += key64[i:i+7]

		i += 8

	return key56

def keyGeneration(key, shift):
	keyL = key[0:28]
	keyR = key[28:]

#	print("L: ", len(keyL))
#	print("R: ", len(keyR))
#	print("M: ", len(key))

	index = [(x+shift)%len(keyL) for x in range(0, len(keyL))]
	extraStr = [None for x in range(0, len(keyL))]

	for i in range(0, len(index)):
		extraStr[index[i]] = keyL[i]

	keyL = "".join(extraStr)

	# -------------------------------------------------------------
	extraStr = [None for x in range(0, len(keyR))]
	for i in range(0, len(index)):
		extraStr[index[i]] = keyR[i]

	keyR = "".join(extraStr)

	key = reductionKeyBits((keyL+keyR))
	key = key[1:] # Just remove first bit

#	print("")
	return key, keyL+keyR

def sBox(res):
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

	return res2

def xor(a, b):
	c = ""

	for i in range(0, len(a)):
		if a[i] == b[i]:
			c += '0'
		else:
			c += '1'

	return c

def decryptionDES(key, pt):
	print("+----------------------------------------------------------+")
	print("")
	index = pBoxPermutationForIndex()

	print(len(index))

	print(len(pt))

	# Initial Permutation
	res = pBoxPermutation(pt, index)
#	print(len(res))

	# ROUND FUNCTION (16 Round)
	for i in range(0, 16):
		resL = res[0:32]
		resR = res[32:]

		# Expansion Permutation
		resR = expansionPermutation(resR)

		# Shift of key
		if(i == 0 | i == 1 | i == 8 | i == 15):
			key2, key = keyGeneration(key, 1)
		else:
			key2, key = keyGeneration(key, 2)

		# XOR
		resR = xor(key2, resR)

		# S-Box
		resR = sBox(resR)

		# Straigh P-Box
#		print(len(resR))
#		print(len(index[len(resR):]))
		resR = pBoxPermutation(resR, index[len(resR):])

		# XOR
		resL = xor(resL, resR)

		# Swapper
		resL, resR = resR, resL

	# END ROUND

	# Final Permutation
	res = resL + resR
	res = pBoxPermutation(res, index)

	lol = bitToStr(res)
	print("RES: ", lol)

	return None

if __name__ == "__main__":
	f = open("file/msg.txt", 'r')

	txt = f.read()

	f.close()

	f = open("file/key.txt", 'r')

	key_txt = f.read()

	f.close()

	pt = strToBit(txt)
	key = strToBit(key_txt)

	print("LEN: ", len(key_txt))
	print("LEN: ", len(key))

	print(txt)
	print(key_txt)

#	print(" So sad: ", txt)
#	print(len(txt))
#	print(" >>>> ", len(pt))

#	print("Key: ", key)
#	print("PT: ", pt)

	res = decryptionDES(key, pt)
