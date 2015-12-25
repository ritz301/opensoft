""" Using wikiminer API to extract wikipedia articles from an input text """

import requests
import sys
from lxml import etree

def main():
	sys.stdout.write("Enter your string:\n")
	input = sys.stdin.readline()
	r = requests.get("http://wikipedia-miner.cms.waikato.ac.nz/services/wikify", params={"source":input})
	content = etree.XML(r.content);
	count = 0
	for child in content[2]:
		count = count + 1
	sys.stdout.write("\nThe number of detected wikipedia articles found in your text is {}.\n".format(count))
	count = 1
	for child in content[2]:
		sys.stdout.write("{}\t".format(count))
		a = child.items()
		sys.stdout.write("{}\t\t".format(list(a[1])[1]))
		sys.stdout.write("http://en.wikipedia.org/?curid={}\n".format(list(a[0])[1]))
		count = count + 1

if __name__ == "__main__":
    main()

""" Refer below link for more:
    http://lxml.de/tutorial.html """