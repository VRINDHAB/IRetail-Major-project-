a=int(input('enter n: '))
for i in range(a):
	for k in range(a-i,0,-1):
		print(" ",end=" ")
	for j in range(i):
		print("1",end=" ")
	
	print()
for p in range(a):
	for q in range(p+1):
		print(" ",end=" ")
	for r in range(a-p,1,-1):
		
		print(1,end=" ")
	print()
