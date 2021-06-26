a=['1','2','3']
def globa():
	
	
	a=12
	print(a)
#globa()
def appnd():
	global a
	a=['ab','abc','abcd']
	a.append('abc')
	print(a)
appnd()
print(a)