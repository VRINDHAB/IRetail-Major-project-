a=int(input('enter a ; '))
for i in range(a):
	for k in range(i):
		print(" ",end="")
	for j in range(i+1,a+a-i):
		print(j,end="")

	print()
