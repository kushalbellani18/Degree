from socket import *

def encryptMsg(msg, key):
	global data
	msg2 = ""

	for c in msg:
		if(c == ' '):
			msg2 += ' '
		else:
			number = (data[c] + key) % 26
			for k, v in data.items():
				if(v == number):
					msg2 += k

	return msg2

if __name__ == "__main__":
	data = {}

	i = 0
	while(i < 26):
		var = 97
		data[chr(var + i)] = i
		i += 1

	key = 15

	msg = input("Enter: ")
	msg = msg.lower()
	msg2 = encryptMsg(msg, key)
	# print(msg2)

	## <<<<----- Socket------->>>>
	serverName = "127.0.0.1"
	serverPort = 12345

	clientSocket = socket(AF_INET, SOCK_DGRAM)

	clientSocket.sendto(msg2.encode(), (serverName, serverPort))

	clientSocket.close()
