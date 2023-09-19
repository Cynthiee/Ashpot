import tkinter

def set():
    print("Hello World")

root =tkinter.Tk()
root.geometry("200x150")

frame = tkinter.Frame(root)
frame.pack()
btn = tkinter.Button(frame, text="Button", command=set, 
                     fg="red", font="Verdana 14 underline",
                     bd=2, bg="light blue", relief="groove")
btn.pack(pady=15)


root.title("Button")
root.mainloop()