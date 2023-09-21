import tkinter as t

 
root = t.Tk()
root.geometry("200x200")
frame = t.Frame(root)
frame.pack()
 
Scala = t.Scale(frame, from_=0, to=10)
Scala.pack(padx=5, pady=5)
 
Scala2 = t.Scale(frame, from_=0, to=10, orient="horizontal")
Scala2.pack(padx=5, pady=5)
 
root.title("Scale") 
root.mainloop()