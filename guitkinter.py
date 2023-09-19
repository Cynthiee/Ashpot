import tkinter 

# print(tkinter.TkVersion)  checks the version of tkinter
root = tkinter.Tk()
root.title("title page")

title_label = tkinter.Label(root, text="We are Learning Tkinter.")
insert = tkinter.Entry(root)
btn = tkinter.Button(root, text="Submit")

title_label.pack(pady=45)
insert.pack()
btn.pack(pady=15)

root.mainloop()

# List of All Tkinter widgets
# 1. Frame
# 2. Button
# 3. Entry
# 4. Radio button
# 5. Label
# 6. Menu
# 7. CommonBox
# 8. ListBox
# 9. Menu button
# 10. Canvas
# 11. Scale
# 12. Scrollbar
# 13. Toplevel