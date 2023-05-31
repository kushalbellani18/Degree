from socket import *

def getKeyMatrix():
	arr = []

	for i in range(0, 26):
		t = []
		for j in range(i, 26+i):
			t.append(j % 26)

		arr.append(t)

	return arr

def decryptVigenereCipher(msg, key):
	keyMatrix = getKeyMatrix()

	encrypt = ""

	for i in range(0, len(msg)):
		c = ord(msg[i]) - 65
		r = ord(key[i]) - 65

		for j in range(0, len(keyMatrix[r])):
			if(c == keyMatrix[r][j]):
				encrypt += chr(j + 65)
				break

	return encrypt

if __name__ == "__main__":
	serverName = "127.0.0.1"
	serverPort = 12345

	serverSocket = socket(AF_INET, SOCK_DGRAM)
	serverSocket.bind(("", serverPort))

	msg, serverAddress = serverSocket.recvfrom(2048)

	msg = msg.decode()
	msg = msg.split(" ")

	key = msg[1]
	msg = msg[0]

	print(key)
	print(msg)

	key2 = ""
	for i in range(0, len(msg)):
		key2 += key[int(i%len(key))]

	res = decryptVigenereCipher(msg, key2)
	print(res)
