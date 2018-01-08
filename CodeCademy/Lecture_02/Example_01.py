import sys
if(sys.version_info[0] < 3):
    print("This program is written with Python 3.x")
    print("Run \'Python3 Example_01.py\' to propperly run the program")
    sys.exit(1)
else:
    # In this example we learn on manipulating strings effectively

    name = "Paul"
    age = "20"
    food = "hot dog"


    # Escaping characters

    statement = 'This isn\'t flying, this is falling with style!'

    print(name, "Who is", age, "Stateted.... ", statement)


    print("\nIn this example we learn access the string's index")
    print("---------------------------")

    n = "Ryan"[0]
    b = "tired"[1]
    i = "might"[2]
    k = "straight"[6]
    c = "cats"[2]
    print(n,b,i,k,c)

    print("---------------------------\n")

    print("String methods")
    print("---------------------------")

    parrot = "Norwegian Blue"

    print("USING len()")
    print (len(parrot))

    print("USING lower()")
    print ("From:", parrot, "To:", parrot.lower())

    print("USING upper()")
    print ("From:", parrot, "To:", parrot.upper())

    print("USING str()")
    print (str(37746748848499), "Is a string not an integer")

    print("---------------------------\n")
