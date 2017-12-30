"" This Program checks the version of python that you're using """

import sys
if(sys.version_info[0] < 3):
    print ("This is Python version 2.X")
else:
    print ("This is Python version 3.X")
