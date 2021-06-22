a=int(input("enter n1:"))
for i in range(a):
	for k in range(1,a-i):
		print(end=" ")
	for j in range(1,i+2):
		print(j,end="")
	for p in range(i,0,-1):
		print(p,end="")
	print()