from experta import *

class sym(KnowledgeEngine):
	@Rule(Fact(no = MATCH.a),
		TEST(lambda a: a > 4)
	)
	def hello(self):
		print("Warning! you got covid!")

	@Rule(Fact(no = MATCH.a),
		TEST(lambda a: a > 1 and a <= 4)
	)
	def hello2(self):
		print("Either Flu or covid!")

	@Rule(Fact(no = MATCH.a),
		TEST(lambda a: a == 1)
	)
	def hello3(self):
		print("Flu!")

if __name__ == "__main__":
	s = sym()
	s.reset()
	noDays = int(input("How many days, you feel unwell? "))
	s.declare(Fact(no = noDays))
	s.run()
