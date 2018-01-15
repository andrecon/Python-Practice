
import sys

if(sys.version_info[0] < 3):
    print("This program is written with Python 3.x")
    print("Run \'Python3 filename.py\' to propperly run the program")
    sys.exit(1)

else:
    # Do work here

    counter = 0 

    def main():
        import tkinter as tk


        def counter_label(label):
            def count():
                global counter
                counter = counter + 1
                label.config(text=str(counter))
                label.after(1000, count)
            count()


        root = tk.Tk()
        root.title("Counting Seconds")
        label = tk.Label(root, fg="green")
        label.pack()
        counter_label(label)
        button = tk.Button(root, text='Stop', width=25, command=root.destroy)
        button.pack()
        root.mainloop()

        pass

    if __name__ == '__main__':
        sys.exit(main())
