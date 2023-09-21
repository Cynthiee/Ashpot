import tkinter as t

def NewWindow():
    window = t.Toplevel()
    window.geometry('150x150')
    newlabel = t.Label(window, text = "Settings Window")
    newlabel.pack()
 
 
root = t.Tk()
root.geometry('200x200')
 
myframe = t.Frame(root)
myframe.pack()
 
mybutton = t.Button(myframe, text = "Settings", command = NewWindow)
mybutton.pack(pady = 10)
 
root.mainloop()