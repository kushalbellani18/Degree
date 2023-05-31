def removeSpecialChar(word):
	word = word[0:len(word)-1]

	return word

if __name__ == "__main__":
	msg = input("Enter msg: ")

	arr = msg.split(' ')
	dis = []
	rep = []

	for i in range(0, len(arr)):
		word = arr[i]

		if word[-1] in ['.', ',', ';', '!']:
			word = removeSpecialChar(word)

		if word not in dis:
			dis.append(word)
		else:
			if(word not in rep):
				rep.append(word)

	print(dis)
	print(rep)
