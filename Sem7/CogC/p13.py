import cv2

if __name__ == "__main__":
	cap = cv2.VideoCapture(0)
	cap.set(3, 1366)
	cap.set(4, 768)

	# Reading the image
	# img = cv2.imread('...')

	# Importing cascade classifiers
	faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades +  "haarcascade_frontalface_default.xml")

	# Face Detection
	while True:
		success, img = cap.read()

		# Converting into grey
		imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

		# Getting the corners around the face
		faces = faceCascade.detectMultiScale(imgGrey, 1.2, 5)

		# Drawing bounding box around the face
		for (x, y, w, h) in faces:
			img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

		# Eye Detection


		# Opening camera window
		cv2.imshow('face_detect', img)
		if cv2.waitKey(10) & 0xFF == ord('q'):
			break

	cap.release()
	cv2.destroyWindow('face_detect')
