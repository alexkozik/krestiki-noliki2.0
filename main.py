import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("340x440") # увеличена высота для добавления кнопки сброса и табло

current_player = "X"
buttons = []
scores = {"X": 0, "O": 0}  # Словарь для хранения счёта
game_active = True  # Флаг активности игры

# сброс/новая игра
def reset_game(full_reset=False):
    global current_player, game_active
    current_player = "X"
    for row in buttons:
        for button in row:
            button.config(text="", state=tk.NORMAL)

    if full_reset:
        global scores
        scores = {"X": 0, "O": 0}
        game_active = True
    update_score_display()

def update_score_display():
    score_label.config(text=f"X: {scores['X']}  |  O: {scores['O']}")
    # Проверяем, достигнут ли лимит побед
    if scores['X'] >= 3 or scores['O'] >= 3:
        check_final_winner()


def check_final_winner():
    global game_active
    if scores['X'] >= 3:
        winner = "X"
    else:
        winner = "O"

    game_active = False
    for row in buttons:
        for button in row:
            button.config(state=tk.DISABLED)

    if messagebox.askyesno("Игра окончена",
                           f"Игрок {winner} победил в матче со счётом {scores['X']}:{scores['O']}!\n"
                           "Хотите начать новый матч?"):
        reset_game(full_reset=True)
    else:
        window.quit()
        
# ходы игроков
def on_click(row, col):
    global current_player
    buttons[row][col]['text'] = current_player
    if check_winner():
        scores[current_player] += 1
        messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")
        reset_game()
    elif is_board_full():
        messagebox.showinfo("Игра окончена", "Ничья!")
        reset_game()
    else:
        current_player = "O" if current_player == "X" else "X"


# проверка победителя
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

# пороверка ничьей
def is_board_full():
    for row in buttons:
        for button in row:
            if button["text"] == "":
                return False
    return True

# Создание табло счёта
score_label = tk.Label(window, text="X: 0  |  O: 0", font=("Arial", 16))
score_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="we")

# Создание игрового поля
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=3, command=lambda r=i, c=j: on_click(r, c))
        # Добавлены отступы между кнопками
        btn.grid(row=i+1, column=j, padx=5, pady=5)
        row.append(btn)
    buttons.append(row)

# Кнопка сброса
reset_btn = tk.Button(window, text="Новая игра", font=("Arial", 14), command=reset_game)
reset_btn.grid(row=4, column=0, columnspan=3, padx=5, pady=5, sticky="we")


window.mainloop()
