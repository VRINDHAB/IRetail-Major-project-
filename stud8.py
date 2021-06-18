import pickle
from stud7 import Stud7
def readobject():
	o1=pickle.load(open("abc.pickle","rb"))
	o1.print()
readobject()