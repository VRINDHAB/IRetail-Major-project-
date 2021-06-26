n=[]
def read():
	global n
	a=int(input('enter limit : '))
	
	for i in range(a):
		b=int(input('enter values : '))
		n.append(b)
	print(n)
read()
def grtr():
	global n
	t=0
	for i in n:
		if(i>t):
			t=i	
	print(t,'is greater')
grtr()
def small():
	global n
	s=n[0]
	for i in n:
		if(i<s):
			s=i
	print(s,'is smallest')
small()
		