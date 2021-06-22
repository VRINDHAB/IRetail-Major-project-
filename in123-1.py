n=int(input('enter n : '))
for i in range(1,n):
	for k in range(i):
		print(" ",end=" ")
	for j in range(n-i,0,-1):
		print(j,end=" ")
	print()
