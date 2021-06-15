class Stud:
	def read(self):
		self.n=input("enter ur name")
		self.a=int(input("enter ur age"))
	def print(self):
		print("name",self.n)
		print("age",self.a)
	def edit(self):
		x=input("enter the name to be edit")
		y=int(input("enter the new age"))
		if(x==self.n):
			self.a=y
		print("name",self.n)
		print(" changed age",self.a)
o=Stud()
o.read()
o.print()
o.edit()
#o.read() error kanikkum last vilicha allagil __init__ kodukk
