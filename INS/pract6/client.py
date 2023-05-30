import random
from socket import *

def getKey():
	n = 4
	arr = []
	str = ""

	for i in range(0, int(n/2)):
		t = []
		for j in range(0, int(n/2)):
			c = random.randint(ord('A'), ord('Z'))
			str += chr(c)
			t.append(c - 65)

		arr.append(t)

	return str, arr

def partition(pt, n):
	arr = []

	i = 0
	while(i < len(pt)):
		arr.append(pt[i:i+2])

		i += 2

	return arr

def getMatrix(pt, n):
	arr = []

	for s in pt:
		a = []

		for i in range(0, int(n/2)):
			a.append(
				ord(s[i]) - 65
			)

		arr.append(a)

	return arr

def encryptHillCipher(k, p):
	ans = []
	str = ""

	for s in p:
		a = []

		for i in range(0, len(k)):
			res = (k[i][0] * s[0]) + (k[i][1] * s[1])
			res %= 26

			a.append(res)
			str += chr(res+65)

		ans.append(a)

	return str, ans

if __name__ == "__main__":

	while(True):
		pt = input(">> ").upper()
		if(len(pt) % 4 == 0):
			break

	key, keyArr = getKey()

	ptStr = partition(pt, len(key))
	ptArr = getMatrix(ptStr, len(key))

	#print(ptArr)
	#print(keyArr)

	res, resArr = encryptHillCipher(keyArr, ptArr)
	print("---------------------------------------------")
	print(res)
	#print(resArr)

	# <<<<--- Socket --->>>>
	serverName = "127.0.0.1"
	serverPort = 12345

	clientSocket = socket(AF_INET, SOCK_DGRAM)
	clientSocket.sendto(key.encode(), (serverName, serverPort))
	clientSocket.sendto(res.encode(), (serverName, serverPort))

	clientSocket.close()
