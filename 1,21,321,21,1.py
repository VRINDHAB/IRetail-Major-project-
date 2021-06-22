a=int(input('enter n: '))
for i in range(a):
	for k in range(i+1,0,-1):
		print(k,end=" ")
	print()
for p in range(a):
	for r in range(a-p-1,0,-1):
		print(r,end=" ")
	print()
