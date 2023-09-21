import tkinter as t

root = t.Tk()
root.geometry("500x350")
frame = t.Frame(root)
frame.pack()
 
MenuBttn = t.Menubutton(frame, text="Favourite food", relief="raised")
 
Var1 = t.IntVar()
Var2 = t.IntVar()
Var3 = t.IntVar()
 
Menu1 = t.Menu(MenuBttn, tearoff = 0)
 
Menu1.add_checkbutton(label = "Pizza", variable = Var1)
Menu1.add_checkbutton(label = "Cheese Burger", variable = Var2)
Menu1.add_checkbutton(label = "Salad", variable = Var3)
 
MenuBttn["menu"] = Menu1
 
MenuBttn.pack()
root.mainloop()
