
import sys

if(sys.version_info[0] < 3):
    print("This program is written with Python 3.x")
    print("Run \'Python3 filename.py\' to propperly run the program")
    sys.exit(1)

else:
    # Do work here

    def main():
        import tkinter as tk

        root = tk.Tk()

        tk.Label(root, 
                text="Red Text in Times Font",
                fg = "red",
                font = "Times").pack()

        tk.Label(root, 
                text="Green Text in Helvetica Font",
                fg = "light green",
                bg = "dark green",
                font = "Helvetica 16 bold italic").pack()

        tk.Label(root, 
                text="Blue Text in Verdana bold",
                fg = "blue",
                bg = "yellow",
                font = "Verdana 10 bold").pack()

        root.mainloop()
        pass

    if __name__ == '__main__':
        sys.exit(main())
