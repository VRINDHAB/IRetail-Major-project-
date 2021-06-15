class Stud:
	def __init__(self):
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
class Studprofile(Stud):
	def __init__(self):
		super().__init__()
		self.phn=int(input("enter the phn no:"))
		self.adress=input("enter the adress:")
	def print(self):
		super().print()
		print("phn no:",self.phn)
		print("adress:",self.adress)	

o1=Studprofile()
o1.print()
o1.edit()
