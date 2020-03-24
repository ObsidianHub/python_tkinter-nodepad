from tkinter import *

root = Tk()
root.geometry('600x400+1000+300')

main_menu = Menu(root)
root.config(menu=main_menu)

# main_menu.add_command(label="File")
# main_menu.add_command(label="About")

# File
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Открыть")
file_menu.add_command(label="Сохранить")
file_menu.add_separator()
file_menu.add_command(label="Выход")
main_menu.add_cascade(label="Файл", menu=file_menu)

# About
help_menu = Menu(main_menu, tearoff=0)
help_menu_sub = Menu(help_menu, tearoff=0)

help_menu_sub.add_command(label="Онлайн")
help_menu_sub.add_command(label="Оффлайн")

help_menu.add_cascade(label="Помощь", menu=help_menu_sub)
help_menu.add_command(label="О программе")

main_menu.add_cascade(label="Справка", menu=help_menu)

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

root.mainloop()