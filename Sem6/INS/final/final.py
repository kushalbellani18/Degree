def display(arr):
	for i in range(0, len(arr)):
		for j in range(0, len(arr[i])):
			print(arr[i][j], end=",")
		print("")

def getPolyAlphabetic():
	arr = []
	for i in range(0, 26):
		t = []
		for j in range(i, i+26):
			t.append(
				chr((j%26) + ord('A'))
			)

		arr.append(t)

#	display(arr)
	return arr

def encrypt(msg, key):
	matrix = getPolyAlphabetic()
	cipher = ""

	for i in range(0, len(msg)):
		r = ord(msg[i]) - ord('A')
		c = ord(key[i]) - ord('A')

		cipher += matrix[r][c]

	print("Cipher: ", cipher)
	return cipher

def decrypt(cip, key):
	matrix = getPolyAlphabetic()
	msg = ""

	i = 0
	for k in key:
		r = ord(k) - ord('A')

		for j in range(0, len(matrix[r])):
			if matrix[r][j] == cip[i]:
				msg += chr(j+ord('A'))
				break
		i += 1

	print("Message: ", msg)
	return msg

if __name__ == "__main__":
	msg = input("Enter a message: ").upper()
	key = input("Enter a key: ").upper()

	key2 = ""
	for i in range(0, len(msg)):
		key2 += key[i%len(key)]

	print("key2: ", key2)

	print("+---------------------------------------------+")
	cipher = encrypt(msg, key2)
	message = decrypt(cipher, key2)

	if(msg == message):
		print("Successfully!")
	else:
		print("Failed!")
