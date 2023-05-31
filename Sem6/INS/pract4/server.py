import numpy as np
from socket import *

def strToList(str):
	arr = []

	for s in str:
		arr.append(s)

	return arr

def keyMatrix(arr):

	i = ord('A')
	while(i <= ord('Z')):
		if(chr(i) not in arr):
			if(chr(i) != 'J'):
				arr.append(chr(i))

		i += 1

	print(arr)
	return arr

def twoPair(arr):
	a = []

	v2 = 1
	while(v2 < len(arr)):
		v1 = v2 - 1
		a.append(arr[v1] + arr[v2])

		v2 += 2

	return a

def scanIndex(key, str):
	a = []

	for c in str:

		for i in range(0, len(key)):
			for j in range(0, len(key[i])):
				if(c == key[i][j]):
					a.append([i,j])

	return a

def dePlayFairCipher(key, arr):
	npKey = np.array(key).reshape(5,5)
	newArr = []

	for c in arr:
		a = scanIndex(npKey, c)

		# Same row
		if(a[0][0] == a[1][0]):
			c1 = (a[0][1] - 1) % 5
			c2 = (a[1][1] - 1) % 5

			newArr.append(
				npKey[a[0][0]][c1] + npKey[a[1][0]][c2]
			)
		# Same column
		elif(a[0][1] == a[1][1]):
			r1 = (a[0][0] - 1) % 5
			r2 = (a[1][0] - 1) % 5

			newArr.append(
				npKey[r1][a[0][1]] + npKey[r2][a[1][1]]
			)
		else:
			r1 = a[0][0]
			c1 = a[0][1]

			r2 = a[1][0]
			c2 = a[1][1]

			newArr.append(
				npKey[r1][c2] + npKey[r2][c1]
			)

	s = ""
	for lol in newArr:
		s += lol

	return s

if __name__ == "__main__":
	serverName = "127.0.0.1"
	serverPort = 12345

	serverSocket = socket(AF_INET, SOCK_DGRAM)
	serverSocket.bind(("", serverPort))

	key, serverAddress = serverSocket.recvfrom(2048)
	msg, serverAddress = serverSocket.recvfrom(2048)

	key = key.decode()
	msg = msg.decode()

	key = key.upper()

	arr = strToList(msg)
	str = twoPair(arr)

	k = []
	for lol in key:
		if(lol not in k):
			k.append(lol)

	k = keyMatrix(k)

	ans = dePlayFairCipher(k, str)

	if('X' in ans):
		s = ""
		for c in ans:
			if(c != 'X'):
				s += c

		ans = s

	print("Ans: ", ans)


	serverSocket.close()
