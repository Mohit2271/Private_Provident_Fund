from tkinter import *
import Menu

def open_main_menu():
    root = Tk()
    obj = Menu.Menu(root)
    obj.create_widgets(root)
    root.mainloop()

open_main_menu()
