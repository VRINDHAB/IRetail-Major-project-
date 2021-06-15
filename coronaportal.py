l=[]
d={}

def menu():
	global l,d
	print("..............................................")
	print("CORONA PORTAL ")
	print(".......................................")
	print("1. REGISTRATION")
	print("2. Mark Negetive")
	print("3. Current number of positive patients : ")
	print("4.Search")
	print("Back")
	print("..............................................")
	n=int(input('enter your choice : '))
	print("..............................................")

def patients():
	global l,d
	p=int(input('enter limit:'))
	for i in range(p):
		
		print("..............................................")
		print("Enter details of corona patients")
		print("..............................................")
		rollno=int(input('enter registration number : '))
		name=input('enter patient name : ')
		age=int(input('enter patient age : '))
		mob=int(input('enter mobile number : '))
		address=input('enter address : ')
		panchyat=input('Panchayat/Corporation : ')
		status=input('Currently positive/negetive : ')
		print("..............................................")
		d={"rollno":rollno,"name":name,"age":age,"Mobile":mob,"Address":address,"Panchayat/Corporation":panchayat,"status":status}
		l.append(d)
	print(l)


def mark_negetive():

	global l,d
	u=int(input('enter registration number of patients to mark negative : '))
	for i in l:
		if(i["rollno"]==u):
			i["status"]="negetive"
	print(l)


def currently_positive():

	global l,d
	c=0
	for i in l:
		if(i["status"]=="positive"):
			c=c+1
	print("currently positive",c)

def panchayat():
	global l,d
	m=0
	x=0
	for i in l:
		if(i["status"]=="positive"):
			if(i["panchayat"]=="thiruvanathapuram"):
				m=m+1
			else:
				x=x+1
	
	print(" Thiruvanathapuram corporation positive cases : ",m)
	print("Panchayat positive cases ",x)

def main_menu():
	n=0
	global l,d
	while(n!=5):
		n=menu()
		if(n==1):
			patients()
		elif(n==2):
			mark_negative()
		elif(n==3):
			currently_positive()
		elif(n==3):
			panchayat()
		else:
			print("Exit")
		
main_menu()
	