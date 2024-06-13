import tkinter as tk
from tkinter import messagebox

def download_video():
    
    messagebox.showinfo("Download", "Video downloaded!")

root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("400x400")
root.configure(bg="lightpink")

# background_image = tk.PhotoImage(file="lappy.jpg")
# body = tk.Label(root, image=background_image, compound="center")

title_label = tk.Label(root, text="YouTube Downloader", font=("Arial", 18))
title_label.pack(pady=20)

url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.pack(pady=5)
url_entry = tk.Entry(root, width=40)
url_entry.pack(pady=10)

download_button = tk.Button(root, text="Download Video", bg="pink", command=download_video)
download_button.pack(pady=30)

root.title("YouTube Downloader")
root.mainloop()