import numpy as np

def strToList(str):
	arr = []
	for s in str:
		arr.append(s)

	return arr

def keyMatrix(key):
	key = key.upper()
	arr = []

	for k in key:
		if k not in arr:
			arr.append(k)

	i = ord('A')
	while(i <= ord('Z')):
		if chr(i) not in arr and chr(i) != 'J':
			arr.append(chr(i))

		i += 1

	return arr

def twoPair(plainText):
	plainText = plainText.upper()
	arr = []
	pt = strToList(plainText)

	i = 0
	while(i < len(pt)):
		v1 = pt[i]

		if((i+1) == len(pt)):
			v2 = "X"
		else:
			v2 = pt[i+1]

		if(v1 == v2):
			v2 = "X"
			i -= 1

		arr.append(v1 + v2)
		i += 2

	return arr

def scanIndex(arr, c):
	a = []
	jj = 0

	for lol in range(0, len(c)):
		if(c[lol] == 'J' or c[lol] == 'j'):
			for i in range(0, len(arr)):
				for j in range(0, len(arr[i])):
					if(arr[i][j] == 'i' or arr[i][j] == 'I'):
						a.append([i,j])

		else:
			for i in range(0, len(arr)):
				for j in range(0, len(arr[i])):
					if(arr[i][j] == c[lol]):
						a.append([i,j])

	return a

def encrypt(key, plainText):
	key = keyMatrix(key)
	plainText = twoPair(plainText)

#	print(key)
#	print(len(key))

	npKey = np.array(key).reshape(5, 5)
	newArr = []

#	print("------------------------------------------------------")
#	print("PlainText: ", plainText)
#	print("Key: ", npKey)
#	print("------------------------------------------------------")

	for c in plainText:
		a = scanIndex(npKey, c)
#		print(">> a: " ,a)

		# Same row
		if(a[0][0] == a[1][0]):
			r1 = a[0][0]
			r2 = a[1][0]

			c1 = (a[0][1] + 1) % 5
			c2 = (a[1][1] + 1) % 5

			newArr.append(npKey[r1][c1] + npKey[r2][c2])

		# Same column
		elif(a[0][1] == a[1][1]):
			c1 = a[0][1]
			c2 = a[1][1]

			r1 = (a[0][0] + 1) % 5
			r2 = (a[1][0] + 1) % 5

			newArr.append(npKey[r1][c1] + npKey[r2][c2])

		else:
			newArr.append(npKey[a[0][0]][a[1][1]] + npKey[a[1][0]][a[0][1]])

	str = ""
	for s in newArr:
		str += s

	return str

def decrypt(key, plainText):
	key = keyMatrix(key)
	plainText = twoPair(plainText)

#	print(key)
#	print(len(key))

	npKey = np.array(key).reshape(5, 5)
	newArr = []

	for c in plainText:
		a = scanIndex(npKey, c)

		# Same row
		if(a[0][0] == a[1][0]):
			r1 = a[0][0]
			r2 = a[1][0]

			c1 = (a[0][1] - 1) % 5
			c2 = (a[1][1] - 1) % 5

			newArr.append(npKey[r1][c1] + npKey[r2][c2])

		# Same column
		elif(a[0][1] == a[1][1]):
			c1 = a[0][1]
			c2 = a[1][1]

			r1 = (a[0][0] - 1) % 5
			r2 = (a[1][0] - 1) % 5

			newArr.append(npKey[r1][c1] + npKey[r2][c2])

		else:
			newArr.append(npKey[a[0][0]][a[1][1]] + npKey[a[1][0]][a[0][1]])

	str = ""
	for s in newArr:
		str += s

	str = removeX(str)

	return str

def removeX(txt):
	txt2 = ""

	for t in txt:
		if t != 'X':
			txt2 += t

	return txt2

'''
if __name__ == "__main__":
	str = "HELLOZZDHDDCDIHHFFIEBBIBJIHDFHECCCEDJJFEGAJHFDBECBCDJEIHIAEGDHGAEIDEEDF"
	key = 'kushal'

	print("Str: ", str)

	res = encrypt(key, str)
	print("Encrypt: ", res)

	res = decrypt(key, res)
	res = removeX(res)
	print("Decrypt: ", res)
'''
