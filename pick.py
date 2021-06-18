import pickle
l=pickle.load(open("bcd.pickle","rb"))
d={}
def stud():
	
	na=input("enter the name:")
	ag=int(input("enter the age:"))
	d={"name":na,"age":ag}
	l.append(d)
	pickle.dump(l,open("bcd.pickle","wb"))
def readobject():
	l=pickle.load(open("bcd.pickle","rb"))
	print(l)
def menu():
	n=0
	while(n!=3):
		print("1.registration")
		print("2.view")
		print("3.exist")
		n=int(input("enter ur choice:"))
	
		if(n==1):
			stud()
		elif(n==2):
			readobject()
		else:
			print("exist")
menu()