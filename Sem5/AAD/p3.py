global_t = 0

def sumCall(n, tot):
	global global_t
	global_t += 1

	if(n != 0):
		global_t += 1
		tot = sumCall(n-1, (tot+n))

	return tot

if __name__ == "__main__":
	# ------------------------ For loop ------------------------------
	loop_t = 0
	lsum = 0
	n = int(input("Enter a number of client: "))

	for i in range(1, (n+1)):
		lsum += i
		loop_t += 1

	print("=========> Loop <==========")
	print(str(lsum) + " -> " + str(loop_t) + " steps")
	print("\n")

	# ------------------------- For Rescusive ---------------------------

	global_t
	rsum = sumCall(n, 0)

	print("==========> Rescusion <========")
	print(str(rsum) + " -> " + str(global_t) + " steps")
	print("\n")

	# --------------------------- For Formula ---------------------------

	formula_t = 0
	fsum = (n * (n+1)) / 2
	formula_t += 1

	print("==========> Formula <=========")
	print(str(fsum) + " -> " + str(formula_t) + " steps")
	print("\n")

	try:
		f = open("file/p3.txt", 'a')
		s = str(n) + "," + str(loop_t) + "," + str(global_t) + "," + str(formula_t)

		f.write(s)
		f.write("\n")

	except Exception as e:
		print(e)
