from tkinter import *

def clicked():
    res = "Здрасте {}".format(txt.get())
    lbl.configure(text=res)

def show_profile():
    res = f"Привет {txt.get()}, возраст {txt2.get()}, город {txt3.get()}!"
    lbl.configure(text=res)

def clear_all():
    lbl.configure(text="Привет")
    txt.delete(0, END)
    txt2.delete(0, END)
    txt3.delete(0, END)

window = Tk()
window.title("Уникальное приложение")
window.geometry("700x300")
window.configure(bg="lightblue")
window.resizable(False, False)

lbl = Label(window, text="Привет", font=("Verdana", 30, "bold"), bg="green", fg="red", anchor='center', relief="ridge", bd=5)
lbl.grid(column=0, row=0, columnspan=3, pady=20, sticky='ew')

# Метки и поля
Label(window, text="Имя(Name):", bg="lightblue").grid(column=0, row=1, sticky='w', padx=10)
txt = Entry(window, width=20, bg='white', relief="sunken")
txt.grid(column=1, row=1, padx=10)
Label(window, text="Возраст(Age):", bg="lightblue").grid(column=0, row=2, sticky='w', padx=10)
txt2 = Entry(window, width=20, bg='lightyellow', relief="sunken")
txt2.grid(column=1, row=2, padx=10)
Label(window, text="Город(Town):", bg="lightblue").grid(column=0, row=3, sticky='w', padx=10)
txt3 = Entry(window, width=20, bg='lightcoral', relief="sunken")
txt3.grid(column=1, row=3, padx=10)

# Кнопки
btn = Button(window, text="Привет", command=clicked, bg='green', fg='white', font=("Verdana", 10, "bold"))
btn.grid(column=2, row=1, pady=10)
btn2 = Button(window, text="Показать профиль", command=show_profile, bg='black', fg='white', font=("Verdana", 10, "bold"))
btn2.grid(column=2, row=2, pady=10)
btn3 = Button(window, text="Удалить", command=clear_all, bg='purple', fg='white', font=("Verdana", 10, "bold"))
btn3.grid(column=2, row=3, pady=10)

# Распределение
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

window.mainloop()
