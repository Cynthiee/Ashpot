import tkinter as t

root = t.Tk()
root.geometry("500x350")

frame = t.Frame(root)
frame.pack()

var1 = t.StringVar()

rbtn = t.Radiobutton(frame, text="Option 1", variable=var1, value=1)
rbtn.pack(padx=5, pady=5)

rbtn2 = t.Radiobutton(frame, text="Option 2", variable=var1, value=2)
rbtn2.pack(padx=5, pady=5)

root.title("RadioButton")
root.mainloop()