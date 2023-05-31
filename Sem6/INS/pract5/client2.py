from socket import *

def display(arr):
	for i in range(0, len(arr)):
		for j in range(0, len(arr[i])):
			print(arr[i][j], end=" ")
		print("")

	print("")

def getKeyMatrix():
	arr = []

	for i in range(0, 26):
		t = []
		for j in range(i, 26+i):
			t.append(j % 26)

		arr.append(t)

	return arr

def encrytVigenereCipher(msg, key):
	keyMatrix = getKeyMatrix()

	decryt = ""

	for i in range(0, len(msg)):
		r = ord(msg[i]) - 65
		c = ord(key[i]) - 65

		decryt += chr(keyMatrix[r][c] + 65)

	return decryt

if __name__ == "__main__":
	msg = input("Plain Text>> ").upper()
	key = input("Key>> ").upper()

	key2 = ""
	for i in range(0, len(msg)):
		key2 += key[int(i % len(key))]

	res = encrytVigenereCipher(msg, key2)

	# >>>>>> Socket <<<<<<
	serverName = "127.0.0.1"
	serverPort = 12345

	clientSocket = socket(AF_INET, SOCK_DGRAM)
	clientSocket.sendto((res + " " + key).encode(), (serverName, serverPort))

	clientSocket.close()
