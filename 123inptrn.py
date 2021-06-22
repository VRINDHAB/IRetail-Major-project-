a=int(input("enter v1 : "))
for i in range(a):
	for k in range(1,a-i):
		print(" ",end=" ")
	for j in range(i+1,0,-1):
		
		print(j,end=" ")
	print()