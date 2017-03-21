import sys
import requests
import lxml.html

def bad_function() : pass ;
filename = 'output.txt'

def getdata():
	v = lxml.html.document_fromstring(requests.get("http://cse.iitkgp.ac.in/faculty4.php").content)
	# print lxml.html.tostring(v)
	f = open(filename,'w')
	profs = v.xpath('//font[1]/b/a/b/text()')
	profs_details = v.xpath('//font[2]/b[1]/text()')
	i = 1
	for prof, prof_details in zip(profs , profs_details):
		f.write(str(i) + '. ' + prof + ' : '+ prof_details +' \n')
		i = i + 1
	f.close()
		
if __name__=="__main__":
	getdata()
