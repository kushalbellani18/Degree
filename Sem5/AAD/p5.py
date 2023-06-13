import matplotlib.pyplot as plt
import random

def bubbleSort(data):
	global counter
	bc = counter

	t = None
	bc += 1

	i = 0
	bc += 1

	while(i < len(data)):
		bc += 1
		j = 0
		bc += 1
		while(j <= i):
			bc += 1

			if(data[i][1] < data[j][1]):
				bc += 1

				t = data[j]
				data[j] = data[i]
				data[i] = t

				bc += 3

			bc += 1
			j += 1
			bc += 1

		bc += 1
		i += 1
		bc += 1

	print("============")
	print("\t Bubble Sort")
	print("------------")
	print("Name | No. of quantities")
	for x in data:
		print(x[0] + " | " + str(x[1]))
	print("")
	print("============")

	return bc

def selectionSort(data):
	global counter
	sc = counter

	t = None
	sc += 1

	i = 0
	sc += 1
	while(i < len(data)):
		t2 = data[i][1]
		sc += 1
		ind = i
		sc += 1

		for j in range(i, len(data)):
			sc += 1

			if(t2 > data[j][1]):
				sc += 1
				t2 = data[j][1]
				ind = j

				sc += 2

			sc += 1

		t = data[ind]
		data[ind] = data[i]
		data[i] = t

		sc += 3
		i += 1
		sc += 1

	print("=============")
	print("\t Selection Sort")
	print("-------------")
	print("Name | No. of quantities")
	for x in data:
		print(x[0] + " | " + str(x[1]))

	print("")
	print("=============")

	return sc

def insertionSort(data):
	global counter
	ic = counter

	i=0
	ic += 1
	while(i < len(data)):
		ic += 1

		j = i - 1
		ic += 1
		while(j >= 0):
			ic += 1

			if(data[i][1] < data[j][1]):
				t = data[i]
				data[i] = data[j]
				data[j] = t

				ic += 3
			else:
				ic += 1
				break

			j -= 1
			ic += 1

		i += 1

	print("=============")
	print("\t Insertion Sort")
	print("-------------")
	print("Name | No. of quantities")
	for x in data:
		print(x[0] + " | " + str(x[1]))

	print("")
	print("=============")

	return ic

def enterData():
	global counter
	counter = 0

	n = int(input("Enter a number of items: "))
	counter += 1
	data = []
	counter += 1
	d = None
	counter += 1

	for i in range(0, n):
		sum = 0
		d = []
		counter += 1

		d.append("Item " + str(i+1))
		counter += 1

		s = random.randint(1, 100)
		d.append(s)
		counter += 1

		counter += 1
		data.append(d)
		counter += 1
		print("")


	print(data)

	b = bubbleSort(data)
	print("++++++++++++++++++++++++++++++++++++++++")
	print("++++++++++++++++++++++++++++++++++++++++")
	i = insertionSort(data)
	print("++++++++++++++++++++++++++++++++++++++++")
	print("++++++++++++++++++++++++++++++++++++++++")
	s = selectionSort(data)

	try:
		f = open("file/p5.txt", "a")

		f.write(str(len(data)) + "," + str(b) + "," + str(i) + "," + str(s) + "\n")

		f.close()
	except Exception as e:
		print(e)

def displayData():
	try:
		f = open("file/p5.txt", "r")
		data = []

		str = f.readline()
		while(str):
			data.append(str.split(","))
			str = f.readline()

		print(data)

		n = [int(x[0]) for x in data]
		b = [int(x[1]) for x in data]
		i = [int(x[2]) for x in data]
		s = [int(x[3]) for x in data]

		n.sort()
		b.sort()
		i.sort()
		s.sort()

		plt.subplot(2, 1, 1)
		plt.plot(n, b, label="Bubble Sort")
		plt.plot(n, i, label="Insertion Sort")
		plt.plot(n, s, label="Selection Sort")
		plt.legend()
		plt.title("Plot")

		plt.subplot(2, 1, 2)
		plt.axis("off")
		plt.table(cellText = data, colLabels = ["N", "Bubble Sort", "Insertion Sort", "Selection Sort"], loc = "center")
		plt.title("Table")

		plt.suptitle("Sort Technique")
		plt.show()

	except Exception as e:
		print(e)

if __name__ == "__main__":
	while(1):
		print("0) Exit")
		print("1) Enter Data")
		print("2) Display Data")
		ch = int(input("Enter your choice? "))

		if(ch == 0):
			break
		elif(ch == 1):
			counter = None
			enterData()
		elif(ch == 2):
			displayData()
