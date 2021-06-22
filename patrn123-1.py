a=int(input('enter n: '))
for i in range(a):
	for k in range(i):
		print(" ",end=" ")
	for j in range(1,a-i):
		print(j,end=" ")
	print()