import sys
# if there are no conflicting packages in the default Python Libs =>
sys.path.append("/usr/home/username/pdfminer")

from pdfminer import *
from slate import *
from test_slate import *

x = pytest_funcarg__doc()
print "done"