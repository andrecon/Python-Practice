
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
        logo = tk.PhotoImage(file="Tau_Kappa_Epsilon__TKE__TEKES-logo-8B93BCB3A4-seeklogo.com.gif")

        explanation = """At present, only GIF and PPM/PGM
        formats are supported, but an interface 
        exists to allow additional image file
        formats to be added easily."""

        """w = tk.Label(root, 
                compound = tk.CENTER,
                text=explanation, 
                image=logo).pack(side="right")
        """

        w = tk.Label(root, 
                justify=tk.CENTER,
                compound = tk.BOTTOM,
                padx = 10, 
                text=explanation, 
                image=logo).pack(side="left")


        root.mainloop()
        pass


    if __name__ == '__main__':
        sys.exit(main())
