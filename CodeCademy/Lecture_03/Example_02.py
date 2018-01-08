import sys

if(sys.version_info[0] < 3):
    print("This program is written with Python 3.x")
    print("Run \'Python3 Example_02.py\' to propperly run the program")                                                                                                                    
    sys.exit(1)  

else:
    # Example for Comparison
    
    """ 1) Equal to (==)
        2) Not equal to (!=)
        3) Less than (<)
        4) Less than or equal to (<=)
        5) Greater than (>)
        6) Greater than or equal to (>=) """
    
    # Assign True or False as appropriate on the lines below!
    print("CCOMPARISON EXAMPLE... LOOK IN FILE \'Example_02.py\' TO SEE ALL WORK\n")

    # (20 - 10) > 15
    bool_one = False

    if(bool_one == False):
        answer = "False"
    else:
        answer = "True"

    print("(20 - 10) > 15 is", answer , "\n------------")

    # (10 + 17) == 3**16
    # Remember that ** can be read as 'to the power of'. 3**16 is about 43 million.
    bool_two = False

    if(bool_two == False):
        answer = "False"
    else:
        answer = "True"

    print("(10 + 17) == 3**16 is", answer, "\n------------")

    # 1**2 <= -1
    bool_three = False

    if(bool_three == False):
        answer = "False"
    else:
        answer = "True"

    print("1**2 <= -1 is", answer, "\n------------")

    # 40 * 4 >= -4
    bool_four = True

    if(bool_four == False):
        answer = "False"
    else:
        answer = "True"

    print("40 * 4 >= -4 is", answer, "\n------------")

    # 100 != 10**2
    bool_five = False

    if(bool_five == False):
        answer = "False"
    else:
        answer = "True"

    print("100 != 10**2 is", answer, "\n------------")

