from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb

root = Tk()
root.title("Hiding Secret Text Message")
root.geometry("700x600+150+180")
root.resizable(False, False)
root.configure(bg="black")

def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title="Select File Image",
                                          filetype=(("PNG file", "*.png"),
                                                    ("JPG file", "*.jpg"),
                                                    ("All file", "*.*")))
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img, width=250, height=250)
    lbl.image = img

def Hide():
    global secret
    message = text1.get(1.0, END)
    secret = lsb.hide(filename, message)

def Show():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_message)

def save():
    secret.save("hidden.png")


# Icon
image_icon = PhotoImage(file="download.png")
root.iconphoto(False, image_icon)

# Logo
logo = PhotoImage(file="CAPTURE.png")
Label(root, image=logo, bg="black").place(x=240, y=30)
Label(root, text="CYBER SCIENCE", fg="#20C20E", font="arial 25 bold", bg="black").place(x=210, y=0)

# First frame
f = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
f.place(x=10, y=180)
lbl = Label(f, bg="black")
lbl.place(x=40, y=40)

# Second frame
Frame2 = Frame(root, bd=3, width=340, height=280, relief=GROOVE)
Frame2.place(x=350, y=180)

text1 = Text(Frame2, font=("poppins", 20, "bold"), bg="#4F4F4F", fg="white", relief=GROOVE)
text1.place(x=0, y=0, width=320, height=280)

scrollbar1 = Scrollbar(Frame2)
scrollbar1.place(x=320, y=0, height=300)
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Third frame
Frame3 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
Frame3.place(x=10, y=480)

Button(Frame3, text="Open Image", width=10, height=2, font="arial 14 bold", command=showimage).place(x=30, y=30)
Button(Frame3, text="Save Image", width=10, height=2, font="arial 14 bold", command=save).place(x=180, y=30)
Label(Frame3, text="Picture, Image File", bg="green").place(x=110, y=5)

# Fourth frame
Frame4 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
Frame4.place(x=360, y=480)

Button(Frame4, text="Hide Data", width=10, height=2, font="arial 14 bold", command=Hide).place(x=30, y=30)
Button(Frame4, text="Show Data", width=10, height=2, font="arial 14 bold", command=Show).place(x=180, y=30)
Label(Frame4, text="Picture, Image File", bg="green").place(x=110, y=5)

root.mainloop()
