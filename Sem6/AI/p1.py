from experta import *

class weather(Fact):
	pass

class sky(KnowledgeEngine):
	@DefFacts()
	def enjoyAI(self):
		ch = input("Is it rainy? (y/n)")
		if(ch == 'y'):
			yield weather(we='rainy')
		else:
			ch = input("Is it windy? (y/n)")
			if(ch == 'y'):
				yield weather(we='windy')
			else:
				ch = input("Is it cloudy? (y/n)")
				if(ch == 'n'):
					yield weather(we='sunny')
				else:
					t = int(input("What the temperature (in C)? "))
					if(t >= 15 and t <= 20):
						print("Maybe")
						yield weather(we='rainy')
					elif(t < 15):
						print("Maybe")
						yield weather(we='windy')
					else:
						yield weather(we='sunny')

	@Rule(weather(we = 'rainy'))
	def rainy(self):
		print("Bring Umbrella!")
		print("Take care and Be safety! Wear a mask and maintain a social distance")

	@Rule(weather(we = 'windy'))
	def windy(self):
		print("Bring raincoat!")
		print("Take care and Be safety! Wear a mask and maintain a social distance")

	@Rule(weather(we = 'sunny'))
	def sunny(self):
		print("Take care and Be safety! Wear a mask and maintain a social distance")

if __name__ == "__main__":
	s = sky()
	s.reset()
	s.run()
