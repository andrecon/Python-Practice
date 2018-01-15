
import sys

if(sys.version_info[0] < 3):
    print("This program is written with Python 3.x")
    print("Run \'Python3 filename.py\' to propperly run the program")
    sys.exit(1)

else:
    # Do work here

    def main():
        import tkinter as tk

        master = tk.Tk()
        whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
        msg = tk.Message(master, text = whatever_you_do)
        msg.config(bg='lightgreen', font=('times', 24, 'italic'))
        msg.pack()
        tk.mainloop()
        pass

    if __name__ == '__main__':
        sys.exit(main())
