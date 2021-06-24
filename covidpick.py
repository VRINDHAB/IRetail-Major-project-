import pickle
class Userdetials:
	def __init__(self):
		self.name=""
		self.age=0
		self.place=""
		self.mobile=0
		self.adress=""
		self.co_pan=""
		self.district=""
		self.state=""
		self.postivedate=0
		self.negdate=0
		self.currentstat=True
	def read(self):
		self.name=input("enter name")
		self.age=int(input("enter age"))
		self.place=input("enter place")
		self.mobile=int(input("enter mobile : "))
		self.adress=input("enter adress")
		self.co_pan=input("enter co or pan")
		self.district=input("enter district")
		self.state=input("enter state")
		self.postivedate=int(input("enter postive date"))
	def print(self):
		print("......Corna portal.......")
		print("NAME:",self.name)
		print("AGE:",self.age)
		print("PLACE:",self.place)
		print("MOBILE:",self.mobile)
		print("ADFRESS:",self.adress)
		print("co or pan:",self.co_pan)
		print("DISTRICT:",self.district)
		print("STATE:",self.state)
		print("POSTIVE DATE:",self.postivedate)
		print("current STATUE:",self.currentstat)
	def update(self):
		print("......STATUS......")
		self.currentstat=False
		self.negdate=int(input("enter  negative dte:"))
		print("covid negative",self.negdate)
	
		