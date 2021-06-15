import datetime
l=[]

def reg_corona_postive_patient():
	global l
	x=int(input("eneter the limits :"))
	for i in range(x):
		n=input("enter the name :")
		a=int(input("enter the age :"))
		ph=int(input("enter the ph.no :"))
		d=input("enter the date:")
		po=int(input("enter the post office :"))
		ad=input("enter the adress :")
		pco=input("enter the pan/cor(../tvm) :")
		
		d={"name":n,"age":a,"phone":ph,"covid date":d,"post off":po,"adress":ad,"pan/cor":pco}
		d["poneg"]="positve"
		l.append(d)
	print(l)
def negative():
	global l
	x=input("enter the name of patient who is negative")
	for i in l:
		if(x==i["name"]):
			i["poneg"]="negative"
			print(i)
		
def count():
	global l
	count=0
	for i in l:
		if(i["poneg"]=="positive"):
			if(i["pco"]=="tvm"):
				count+=1
				print("postive cases in co",count)
			else:
				count+=1
				print("postive cases in pan",count)

reg_corona_postive_patient()
negative()
count()