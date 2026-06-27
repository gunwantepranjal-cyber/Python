from tkinter import *
from tkinter import ttk

def button_handler():
    print("hello")

def main():
    root_window = Tk()
    root_window.title("feet to meter conversion")

    master_frame = ttk.Frame(root_window , padding = "3 3 12 12")
    master_frame.grid(column = 0 , row = 0, sticky= (N,W,E,S))

    root_window.columnconfigure(0,weight = 10)
    root_window.rowconfigure(0,weight = 10)

    B = ttk.Button(master_frame)
    B.configure(text = "Hello" , command = button_handler)
    B.grid(row = 1,column = 0,padx = 99, pady =65 )
    root_window.mainloop()

main()