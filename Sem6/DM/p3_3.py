if __name__ == "__main__":
	elements = [a for a in range(-100, 101)]
	logicElements = []

	for a in elements:
		if((a**2) >= 0):
			logicElements.append(True)
		else:
			logicElements.append(False)

	for i in range(0, len(elements)):
		print(str(elements[i]) + ": " + str(logicElements[i]))

