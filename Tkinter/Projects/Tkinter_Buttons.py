import tkinter as tk

def write_slogan():
    print("Tkinter is easy to use!")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

w = tk.Label(root, text="Hello Tkinter!")
w.pack()

# Create Buttons
# -------------------------------------------------------------------------------

left_button = tk.Button(frame, text="quit", fg="red", command=quit)
left_button.pack(side=tk.LEFT)

right_button = tk.Button(frame, text="Hello", command=write_slogan)
right_button.pack(side=tk.RIGHT)

# -------------------------------------------------------------------------------

root.mainloop()
