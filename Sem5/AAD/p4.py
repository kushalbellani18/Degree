import matplotlib.pyplot as plt

def goToDisplay():
	try:
		f = open("file/p4.txt", "r")
		r = f.readline()
		data = []

		while(r):
			data.append(r.split(","))
			r = f.readline()

		n = [int(x[0]) for x in data]
		i = [int(x[1]) for x in data]
		r = [int(x[2]) for x in data]

		plt.subplot(2, 1, 1)
		plt.plot(n, i, label="Iterative")
		plt.plot(n, r, label="Recusive")
		plt.legend()
		plt.title("Plot")

		plt.subplot(2, 1, 2)
		plt.axis("off")
		plt.table(cellText = data, colLabels=["N", "Iterative", "Recusive"], loc="center")
		plt.title("Table")

		plt.show()

	except Exception as e:
		print(e)

def callR(arr, n, tR, a, b):
	tR += 3

	if(n != 0):
		tR += 1

		arr.append(a)
		tR += 1

		temp = a + b
		tR += 1
		a = b
		tR += 1
		b = temp
		tR += 1

		tR = callR(arr, (n-1), tR, a, b)

	tR += 1

	return tR

def goToRecusive(n):
	arr = []
	t = callR(arr, n, 0, 0, 1)

	print("Using Rescusive method: ")
	print(arr)
	print("Steps: " + str(t))
	print("Total pair in 1 year approximately: " + str(arr[-1]))

	return t

def goToIterative(n):
	# global tI
	tI = 0

	temp = 0
	tI += 1
	arr = []
	tI += 1

	a = 0
	tI += 1
	b = 1
	tI += 1

	i = 0
	while(i < n):
		tI += 1

		arr.append(a)
		tI += 1
		temp = a + b
		tI += 1
		a = b
		tI += 1
		b = temp
		tI += 1

		i += 1

	tI += 1

	print("Using Iterative method: ")
	print(arr)
	print("Steps: " + str(tI))
	print("Total pair in 1 year approximately: " + str(arr[-1]))

	return tI

if __name__ == "__main__":
	while(True):
		print("---------==> Welcome <==---------")
		print("1) Enter data")
		print("2) Display data")
		print("0) Exit")
		ch = int(input("Enter your choice: "))

		if(ch == 1):
			n = int(input("Enter a number: "))
			tI = goToIterative(n)
			#global tI
			print("--------")
			tR = goToRecusive(n)
			#global tR
			print("--------")

			try:
				f = open("file/p4.txt", "a")

				f.write(str(n) + "," + str(tI) + "," + str(tR) + "\n")

				print("+ ------------- +")
				print("  Done Write...")
				print("+ ------------- +")

				f.close()
			except Exception as e:
				print("Error: " + str(e))

		elif(ch == 2):
			goToDisplay()
		elif(ch == 0):
			break
		print("")

	print("Exit!!")
