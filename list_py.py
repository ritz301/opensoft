""" Prints all the python file names recursively in the directory where script is run
To use it simply run this in the desired location:
python list_py.py  """

import os
from os import listdir
from os.path import join, isdir

def printlist(mypath):
	pyfiles = [f for f in listdir(mypath) if f.endswith('.py')]
	for file in pyfiles:
		if not file.startswith('test_'):
			print file
	dirfiles = [f for f in listdir(mypath) if os.path.isdir(join(mypath, f))]
	if len(dirfiles)==0:
		return
	else:
		for dir in dirfiles:
			printlist(join(mypath, dir))

if __name__=="__main__":
	mypath = os.getcwd()
	printlist(mypath)

# os.path.dirname(os.path.abspath(__file__)) gives script location