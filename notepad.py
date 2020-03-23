from tkinter import *

root = Tk()
root.geometry('600x400+1000+300')

main_menu = Menu(root)
root.config(menu=main_menu)

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

root.mainloop()