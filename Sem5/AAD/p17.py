if __name__ == "__main__":
	numberOfStudents = int(input("Enter a number of students: "))
	studentMarks = []
	candies = []

	for i in range(0, numberOfStudents):
		m = int(input("Student " + str(i+1) + " marks: "))
		studentMarks.append(m)

	candies.append(1)
	for i in range(1, numberOfStudents):
		if(studentMarks[i] > studentMarks[i-1]):
			candies.append(candies[i-1] + 1)
		else:
			#candies.append(candies[i-1] - 1)
			candies.append(1)

	print("Student Marks: ", studentMarks)
	print("Candy List : ", candies)
	print("Total: ", sum(candies))
