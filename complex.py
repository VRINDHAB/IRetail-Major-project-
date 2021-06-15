n=int(input("enter a limit:"))
for k in range(1,n+1):
	if(k%2==0):
		print(k,"...even",end="")
	else:
		print(k,"...odd",end="")
	flag=0
	
	if(n%k==0):
		flag+=1
	if(flag==1):
		print("...","prime",end="")
	else:
		print("...","no prime",end="")
	flag1=0
	for j in range(1,k):
	if(k%j==0):
		flag1=flag1+j
	if(j==flag1):
		print("...","prefect",end="")
	else:
		print("...","not prefect",end="")
	
	print()