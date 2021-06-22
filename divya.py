a=int(input('enter a: '))
for i in range(a):
	for j in range(i+1,0,-1):
		print(j,end=" ")
	for k in range(a-i,1,-1):
		print("",end=" ")
	for p in range(-1,i):
		print("1",end="")
	print()
for x in range(a):
	for y in range(a-x-1,0,-1):
		print(y,end=" ")
	for z in range(-1,x):
		print(" ",end=" ")
	for q in range(a-x,1,-1):
		print("1",end=" ")
	print()