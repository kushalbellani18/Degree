import numpy as np
from socket import *

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
		if(c[lol] == 'J'):
			for i in range(0, len(arr)):
				for j in range(0, len(arr[i])):
					if(arr[i][j] == "I"):
						a.append([i, j])
		else:
			for i in range(0, len(arr)):
				for j in range(0, len(arr[i])):
					if(arr[i][j] == c[lol]):
						a.append([i, j])

	return a

def playFairCipher(key, plainText):
	npKey = np.array(key).reshape(5, 5)
	newArr = []

	for c in plainText:
		# Remember, a get value [ [r1, c1], [r2, c2] ],
		# Where, [r1, c1] is first character of string variable 'c',
		# and also [r2, c2] is second one.
		a = scanIndex(npKey, c)

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

		# Different in row and column. So, just swap column's index of string in key matrix
		else:
			newArr.append(npKey[a[0][0]][a[1][1]] + npKey[a[1][0]][a[0][1]])

	str = ""
	for s in newArr:
		str += s

	return str

if __name__ == "__main__":
	key = input("Enter Key: ")
	plainText = input("Enter Plain Text: ")

	k = keyMatrix(key)
	pt = twoPair(plainText)

	res = playFairCipher(k, pt)
	print(res)

	# <<<<------ Socket --------->>>>
	serverName = "127.0.0.1"
	serverPort = 12345

	clientSocket = socket(AF_INET, SOCK_DGRAM)
	clientSocket.sendto(key.encode(), (serverName, serverPort))
	clientSocket.sendto(res.encode(), (serverName, serverPort))

	clientSocket.close()
