import playfair as pf
import hashlib

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
	# Get key from file
	f = open('file/secure.txt')

	_, msg = f.read().split('/')

	f.close()

	key = input("Enter your key: ").upper()

	# Decryption
	if('ZZ' in pf.decrypt(key, msg)):
		a, b = pf.decrypt(key, msg).split('ZZ')

		hashMsg = hashlib.sha256()
		hashMsg.update(a.encode())

		finalRes = numToStr(hashMsg.hexdigest().upper())
		finalRes = replaceJ(finalRes)

		if(finalRes == b):
			print("Message: ", a)
		else:
			print("Not success!")
	else:
		print("Error! Get out!")
