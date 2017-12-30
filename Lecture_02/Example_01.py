import sys
if(sys.version_info[0] < 3):
    print("This program is written with Python 3.x")
    print("Run \'Python3 Example_01.py\' to propperly run the program")
    sys.exit(1)
else:
    # Example for Strings

    name = "Paul"
    age = "20"
    food = "hot dog"


    # Escaping characters

    statement = 'This isn\'t flying, this is falling with style!'

    print(name, "Who is", age, "Stateted.... ", statement)
