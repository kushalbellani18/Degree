import matplotlib.pyplot as plt

global_t = 0
arr = []

def sumCall(n, tot, lol):
	global global_t
	global arr

	global_t += 1
	if(n != 0):
		global_t += 1
		tot = sumCall(n-1, tot+n, lol+arr[n-1])

	if(n == 0):
		print("Total using recusive: " + str(lol))

	return tot

def goToAddData():
	global global_t
	global arr
	# -------------------- For Loop -----------------------------
	loop_t = 0
	lol = 0
	lsum = 0

	companyName = input("Enter a company name: ")
	n = int(input("Enter a number of Client: "))

	print("Enter list of " + str(n) + " employee's salary")
	for i in range(1, (n+1)):
		why = int(input())

		arr.append(why)

		lol += arr[i-1]

		lsum += i
		loop_t += 1

	print("")
	print("Total using iterative: " + str(lol))


	# ------------------- For Rescusive -----------------------
	global_t = 0
	rsum = sumCall(n, 0, 0)

	# ------------------- For Formula -------------------------
	formula_t = 0
	fsum = 0

	fsum = (n * (n+1)) / 2
	formula_t += 1

	print("===================================================")
	print("\n")
	print("\t\t\t\t Analysis Performance")
	print("")
	print("===================================================")

	# ------------------- Display -------------------
	print("Loop")
	print("Sum: " + str(lsum) + " & Steps: " + str(loop_t))
	print("")
	print("Rescusive")
	print("Sum: " + str(rsum) + " & Steps: " + str(global_t))
	print("")
	print("Formula")
	print("Sum: " + str(fsum) + " & Steps: " + str(formula_t))
	print("")

	# --------------------- Write to File -------------------------
	try:
		f = open("file/p3.txt", 'a')

		f.write(str(lsum) + "," + str(loop_t) + "," + str(global_t) + "," + str(formula_t))
		f.write("\n")

		f.close()
	except Exception as e:
		print(e)

def goToDisplayData():
	try:
		f = open("file/p3.txt", "r")
		s = f.readline()
		data = []

		while(s):
			data.append(s.split(','))
			s = f.readline()

		n = [int(x[0]) for x in data]
		l = [int(x[1]) for x in data]
		r = [int(x[2]) for x in data]
		f = [int(x[3]) for x in data]

		n.sort()
		l.sort()
		r.sort()
		f.sort()

		plt.subplot(2, 1, 1)
		plt.plot(n, l, label="Iterative")
		plt.plot(n, r, label="Rescusive")
		plt.plot(n, f, label="Formula")
		plt.legend()
		plt.title("Plot")

		plt.subplot(2, 1, 2)
		plt.axis("off")
		plt.table(cellText = data, colLabels = ["N", "Iterative", "Rescusive", "Formula"], loc="center")
		plt.title("Table")

		plt.suptitle("Sum from 1 to N")
		plt.show()
	except Exception as e:
		print(e)

if __name__ == "__main__":
	while(True):
		print("=========> Welcome <==========")
		print("0 -> Exit")
		print("1 -> Add new data")
		print("2 -> Display Chart")
		ch = int(input("Enter your choice? "))

		if ch==0:
			break
		elif ch == 1:
			goToAddData()
		elif ch == 2:
			goToDisplayData()

		print("-----------------------")
		print("")

	print("Exit")
