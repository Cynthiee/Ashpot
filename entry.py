import tkinter as tk

root = tk.Tk()
root.geometry("200x150")

frame = tk.Frame(root)
frame.pack()

my_entry = tk.Entry(frame, width=20)
my_entry.insert(0, 'Username: ')
my_entry.pack(padx=10, pady=10)

my_entry2 = tk.Entry(frame, width=15)
my_entry2.insert(0, 'password')
my_entry2.pack(padx=10, pady=10)

root.title("Entry")
root.mainloop()