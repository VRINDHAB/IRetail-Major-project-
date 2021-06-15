class Demo:
	def __init__(self):
		self.a=10
	def read(self):
		self.a=int(input("enter the num"))
	def print(self):
		print(self.a)
o1=Demo()
o1.read()
o1.print()
o2=Demo()
o2.read()
o2.print()
o3=Demo()
o3.a=0
o3.a=o1.a+o2.a
print(o3.a)