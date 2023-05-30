from socket import *

def getDataList(msg):
	global data

	list = []
	key = 0

	while(key < 26):
		str = ""
		for c in msg:
			if c == " ":
				str += " "
			else:
				number = (data[c] - key) % 26
				for k, v in data.items():
					if(v == number):
						str += k
		list.append(str)
		key += 1

	return list

if __name__ == "__main__":
	serverName = "127.0.0.1"
	serverPort = 12345

	serverSocket = socket(AF_INET, SOCK_DGRAM)
	serverSocket.bind(("", serverPort))

	getMsg, serverAddress = serverSocket.recvfrom(2048)

	cleanMsg = getMsg.decode()

	# <<<<--- Find data with the help of bruteforce attack! ---->>>>
	data = {}

	i = 0
	while(i < 26):
		var = chr(i + 97)
		data[var] = i
		i += 1

	arr = getDataList(cleanMsg)

	print("Key --> Value")
	for i in range(0, len(arr)):
		print(i, end=" --> ")
		print(arr[i])
