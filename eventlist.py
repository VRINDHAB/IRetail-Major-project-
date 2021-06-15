def home():
	print("------------")
	print("1.addition")
	print("2.substraction")
	print("3.multiplication")
	print("4.greatest")
	print("5.smallest")
	print("6.sreach")
	print("7.sreach and replace")
	print("8.prime")
	print("9.prefect")
	print("10.amstrong")
	print("------------")
	x=int(input("enter the choice"))
	return(x)
def list():
	i=0
	while i!=11:
		i=home()
		if i==1:
			add()
		elif i==2:
			sub()
		elif i==3:
			multi()
		elif i==4:
			big()
		elif i==5:
			small()
		elif i==6:
			srch()
		elif i==7:
			srchre()
		elif i==8:
			
			n=[]
			a=int(input("eneter the  limit"))
			for i in range(a):
				c=int(input("enter the int values"))
				n.append(c)
			print(n)
			for i in n:
				prime(i)
		elif i==9:
			n=[]
			a=int(input("eneter the  limit"))
			for i in range(a):
				c=int(input("enter the int values"))
				n.append(c)
			for i in n:
				prefect(i)
		elif i==10:
			arm()
		elif i==11:
			print("---exist---")
		else:
			print("invalid choice")
def add():
	n=[]
	a=int(input("eneter the  limit"))
	for i in range(a):
		c=int(input("enter the int values"))
		n.append(c)
	print(n)
	s=0
	for i in n:
		s=s+i
	print(s)
def sub():
	n=[]
	a=int(input("eneter the  limit"))
	for i in range(a):
		c=int(input("enter the int values"))
		n.append(c)
	print(n)
	s=n[0]
	for i in n:
		s=s-i+1
	print(s)
def multi():
	n=[]
	a=int(input("eneter the  limit"))
	for i in range(a):
		c=int(input("enter the int values"))
		n.append(c)
	print(n)
	s=1
	for i in n:
		s=s*i
	print(s)
def big():
	n=[]
	a=int(input("eneter the  limit"))
	for i in range(a):
		c=int(input("enter the int values"))
		n.append(c)
	b=0
	for i in n:
		if(b<i):
			b=i
	print("bigg",b)	
def small():
	n=[]
	a=int(input("eneter the  limit"))
	for i in range(a):
		c=int(input("enter the int values"))
		n.append(c)
	s=n[0]
	for i in n:
		if(s>i):
			s=i
	print(s)
def srch():
	n=[]
	a=int(input("eneter the  limit"))
	for i in range(a):
		c=int(input("enter the int values"))
		n.append(c)
	print(n)
	b=int(input("enter the values to be srched"))
	flag=0
	for i in n:
		
		if(i==b):
			flag+=1
	if(flag!=0):
		print("count",flag)
		print("found=",b)
	else:
		print("note found")
	
def srchre():
	n=[]
	a=int(input("eneter the  limit"))
	for i in range(a):
		c=int(input("enter the int values"))
		n.append(c)
	print(n)
	x=int(input("enter scrh elemt to change"))
	y=int(input("enter the value to replave"))
	j=0
	for i in n:
		if(i==x):
			n[j]=y
		j+=1
	print(n)	
def prime(a):
	
	flag=0
	for i in range(1,a):
		if(a%i==0):
			flag+=1
	if(flag==1):
		print("prime")
	else:
		print("no prime")
def prefect(a):
	temp=a
	flag=0
	for i in range(1,a):
		if(a%i==0):
			flag=flag+i
	if(temp==flag):
		print("prefect")
	else:
		print("not prefect")
	
list()
