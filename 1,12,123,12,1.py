a=int(input('enter n: '))
for i in range(a):
	for k in range(a-i,1,-1):
		print(" ",end=" ")
	for j in range(1,i+2):
		print(j,end=" ")
	print()
for p in range(a):
	for r in range(-1,p):
		print(" ",end=" ")
	for q in range(1,a-p):
		print(q,end=" ")
	print()

