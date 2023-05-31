import random
from socket import *

def getRandomKey(len):
	a = ord('A')
	z = ord('Z')

	str = ""
	for i in range(0, len):
		str += chr(random.randint(a, z))

	return str

def getKeyChar(p, k):
	return chr(
		abs((ord(p) + ord(k)
		) % 26)
		+ 65
		)

def encrytOneTimePad(arr, key):
	decryt = []

	for i in range(0, len(arr)):
		str = ""
		for j in range(0, len(arr[i])):
			str += getKeyChar(arr[i][j], key[i][j])

		decryt.append(str)

	#print(decryt)
	return "".join(decryt)

if __name__ == "__main__":
	msg = input(">> ").upper()
	arr = msg.split(' ')

	key = []
	for a in arr:
		key.append(getRandomKey(len(a)))

	res = encrytOneTimePad(arr, key)
	key = "".join(key)

	print(res)
	print(key)

	# >>>> Socket <<<<
	serverName = "127.0.0.1"
	serverPort = 12345

	clientSocket = socket(AF_INET, SOCK_DGRAM)
	clientSocket.sendto((res+key).encode(), (serverName, serverPort))

	clientSocket.close()
