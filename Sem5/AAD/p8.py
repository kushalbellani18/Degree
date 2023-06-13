import random
import matplotlib.pyplot as plt

def straightMinMax(arr, t):
	min = arr[0]
	max = arr[0]
	t += 3

	for i in range(1, len(arr)):
		if(arr[i] < min):
			min = arr[i]
			t += 1
		t += 1

		if(arr[i] > max):
			max = arr[i]
			t += 1
		t += 1

	t += 1

	print("Min: ", min)
	print("Max: ", max)
	t += 2

	return t

def callFunc(arr, min, max, index, t1):

	if(index < len(arr)):
		if(arr[index] < min):
			min = arr[index]
			t1 += 1
		t1 += 1

		if(arr[index] > max):
			max = arr[index]
			t1 += 1
		t1 += 1

		min, max, t1 = callFunc(arr, min, max, index+1, t1)

	t1 += 1

	return min, max, t1

def divideConquerMinMax(arr, t):
	min = arr[0]
	max = arr[0]
	t1 = t

	min, max, t1 = callFunc(arr, min, max, 1, t1)

	print("Min: ", min)
	print("Max: ", max)

	return t1

def goToEnterData():
	t = 0

	n = int(input("Enter a number of elements: "))
	arr = []
	t += 2

	for i in range(0, n):
		lol = random.randint(1, 100)
		print("Item-", str(i+1), ": ", str(lol))
		arr.append(lol)
		t += 3

	print("")
	print("----> Straight <----")
	ts = straightMinMax(arr, t)
	print(ts)

	print("")
	print("----> Divide & Conquer <----")
	tdc = divideConquerMinMax(arr, t)
	print(tdc)

	try:
		f = open("file/p8.txt", "a")

		f.write(str(n) + "," + str(ts) + "," + str(tdc) + "\n")

		f.close()
	except Exception as e:
		print("Error: ", e)

def goToDisplayData():
	try:
		f = open("file/p8.txt", "r")
		s = f.readline()
		data = []

		while(s):
			data.append(s.split(','))
			data[len(data)-1][0] = int(data[len(data)-1][0])
			s = f.readline()

		data.sort()

		n = [x[0] for x in data]
		ts = [int(x[1]) for x in data]
		tdc = [int(x[2]) for x in data]

		plt.subplot(2, 1, 1)
		plt.plot(n, ts, label="Straight")
		plt.plot(n, tdc, label="Divide & Conquer")
		plt.legend()
		plt.title("Plot")

		plt.subplot(2, 1, 2)
		plt.axis("off")
		plt.table(cellText=data, colLabels=["N", "Straight", "Divide & Conquer"], loc="center")
		plt.title("Table")

		plt.suptitle("Min-Max Problem")
		plt.show()

	except Exception as e:
		print("Error: ", e)

if __name__ == "__main__":
	print("===========|> Flipkart <| =============")
	print("")

	while(1):
		print("1) Enter data")
		print("2) Display data")
		print("0) Exit")
		ch = int(input("Enter your choice? "))

		if(ch == 1):
			goToEnterData()
		elif(ch == 2):
			goToDisplayData()
		elif(ch == 0):
			break
		print("")
		print("")
