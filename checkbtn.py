import tkinter as t

root = t.Tk()
root.geometry("200x150")

frame = t.Frame(root)
frame.pack()

var1 = t.IntVar()
var2 = t.IntVar()

chkbtn = t.Checkbutton(frame, width=15, variable=var1)
chkbtn.pack(padx=5, pady=5)

chkbtn2 = t.Checkbutton(frame, width=15, variable=var2)
chkbtn2.pack(padx=5, pady=5)

root.title("CheckButton")
root.mainloop()