
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

        v = tk.IntVar()

        tk.Label(root, 
                text="""Choose a 
                programming language:""",
                justify = tk.LEFT,
                padx = 20).pack()

        tk.Radiobutton(root, 
                text="Python",
                padx = 20, 
                variable=v, 
                value=1).pack(anchor=tk.W)

        tk.Radiobutton(root, 
                text="Perl",
                padx = 20, 
                variable=v, 
                value=2).pack(anchor=tk.W)

        root.mainloop()
        pass

    if __name__ == '__main__':
        sys.exit(main())
