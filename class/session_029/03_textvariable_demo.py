from tkinter import *
from tkinter import ttk
import time

msg = None
i = -1

L =["Hello-1","Hello-10","Hello-100"]

def change_button_handler():
    global i
    i= (i+1) % len(L)
    msg.set(L[i])
    s = msg.get()
    print(s)
    
def main():
    global msg
    root_window = Tk()
    root_window.title("Feet to meter conversion")

    msg = StringVar()
    Lb = ttk.Label(root_window)
    Lb.configure(textvariable = msg)
    msg.set("start")
    Lb.grid(row=20,column = 10)

    B = Button(root_window)
    B.configure(text = " change ",padx= 3,pady=3,command=change_button_handler)
    B.grid(row=30,column = 10)

    root_window.mainloop()

main()