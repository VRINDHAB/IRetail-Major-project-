class Mod:
	def __init__(self):
		self.a=0
		self.b=" "
	def read(self):
		self.a=int(input("enter a number:"))
		self.b=input("enter ur name:")
	def print(self):
		print(self.a)
		print(self.b)
