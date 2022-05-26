from tkinter import *
from PIL import ImageTk,Image

root = Tk()


def hello():
    print("You pressed button")
root.geometry("560x350")
root.title("Indus Attendance System")
image = Image.open("Images/indus.jpeg")
resized_image= image.resize((300,205), Image.ANTIALIAS)
photo= ImageTk.PhotoImage(resized_image)

f1=Frame(root,bg="yellow")

b1 = Button(f1,fg="red",text="Press it",command=hello,borderwidth=2, relief=SUNKEN)
b2 = Button(f1,fg="red",text="Close window",command=root.destroy,borderwidth=2, relief=SUNKEN)
b1.pack()
b2.pack()

vlabel = Label(root,image=photo)

t = Label(text="Indus Face Recognition Attendance System",font="comicsansms 19 bold")
t.pack()
vlabel.pack()
f1.pack()

root.mainloop()