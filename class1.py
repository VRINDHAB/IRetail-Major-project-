class Demo:
	def __init__(self):
		self.a=12
	

o=Demo()
print(o.a)
o.a="ash"
print(o.a)

o1=Demo()
o1.a="anu"
print(o1.a)

o2=Demo()
o2.a=o.a+o1.a
print(o.a ,"+", o1.a," =", o2.a)


