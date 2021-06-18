import pickle
class Stud7:
	def __init__(self):
		self.name=""
		self.age=0
	def read(self):
		self.name=input("enter the name :")
		self.age=int(input("enter the age :"))
	def print(self):
		print("NAME:",self.name)
		print("AGE:",self.age)
def create():
	o=Stud7()
	o.read()
	o.print()
	pickle.dump(o,open("abc.pickle","wb"))

