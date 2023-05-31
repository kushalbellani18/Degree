from experta import *

class scanFace(KnowledgeEngine):

	@Rule(Fact(mood='happy'), OR(Fact(status='positive'), Fact(status='unsure')))
	def happy1(self):
		print("==> Smile!")

	@Rule(Fact(mood='happy'), Fact(status='negative'))
	def happy2(self):
		print("==> Nod")

	@Rule(Fact(mood='sad'), OR(Fact(status='positive'), Fact(status='negative'), Fact(status='unsure')))
	def sad(self):
		print("==> Frown!")

	@Rule(Fact(mood='neutral'), OR(Fact(status='positive'), Fact(status='negative')))
	def neutral1(self):
		print("==> Nod")

	@Rule(Fact(mood='neutral'), OR(Fact(status='unsure')))
	def neutral2(self):
		print("==> Blink!")

if __name__ == "__main__":
	sf = scanFace()
	sf.reset()

	a = input("Enter mood: ")
	b = input("Enter status: ")
	c = (a, b)

	sf.declare(Fact(mood=c[0], status=c[1]))
	sf.run()
