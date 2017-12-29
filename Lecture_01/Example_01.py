# WORKS FOR PYTHON 2.X AND 3.X

#This Example shows you how small Functions work 
#To do that initialize it with "def" to "Define" it. Indentation is crucial...


def Hello(name="everybody"):
    """ Greets a person """
    print("Hello " + name + "!")


def square(x):
    print(x*x)


print(square(4))

Hello("Peter")
Hello()
