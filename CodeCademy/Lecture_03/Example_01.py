import sys

if(sys.version_info[0] < 3):
    print("This program is written with Python 3.x")
    print("Run \'Python3 Example_01.py\' to propperly run the program")
    sys.exit(1)
else:
    """ Control flow gives us this ability to choose among outcomes based off what else is happening in the program. """

    def clinic():
        print("You've just entered the clinic!")
        print ("Do you take the door on the left or the right?")
	
	# This line takes users input and stores it into answer as a string variable.
        answer = input("Type left or right and hit 'Enter'.\nInput: ").lower()

        if answer == "left" or answer == "l":
            print("***This is the Verbal Abuse Room, you heap of parrot droppings!***")
        elif answer == "right" or answer == "r":
            print("***Of course this is the Argument Room, I've told you that already!***")
        else:
            print("You didn't pick left or right! Try again.\n")
            clinic()

    clinic()
