import pdfminer
from slate import *

with open('test.pdf') as f:
	doc = slate.PDF(f)
	doc
print "done"