a=int(input('enter n: '))
for i in range(a):
	for k in range(0,i):
		print("",end=" ")
	for j in range(a-i,0,-1):
		print(j,end=" ")
	for p in range(2,a-i+1):
		print(p,end=" ")
	print()




