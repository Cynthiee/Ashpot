import tkinter

root = tkinter.Tk()
root.geometry("200x150")
frame = tkinter.Frame(root)
frame.pack()

leftframe = tkinter.Frame(root)
leftframe.pack(side="LEFT")

rightframe =tkinter.Frame(root)
rightframe.pack(side="RIGHT")

label = tkinter.Label(frame, text="Hello world")
label.pack()

btn1 = tkinter.Button(leftframe, text="Button1")
btn1.pack(padx=3, pady=3)
btn2 = tkinter.Button(leftframe, text="Button2")
btn2.pack(padx=3, pady=3)
btn3 = tkinter.Button(leftframe, text="Button3")
btn3.pack(padx=3, pady=3)



root.title("Frame")
root.mainloop()