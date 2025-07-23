import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("340x400") # увеличена высота для добавления кнопки сброса

current_player = "X"
buttons = []

def reset_game():
    global current_player
    current_player = "X"
    for row in buttons:
        for button in row:
            button.config(text="")

def on_click(row, col):
    global current_player
    buttons[row][col]['text'] = current_player
    if check_winner():
        messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")
    current_player = "0" if current_player == "X" else "X"


def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True
        if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
            return True
        if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
            return True
    return False

# Создание игрового поля
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=3, command=lambda r=i, c=j: on_click(r, c))
        # Добавлены отступы между кнопками
        btn.grid(row=i, column=j, padx=5, pady=5)
        row.append(btn)
    buttons.append(row)

# Кнопка сброса
reset_btn = tk.Button(window, text="Новая игра", font=("Arial", 14), command=reset_game)
reset_btn.grid(row=3, column=0, columnspan=3, padx=5, pady=5, sticky="we")


window.mainloop()
