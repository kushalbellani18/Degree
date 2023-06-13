import matplotlib.pyplot as plt

def bubbleSort(data):
	global counter
	bcounter = counter

	t = None
	bcounter += 1

	i = 0
	bcounter += 1

	while(i < len(data)):

		bcounter += 1
		j = 0
		bcounter += 1
		while(j <= i):
			bcounter += 1

			if(data[i][5] > data[j][5]):
				bcounter += 1

				t = data[j]
				data[j] = data[i]
				data[i] = t

				bcounter += 3

			bcounter += 1
			j += 1
			bcounter += 1

		bcounter += 1
		i += 1
		bcounter += 1

	print("==============")
	print("\t Bubble Sort ")
	print("--------------")
	print("Name | Year 1 | Year 2 | Year 3 | Year 4 | Avg.")
	for x in data:
		print(x[0] + " | " + str(x[1]) + " | " + str(x[2]) + " | " + str(x[3]) + " | " + str(x[4]) + " | " + str(x[5]))

	print("")
	print("Highest Mark --> " + data[0][0] + " ( " + str(data[0][5]) + " )")
	print("==============")

	return bcounter

def insertationSort(data):
	global counter
	icounter = counter

	t = None
	icounter += 1

	i = 0
	icounter += 1
	while(i<len(data)):
		max = data[i][5]
		icounter += 1
		ind = i
		icounter += 1

		for j in range(i, len(data)):
			icounter += 1

			if(max < data[j][5]):
				icounter += 1
				max = data[j][5]
				ind = j

				icounter += 2

			icounter += 1

		t = data[ind]
		data[ind] = data[i]
		data[i] = t

		icounter += 3
		i += 1
		icounter += 1

	print("=============")
	print("\t Insertation Sort ")
	print("-------------")
	print("Name | year 1 | year 2 | year 3 | year 4 | Avg. ")
	for x in data:
		print(x[0] + " | " + str(x[1]) + " | " + str(x[2]) + " | " + " | " + str(x[3]) + " | " + str(x[4]) + " | " + str(x[5]))
	print("")
	print("Highest Mark --> " + data[0][0] + " ( " + str(data[0][5]) + " )")
	print("==============")

	return icounter

def enterData():
	global counter
	counter = 0

	n = int(input("Enter a number of students: "))
	counter += 1
	data = []
	counter += 1
	d = None
	counter += 1

	for i in range(0, n):
		sum = 0
		d = []
		counter += 1

		s = input("Enter student name: ")
		counter += 1
		d.append(s)
		counter += 1

		for j in range(1, 5):
			ex = float(input("Year " + str(j) + " cgpa: "))
			counter += 1

			d.append(ex)
			counter += 1

		for x in range(1, 5):
			sum += d[x]
			counter += 1

		counter += 1

		d.append(sum/4)
		counter += 1
		data.append(d)
		counter += 1
		print("")

	backup = data

	b = bubbleSort(data)
	print("++++++++++++++++++++++++++++++++++++++++")
	print("++++++++++++++++++++++++++++++++++++++++")
	i = insertationSort(data)

	try:
		f = open("file/p6.txt", "a")

		f.write(str(len(data)) + "," + str(b) + "," + str(i) + "\n")

		f.close()
	except Exception as e:
		print(e)

def displayData():
	try:
		f = open("file/p6.txt", "r")
		data = []

		str = f.readline()
		while(str):
			data.append(str.split(","))
			str = f.readline()

		data.sort()

		n = [int(x[0]) for x in data]
		b = [int(x[1]) for x in data]
		i = [int(x[2]) for x in data]

		plt.subplot(2, 1, 1)
		plt.plot(n, b, label="Bubble Sort")
		plt.plot(n, i, label="Insertation Sort")
		plt.legend()
		plt.title("Plot")

		plt.subplot(2, 1, 2)
		plt.axis("off")
		plt.table(cellText = data, colLabels = ["N", "Bubble Sort", "Insertation Sort"], loc = "center")
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
