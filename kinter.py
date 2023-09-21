from tkinter import *

root = Tk()
root.geometry("500x350")
frame = Frame(root)
frame.pack()
 
MenuBttn = Menubutton(frame, text="Favourite food", relief="raised")
 
Var1 = IntVar()
Var2 = IntVar()
Var3 = IntVar()
 
Menu1 = Menu(MenuBttn, tearoff = 0)
 
Menu1.add_checkbutton(label = "Friedrice", variable = Var1)
Menu1.add_checkbutton(label = "Coconut and bread", variable = Var2)
Menu1.add_checkbutton(label = "Egusi soup", variable = Var3)
 
MenuBttn["menu"] = Menu1
 
MenuBttn.pack()
root.mainloop()