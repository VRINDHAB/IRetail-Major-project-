n=[]
def read():
	global n
	a=int(input('enter limit : '))
	
	for i in range(a):
		b=int(input('enter values : '))
		n.append(b)
	
read()

def menu():
	print('1. Sum')
	print('2. Sub')
	print('3. mult')
	print('4. Greatest')
	print('5. Smallest')
	print('6. Search a value ')
	print('7. Replace a value ')
	print('8. Prime')
	print('9. Armstrong')
	print('10. Perfect')
	print('11. Delete a value')
	print('12. Exit')
	a=int(input('enter choice: '))
	return(a)
	print(n)
def sum():
	global n
	a=int(input('enter a: '))
	b=int(input('enter b: '))
	s=0
	s=a+b
	print('Sum=',s)
	
	
def sub():
	global n
	a=int(input('enter a: '))
	b=int(input('enter b: '))
	s=0
	s=a-b
	print('Sub=',s)
def mul():
	global n
	a=int(input('enter a: '))
	b=int(input('enter b: '))
	m=0
	m=a*b
	print('product=',m)
def grtr():
	global n
	t=0
	for i in n:
		if(i>t):
			t=i	
	print(t,'is greater')

def small():
	global n
	s=n[0]
	for i in n:
		if(i<s):
			s=i
	print(s,'is smallest')

def prin():
	global n
	print(n)
prin()
def srch():
	global n
	b=input('enter string to be srched : ')
	flag=0
	for i in n:
		
		if(i==b):
			flag=flag+1
	if(flag!=0):
		print(' string/value is found')
		print(flag)
	else:
		print('not found')

def replace():
	global n
	print('initial list: ',n)
	c=int(input('enter the elment to insert: '))
	b=int(input('srch elmnt: '))
	j=0
	for i in n:
		if(i==b):
			n[j]=c
		j+=1	
	print('replaced list : ',n)

def prime(a):
	flag=0
	for i in range (1,a):
		if(a%i==0):
			flag=flag+1
			
	if(flag==1):
		print(a,'is prime')
	else:
		print(a,'not prime')
def armstrong():
	num = int(input("Enter a number to check : "))  
	sum = 0  
	temp = num  
  	for i in range(1,a):
		while temp > 0:  
   			digit = temp % 10  
  			sum += digit ** 3  
   			temp //= 10  
  
		if num == sum:  
  			 print(num,"is an Armstrong number")  
		else:  
 	  		print(num,"is not an Armstrong number") 

def perfect(a):
	flag=0
	for i in range(1,a):
		
		if(a%i==0):
			flag=flag+i
			
	if(flag==a):
		print(a,"is perfect")
	else:
		print(a,"is not perfect")



def home():
	a=0
	while(a!=5):
		a=menu()
		if(a==1):
			sum()
		elif(a==2):
			sub()
		elif(a==3):
			mul()
		elif(a==4):
			grtr()
		elif(a==5):
			small()
		elif(a==6):
			srch()
		elif(a==7):
			replace()
		elif(a==8):
			for i in n:
				prime(i)
		elif(a==9):
			for i in n:
				armstrong(i)
		elif(a==10):
			for i in n:
				perfect(i)
			
			
		else:
			print('enter a valid option')
home()


	