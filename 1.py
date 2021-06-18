def sampleprint():
	print("Hello World")
#sampleprint()

def sum():
	a=int(input('enter a: '))
	b=int(input('enter b: '))
	c=a+b
	
	print(c)
	
#sum()
def sub():
	a=int(input('enter a: '))
	b=int(input('enter b: '))
	c=a-b
	print(c)
#sub()
def sumwitharg(a,b):
	s=a+b
	print(s,'is sum of a and b')
#sumwitharg(4,5)
def sumwithreturn(a,b):
	s=a+b
	return(s)
z=sumwithreturn(3,4)
print(z)
#sum()
#sub()
#sumwitharg(a,b)
#sumwithreturn(a,b)