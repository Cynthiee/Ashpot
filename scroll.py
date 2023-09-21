import tkinter as t

root = t.Tk() 
root.geometry("200x250") 
    
mylabel = t.Label(root, text ='Scrollbars', font = "30")  
mylabel.pack() 
 
myscroll = t.Scrollbar(root) 
myscroll.pack(side="right", fill="y") 
 
mylist = t.Listbox(root, yscrollcommand = myscroll.set )  
for line in range(1, 100): 
    mylist.insert("end", "Number " + str(line)) 
mylist.pack(side = "left", fill = "both" )    
 
myscroll.config(command = mylist.yview) 
    
root.title("Scroll")
root.mainloop() 