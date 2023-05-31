from socket import *

def getKeyChar(c, k):
	return (chr(
		((ord(c) - ord(k)) % 26) + 65
	))

def decrytOneTimePad(msg, key):
	encryt = []
	str = ""

	for i in range(0, len(msg)):
		str += getKeyChar(msg[i], key[i])

	return str

if __name__ == "__main__":
	serverName = "127.0.0.1"
	serverPort = 12345

	serverSocket = socket(AF_INET, SOCK_DGRAM)
	serverSocket.bind(("", serverPort))

	msg, serverAddress = serverSocket.recvfrom(2048)

	msg = msg.decode()

	key = msg[int(len(msg) / 2) :]
	msg = msg[0:int(len(msg) /2)]

	print(key)
	print(msg)

	res = decrytOneTimePad(msg, key)

	print(res)
