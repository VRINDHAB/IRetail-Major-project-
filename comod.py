from covidmod import Userdetials
l=[]
def menu():
	n=0
	global l
	while(n!=5):
		print("1.REGISTERATION")
		print("2.PRINT")
		print("3.UPDATE")
		
		print("5.EXIST")
		n=int(input("enter an option:"))
		if(n==1):
			print("....REGISTRATION....")
			o=Userdetials()
			o.read()
			l.append(o)
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
		#elif(n==4):
			#print("........NO OF STUDENTS IN A PARTICULAR COURSE...")
			#stream=input("enter the course to search:")
			#count=0
			#for i in l:
			#	if(stream==i.course):
			#		count=count+1
			#print("number of students in",stream,"is:",count)
		else:
			print("EXIST")

menu()
menu()	