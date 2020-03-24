from tkinter import *

root = Tk()
root.geometry('1000x500+1000+300')

main_menu = Menu(root)
root.config(menu=main_menu)

def about_program():
  print('ABOUT')

# File
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Открыть")
file_menu.add_command(label="Сохранить")
file_menu.add_separator()
file_menu.add_command(label="Выход")
main_menu.add_cascade(label="Файл", menu=file_menu)

# Theme
theme_menu = Menu(main_menu, tearoff=0)
theme_menu_sub = Menu(theme_menu, tearoff=0)

theme_menu_sub.add_command(label="Light theme")
theme_menu_sub.add_command(label="Dark theme")

theme_menu.add_cascade(label="Оформление", menu=theme_menu_sub)
theme_menu.add_command(label="О программе", command=about_program)

main_menu.add_cascade(label="Разное", menu=theme_menu)

# Text
f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)



t = Text(f_text, bg="#343D46", fg="#C6DEC1", padx=10, pady=10, wrap=WORD, insertbackground="#EDA756", selectbackground="#4E5A65", width=30, spacing3=10)
t.pack(fill=BOTH, expand=1, side=LEFT)

# Scrollbar
scroll = Scrollbar(f_text, command=t.yview)
scroll.pack(fill=Y, side=LEFT)
t.config(yscrollcommand=scroll.set)

root.mainloop()