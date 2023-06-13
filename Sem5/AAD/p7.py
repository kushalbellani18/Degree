import random
import matplotlib.pyplot as plt

def linearGetResult(data, fN, t):
	t += 1
	for i in range(0, len(data)):
		t += 1
		if(fN == data[i]):
			t += 1
			return 302, t
		t += 1

	t += 1

	return 404, t

def getResult(data, l, r, fN, t):
	size = (r - l) + 1
	t += 1

	if(l <= r):
		t += 1

		size = int(size/2)
		size = (l + size)

		t += 2

		mid = data[size]
		t + 1
		# print(mid, " ---> ", size, " => ", l, " to ", r , " = ", (r-l)+1)

		if(mid == fN):
			t += 1
			# print("Found")
			return 302, t
		elif(mid > fN):
			t += 1

			return getResult(data, l, size-1, fN, t)
		else:
			t += 1

			return getResult(data, size+1, r, fN, t)
	else:
		t += 1

		return 404, t

def enterData():
	t = 0

	n = int(input("Enter no. of employee: "))
	data = []
	t += 2

	for i in range(0, n):
		t += 1
		while(1):
			t += 1
			e = random.randint(1, n+10)
			t += 1
			if(e not in data):
				t += 1
				data.append(e)
				break
			t += 1
		t += 1

	print(data)
	findNo = int(input("Find roll no. of employee: "))
	t += 1

	print("=================> Linear Search <==================")
	value, tl = linearGetResult(data, findNo, t)
	print("Found!") if value == 302 else print("Not Found!")
	print("--> Time: ", tl)


	print("=================> Binary Search <==================")
	data.sort()
	t += 1
	value, tb = getResult(data, 0, n-1, findNo, t)
	print("Found!") if value == 302 else print("Not Found!")
	print("--> Time: ", tb)

	try:
		f = open("file/p7.txt", "a")

		f.write(str(n) + "," + str(tl) + "," + str(tb) + "\n")

		f.close()
	except Exception as e:
		print("Error: ", e)

def displayData():
	try:
		f = open("file/p7.txt", "r")
		s = f.readline()
		data = []

		while(s):
			data.append(s.split(','))
			data[len(data)-1][0] = int(data[len(data)-1][0])
			s = f.readline()

		data.sort()

		n = [x[0] for x in data]
		l = [int(x[1]) for x in data]
		b = [int(x[2]) for x in data]

		plt.subplot(2, 1, 1)
		plt.plot(n, l, label="Linear Search")
		plt.plot(n, b, label="Binary Search")
		plt.legend()
		plt.title("Chart")

		plt.subplot(2, 1, 2)
		plt.axis("off")
		plt.table(cellText=data, colLabels=["N", "Linear Search", "Binary Search"], loc="center")
		plt.title("Table")

		plt.suptitle("Search")
		plt.show()

	except Exception as e:
		print("Error: ", e)

if __name__ == "__main__":
	while(1):
		print("1) Enter data")
		print("2) Display data")
		print("0) Exit")
		ch = int(input("Enter your choice? "))

		if(ch == 0):
			break
		elif(ch == 1):
			enterData()
		elif(ch == 2):
			displayData()

		print("")
		print("---------------------------------")
		print("")
