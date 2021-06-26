n=[]

def stud1():
	s=[]
	a=input('Enter the name : ')
	s.append(a)
	b=int(input('Enter the age: '))
	s.append(b)
	c=input('Enter the address: ')
	s.append(c)
	return(s)
	print(s)
	

def read():
	global n
	a=int(input('Enter the limit: '))
	for i in range(a):
		v=stud1()
		n.append(v)
	print(n)
	
	

def srch():
	global n
	a=input('enter name to srch: ')
	b=int(input('enter age chmge: '))
	for i in n:
		
		if(i[0]==a):
			i[1]=b
	print(n)
		

read()
srch()
	
			

