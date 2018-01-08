import sys

if(sys.version_info[0] < 3):
    print("This program is written with Python 3.x")
    print("Run \'Python3 Example_02.py\' to propperly run the program")
    sys.exit(1)                                              

else:

    print("String Concatenation")
    print("---------------------------")
    
    life = "Life "
    of = "Of "
    Bryan = "Bryan"
    print(life + of + Bryan)

    print("---------------------------\n")

    print("Explicit String Conversion")
    print("---------------------------")

    print("I have " + str(20) + " Burgers")

    print("---------------------------\n")

    print("String Formatting with %")
    print("---------------------------")

    string_1 = "Camelot"
    string_2 = "place"

    print ("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))

    print ("He %s that %s not ready for the %s that\'s going down %s" % ("said","he\'s","tournament", "tomorrow"))

    print("---------------------------\n")



