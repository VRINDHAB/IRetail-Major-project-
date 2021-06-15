def home():
	print("_______________")
	print("1.addition")
	print("2.substraction")
	print("3.multiplictaion")
	print("4.division")
	print("5.home")
	print("6.exist")
	n=int(input("enter the choice"))
	return(n)

def c():
	i=0
	while i!=5:
		i=home()
		if(i==1):
			sum()
		elif(i==2):
			sub()
		elif(i==3):
			multi()
		elif(i==4):
			div()
		elif(i==5):
			
			print("x")
		else:
			print("enter valid option")
		
def sum():
	sum=0
	a=int(input("a"))
	b=int(input("b"))
	summ=a+b
	print(summ)
def sub():
	a=int(input("a"))
	b=int(input("b"))
	sub=a-b
	print(sub)
def multi():
	a=int(input("a"))
	b=int(input("b"))
	m=a*b
	print(m)
def div():
	a=int(input("a"))
	b=int(input("b"))
	d=a/b
	print(d)
c()
