import hashlib
import playfair as pf

def numToStr(txt):
	d = dict()

	for i in range(0, 10):
		d[i] = chr(ord('A') + i)

	txt2 = ""
	for t in txt:
		if(t.isnumeric()):
			txt2 += d[int(t)]
		else:
			txt2 += t

	return txt2

def replaceJ(msg):
	msg2 = ""

	for m in msg:
		if m == 'J':
			msg2 += 'I'
		else:
			msg2 += m

	return msg2

if __name__ == "__main__":
	message = input("Enter a message: ").upper()
	key = input("Your key: ").upper()

	# Hashlib

	hashMsg = hashlib.sha256()
	hashMsg.update(message.encode())

	message += "ZZ"
	message += hashMsg.hexdigest()

	message = message.upper()

	message = numToStr(message)

	message = replaceJ(message)

#	print(">> ", message)
#	print(">> Encrypt: ", pf.encrypt("KUSHAL", message))

	# Write a message and key to the file.
	f = open('file/secure.txt', 'w')

	f.write(key + "/" + pf.encrypt(key, message))

	f.close()

	print("Done!")
