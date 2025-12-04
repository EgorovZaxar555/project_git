import tkinter as tk
from tkinter import messagebox

# Создаём основное окно
root = tk.Tk()
root.title("Крестики-нолики")
root.geometry("300x400")

# Состояние игрового поля (1-9)
board = [''] * 9

# Создаём метки для поля 3x3
labels = []
for i in range(3):
    row = []
    for j in range(3):
        lbl = tk.Label(root, text='', font=("Arial", 24), width=3, height=1, relief="solid")
        lbl.grid(row=i, column=j, padx=5, pady=5)
        row.append(lbl)
    labels.append(row)

# Функция обновления отображения поля
def update_display():
    for i in range(3):
        for j in range(3):
            idx = i * 3 + j
            labels[i][j].config(text=board[idx])

# Текстовое поле для ввода номера клетки
entry_label = tk.Label(root, text="Введите номер клетки (1-9):")
entry_label.grid(row=3, column=0, columnspan=3, pady=(20, 5))

entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.grid(row=4, column=0, columnspan=3, pady=5)

# Функция установки символа
def place_symbol(symbol):
    try:
        pos = int(entry.get())
        if pos < 1 or pos > 9:
            messagebox.showerror("Ошибка", "Введите число от 1 до 9!")
            return
        idx = pos - 1  # преобразуем в индекс 0-8
        if board[idx] != '':
            messagebox.showwarning("Занято", "Эта клетка уже занята!")
            return
        board[idx] = symbol
        update_display()
        entry.delete(0, tk.END)  # очистить поле ввода
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное число!")

# Кнопки
btn_x = tk.Button(root, text="Поставить X", font=("Arial", 12), command=lambda: place_symbol('X'))
btn_o = tk.Button(root, text="Поставить O", font=("Arial", 12), command=lambda: place_symbol('O'))

btn_x.grid(row=5, column=0, pady=10, padx=5)
btn_o.grid(row=5, column=2, pady=10, padx=5)

# Инициализация отображения
update_display()

# Запуск приложения
root.mainloop()