a=int(input('enter n: '))
for i in range(a):
	for k in range(i):
		print("",end=" ")
	for j in range(a-i,1,-1):
		print("1",end="")
	print()
