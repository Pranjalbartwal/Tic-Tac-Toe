
import tkinter as tk
from tkinter import messagebox
import random

# Game settings
HUMAN = "X"
COMPUTER = "O"

board = [""] * 9
human_score = 0
computer_score = 0
draw_score = 0
game_over = False

def check_winner(player):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def update_score():
    score_label.config(
        text=f"You: {human_score}   Computer: {computer_score}   Draws: {draw_score}"
    )

def finish_game(message, winner):
    global game_over, human_score, computer_score, draw_score
    game_over = True

    if winner == HUMAN:
        human_score += 1
    elif winner == COMPUTER:
        computer_score += 1
    elif winner == "Draw":
        draw_score += 1

    update_score()
    status_label.config(text=message)

def computer_move():
    global board

    if game_over:
        return

    # Win if possible
    for i in range(9):
        if board[i] == "":
            board[i] = COMPUTER
            if check_winner(COMPUTER):
                return i
            board[i] = ""

    # Block the player's winning move
    for i in range(9):
        if board[i] == "":
            board[i] = HUMAN
            if check_winner(HUMAN):
                board[i] = ""
                return i
            board[i] = ""

    # Prefer the center
    if board[4] == "":
        return 4

    # Prefer corners
    corners = [i for i in [0, 2, 6, 8] if board[i] == ""]
    if corners:
        return random.choice(corners)

    # Choose any remaining square
    empty = [i for i in range(9) if board[i] == ""]
    if empty:
        return random.choice(empty)

    return None

def player_move(index):
    global board

    if game_over or board[index] != "":
        return

    board[index] = HUMAN
    buttons[index].config(text=HUMAN, fg="#2563eb")

    if check_winner(HUMAN):
        finish_game("Congratulations! You won!", HUMAN)
        return

    if all(cell != "" for cell in board):
        finish_game("It's a draw!", "Draw")
        return

    status_label.config(text="Computer is thinking...")
    root.after(400, make_computer_move)

def make_computer_move():
    global board

    if game_over:
        return

    move = computer_move()

    if move is not None:
        board[move] = COMPUTER
        buttons[move].config(text=COMPUTER, fg="#dc2626")

    if check_winner(COMPUTER):
        finish_game("Computer wins! Try again.", COMPUTER)
    elif all(cell != "" for cell in board):
        finish_game("It's a draw!", "Draw")
    else:
        status_label.config(text="Your turn! You are X.")

def reset_game():
    global board, game_over
    board = [""] * 9
    game_over = False

    for button in buttons:
        button.config(text="", fg="#111827")

    status_label.config(text="Your turn! You are X.")

def reset_scores():
    global human_score, computer_score, draw_score
    human_score = computer_score = draw_score = 0
    update_score()
    reset_game()

# Create the window
root = tk.Tk()
root.title("Tic-Tac-Toe vs Computer")
root.geometry("380x490")
root.resizable(False, False)
root.configure(bg="#f3f4f6")

title = tk.Label(
    root, text="TIC-TAC-TOE",
    font=("Arial", 23, "bold"),
    bg="#f3f4f6", fg="#111827"
)
title.pack(pady=12)

score_label = tk.Label(
    root, text="You: 0   Computer: 0   Draws: 0",
    font=("Arial", 11, "bold"),
    bg="#f3f4f6", fg="#374151"
)
score_label.pack(pady=5)

status_label = tk.Label(
    root, text="Your turn! You are X.",
    font=("Arial", 12),
    bg="#f3f4f6", fg="#047857"
)
status_label.pack(pady=10)

board_frame = tk.Frame(root, bg="#d1d5db")
board_frame.pack(pady=8)

buttons = []

for i in range(9):
    button = tk.Button(
        board_frame,
        text="",
        font=("Arial", 28, "bold"),
        width=4,
        height=2,
        bg="white",
        activebackground="#e5e7eb",
        relief="flat",
        command=lambda i=i: player_move(i)
    )
    button.grid(
        row=i // 3,
        column=i % 3,
        padx=3,
        pady=3
    )
    buttons.append(button)

tk.Button(
    root, text="New Game",
    font=("Arial", 11, "bold"),
    bg="#2563eb", fg="white",
    width=15, relief="flat",
    command=reset_game
).pack(pady=8)

tk.Button(
    root, text="Reset Scores",
    font=("Arial", 10),
    bg="#e5e7eb", fg="#111827",
    width=15, relief="flat",
    command=reset_scores
).pack(pady=2)

root.mainloop()

