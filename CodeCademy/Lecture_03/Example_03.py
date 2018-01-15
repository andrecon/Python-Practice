
import sys

if(sys.version_info[0] < 3):
    print("This program is written with Python 3.x")
    print("Run \'Python3 filename.py\' to propperly run the program")
    sys.exit(1)

else:
    # Do work here
    print("This program teaches you how if,elif and else case statements work. Checke it out!")

    def main():
        answer = "Is it right?"
        def the_flying_circus():
            if not(33 == 33) and (4*4-2) >= 13:
                return False
            elif answer == "Is it right?" or not(10 > 3):
                return True
            else:
                return False

        pass

    if __name__ == '__main__':
        sys.exit(main())
