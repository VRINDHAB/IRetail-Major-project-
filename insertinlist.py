a=[1,2,3,4]
print('initial list: ',a)
def srch():
	global a
	b=int(input('enter search element: '))
	c=int(input('enter the elment to insert: '))
	j=0
	for i in a:
		if(i==b):
			a[j]=c
		j+=1	
	print('replaced list : ',a)
srch()