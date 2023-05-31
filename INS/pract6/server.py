from socket import *

def getKeyMatrix(key):
	arr = []

	x = 0
	for i in range(0,int(len(key)/2)):
		t = []
		for j in range(0, int(len(key)/2)):
			t.append(
				ord(key[x]) - 65
			)

			x += 1
		arr.append(t)

	return arr

def invMatrix(arr):
	#print(arr)

	invArr = []
	a = 1
	b = 1

	for i in range(0, len(arr)):
		t = []
		for j in range(0, len(arr[i])):
			if(i != j):
				ans = 26 - (arr[i][j] % 26)

				t.append(ans)
				a *= arr[i][j]
			else:
				t.append(arr[i-1][i-1])
				b *= arr[i][j]

		invArr.append(t)

	#print("===================")
	#print(invArr)
	#print("---")

	det = b - a
	#print(det)
	if(det < 0):
		det = 26 - (abs(det) % 26)

	# >>>>>>>> Multiplicative inverse <<<<<<<<<
	x = 1
	while(True):
		ans = det * x % 26

		if(ans == 1):
			break
		x += 1

	#print(">>>" ,det)
	#print(x)

	for i in range(0, len(invArr)):
		for j in range(0, len(invArr[i])):
			invArr[i][j] = (invArr[i][j] * x) % 26

	return invArr

def partition(msg):
	arr = []

	i = 0
	while(i < len(msg)):
		arr.append(msg[i:i+2])

		i += 2

	return arr

def getMsgMatrix(msg):
	arr = []

	for s in msg:
		a = []

		for i in range(0, 2):
			a.append(
				ord(s[i]) - 65
			)

		arr.append(a)

	return arr

def decryptHillCipher(k, p):
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
	serverName = "127.0.0.1"
	serverPort = 12345

	serverSocket = socket(AF_INET, SOCK_DGRAM)
	serverSocket.bind(("", serverPort))

	key, serverAddress = serverSocket.recvfrom(2048)
	msg, serverAddress = serverSocket.recvfrom(2048)

	key = key.decode()
	msg = msg.decode()

	keyArr = getKeyMatrix(key)
	msgP = partition(msg)
	msgArr = getMsgMatrix(msgP)

	#print(keyArr)
	#print(msgArr)

	keyArr = invMatrix(keyArr)

	print("------------------------------------------------")
	res, resArr = decryptHillCipher(keyArr, msgArr)
	print(res)
	#print(resArr)
