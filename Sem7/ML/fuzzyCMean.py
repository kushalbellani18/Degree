import math

class FuzzyCMean:
	def __init__(self, data, k, p, w=None):
		self.data = data
		self.k = k
		self.p = p
		self.w = w
		self.c = None

	def computeCentroid(self):
		self.c = []

		for j in range(0, self.k):
			tot = 0
			tot_u_0 = 0
			tot_u_1 = 0

			for i in range(0, len(self.data)):
				tot += self.w[i][j] ** self.p

				tot_u_0 += (self.w[i][j] ** self.p) * self.data[i][0]
				tot_u_1 += (self.w[i][j] ** self.p) * self.data[i][1]

			self.c.append([tot_u_0/tot, tot_u_1/tot])


	def euclidean_distance(self, x1, y1, x2, y2):
		return math.sqrt(
			((x1-x2)**2) + ((y1-y2)**2)
		)

	def updateW(self):
		for i in range(0, len(self.data)):
			for j in range(0, self.k):
				tot = 0
				for a in range(0, self.k):
					dist = self.euclidean_distance(self.data[i][0], self.data[i][1], self.c[a][0], self.c[a][1])
					tot += ( (1/dist) ** (1 / (self.p - 1)) )

				dist = self.euclidean_distance(self.data[i][0], self.data[i][1], self.c[j][0], self.c[j][1])
				lol = ( (1/dist) ** (1/(self.p-1)) )

				self.w[i][j] = round( (lol / tot), 4)

	def fit(self):
		if self.w == None:
			self.w = []
			print(self.k)

			for i in range(0, len(self.data)):
				wt = []
				for j in range(0, self.k):
					wt.append(1/self.k)
				self.w.append(wt)

		self.display(self.w)
		print(self.c)

		self.computeCentroid()
		self.updateW()

		oldCentroid = self.copyData(self.c)

		while True:
			self.computeCentroid()
			self.updateW()

			print(self.c)

			if(oldCentroid == self.c):
				break

			oldCentroid = self.copyData(self.c)

		self.display(self.w)

	def copyData(self, c):
		c1 = []

		for i in range(0, len(c)):
			c11 = []
			for j in range(0, len(c[i])):
				c11.append(c[i][j])

			c1.append(c11)

		return c1

	def display(self, arr):
		print("------------")
		for i in range(0, len(arr)):
			for j in range(0, len(arr[i])):
				print(arr[i][j], end=" ")
			print("")

		print("-----------")


if __name__ == "__main__":
	w = [
		[0.4, 0.6],
		[0.88, 0.12],
		[0.41, 0.59],
		[0.27, 0.73]
	]

	l = FuzzyCMean(data=[[1, 2], [2, 3], [9, 4], [10, 1]], k=2, p=2, w=w)
	l.fit()
