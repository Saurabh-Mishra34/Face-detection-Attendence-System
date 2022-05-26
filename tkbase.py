
import tkinter as tk
r = tk.Tk()

def hello():
   print("you pressed the button")

r.title('Counting Seconds')
button = tk.Button(r, text='Mark Attendence', width=25, command=hello)
button.pack()
r.mainloop()