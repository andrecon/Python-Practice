
# The datetime Library

import sys
from datetime import datetime

if(sys.version_info[0] < 3):
    print("This program is written with Python 3.x")
    print("Run \'Python3 Example_01.py\' to propperly run the program")
    sys.exit(1)

else:
    # Getting the Current Date and Time
    now = datetime.now()
    print ("FULL INFORMATION:", now)

    current_year = now.year
    current_month = now.month
    current_day = now.day

    print ("CURRENT YEAR:", current_year, "\nCURRENT MONTH:", current_month, "\nCURRENT DAY:", current_day)


    print("PRINTING INFORMATION IN mm/dd/yyyy:", '%s/%s/%s' % (now.month, now.day, now.year))
    print("PRINTING TIME IN hh:mm:ss :", '%s:%s:%s' % (now.hour, now.minute, "%.f" % now.second))

    print("PRINTING EVERYTHING IN ONE LINE:", '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, "%.f" % now.second))
