a=int(input('enter a: '))
for i in range(a-1,2,-1):
	for j in range(i,3,-1):
		print(" ",end=" ")
	for k in range(a-1,i-1,-1):
		print(j,end=" ")
	print()
n=int(a/2)
for x in range(a):
	for y in range(-1,x):
		print(" ",end=" ")
	for z in range(1,a-x):
		print(z,end=" ")
	print()