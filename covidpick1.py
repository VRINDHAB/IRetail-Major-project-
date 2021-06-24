import pickle
from covidpick import Userdetials
l=pickle.load(open("xyz.pickle","rb"))
def menu():
	n=0
	global l
	while(n!=5):
		print("1.REGISTERATION")
		print("2.PRINT")
		print("3.UPDATE")
		print("4. VIEW ALL ")
		print("5.EXIT")
		n=int(input("enter an option:"))
		if(n==1):
			print("....REGISTRATION....")
			o=Userdetials()
			o.read()
			l.append(o)
			pickle.dump(l,open("xyz.pickle","wb"))
		elif(n==2):
			print("....PRINT....")
			na=input("enter the name:")
			for i in l:
				if(na==i.name):
					i.print()
		elif(n==3):
			print("....UPDATE....")
			p=input("enter the name to be update:")
			for i in l:
				if(p==i.name):
					i.update()
			pickle.dump(l,open("xyz.pickle","wb"))
		elif(n==4):
			for i in l:
				i.print()
				print("++++++++++")
		else:
			print("EXIST")

menu()
	