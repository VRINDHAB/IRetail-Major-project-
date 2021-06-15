l=[]
class menu:
	def menuu(self):
		global l
		print(";;;;;;;;;;;;;;;;;;;;;;")
		print("corono protal")
		print("::::::::::::::::::::::::::")
		print("1.registeration")
		print("2.mark negative")
		print("3,current number of postive patient")
		print("4,srch")
		print("5. back")
		print(".........................................")
		n=int(input("enter the choice"))
		print("...................................")
		return(n)
class patient:
	global l
	def pat(self):
		p=int(input("enter the limit"))
		for i in range(p):
			print(".............................")
			print("enter the detials of corono patients")
			print("................................")
			self.rollno=int(input("enter the rollno"))
			self.name=input("enter the name")
			self.age=int(input("enter the age "))
			self.mob=int(input("enter the mob"))
			self.adress=input("enter the adress")
			self.panchayat=input("enter the panchayat/corporation")
			self.status=input("currently postive or negative")
			print("..............................")
			d={"rollno":"self.rollno","name":"self.name","age":"self.age","mob":"self.mob","adress":"self.adress","panchayat":"self.panchayat","status":"self.status"}
			l.append(d)
			print(l)
	def marknegative(self):
		global l
		self.u=int(input("enter the register no of patient to mark negative"))
		for i in l:
			if(i["rollno"]==self.u):
				i["status"]="negative"
		print(l)
	def currentpostive(self):
		global l
		self.c=0
		for i in l:
			if(i["status"]=="postive"):
				self.c=self.c+1
		print("currently postive",slef.c)
	def panchayat(self):
		global l
		self.m=0
		self.x=0
		for i in l:
			if(i["status"]=="postive"):
				if(i["panchayat"]=="tvm"):
					self.m+=1
				else:
					self.x+=1
		print("tvm postive cases",self.m)
		print("panchayat postive caeses",self.x)
	def main(self):
		n=0
		global l
		while(n!=5):
		n=menuu()
		
		
		
o=menu()
o.menuu()
o1=patient()
