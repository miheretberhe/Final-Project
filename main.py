import tkinter as tk
from tkinter import messagebox
from random import choice

# Initialize the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("400x300")
root.configure(bg='lightblue')  # Set background color

# Variables to track rounds and timer
round_counter = 0
timer_seconds = 10
max_rounds = 3

# Function to play the game
def play(user_choice):
    global round_counter
    if round_counter < max_rounds:
        computer_choice = choice(['rock', 'paper', 'scissors'])
        user_choice_var.set(f"You chose: {user_choice}")
        computer_choice_var.set(f"Computer chose: {computer_choice}")
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            result = "You win!"
        else:
            result = "You lose!"
        result_var.set(result)
        round_counter += 1
        round_counter_var.set(f"Rounds played: {round_counter}")
        if round_counter == max_rounds:
            messagebox.showinfo("Game Over", "The game is over after three rounds!")
            root.destroy()

# Function to exit the game
def exit_game():
    root.destroy()

# Function to open the second window
def open_second_window():
    second_window = tk.Toplevel(root)
    second_window.title("Second Window")
    second_window.geometry("200x100")
    second_window.configure(bg='lightgreen')  # Set background color
    tk.Label(second_window, text="This is the second window", bg='lightgreen').pack(pady=20)
    tk.Button(second_window, text="Close", command=second_window.destroy).pack(pady=10)

# Function to update the timer
def update_timer():
    global timer_seconds
    if timer_seconds > 0:
        timer_seconds -= 1
        timer_var.set(f"Time left: {timer_seconds} seconds")
        root.after(1000, update_timer)
    else:
        messagebox.showinfo("Time's up!", "The game is over!")
        root.destroy()

# Add labels, buttons, and images
tk.Label(root, text="Choose Rock, Paper, or Scissors:", bg='lightblue', font=('Helvetica', 14)).pack(pady=10)
user_choice_var = tk.StringVar()
computer_choice_var = tk.StringVar()
result_var = tk.StringVar()
round_counter_var = tk.StringVar(value="Rounds played: 0")
timer_var = tk.StringVar(value=f"Time left: {timer_seconds} seconds")
tk.Label(root, textvariable=user_choice_var, bg='lightblue', font=('Helvetica', 12)).pack(pady=5)
tk.Label(root, textvariable=computer_choice_var, bg='lightblue', font=('Helvetica', 12)).pack(pady=5)
tk.Label(root, textvariable=result_var, bg='lightblue', font=('Helvetica', 12)).pack(pady=5)
tk.Label(root, textvariable=round_counter_var, bg='lightblue', font=('Helvetica', 12)).pack(pady=5)
tk.Label(root, textvariable=timer_var, bg='lightblue', font=('Helvetica', 12)).pack(pady=5)
tk.Button(root, text="Rock", command=lambda: play('rock'), bg='white', font=('Helvetica', 12)).pack(side=tk.LEFT, padx=20)
tk.Button(root, text="Paper", command=lambda: play('paper'), bg='white', font=('Helvetica', 12)).pack(side=tk.LEFT)
tk.Button(root, text="Scissors", command=lambda: play('scissors'), bg='white', font=('Helvetica', 12)).pack(side=tk.LEFT, padx=20)
tk.Button(root, text="Exit", command=exit_game, bg='red', font=('Helvetica', 12)).pack(pady=20)
tk.Button(root, text="Open Second Window", command=open_second_window, bg='yellow', font=('Helvetica', 12)).pack(pady=20)

# Load and display images
rock_img = tk.PhotoImage(file="rock.png")
paper_img = tk.PhotoImage(file="paper.png")
scissors_img = tk.PhotoImage(file="scissors.png")
tk.Label(root, image=rock_img, text="Rock", compound="top", bg='lightblue').pack(side=tk.LEFT, padx=10)
tk.Label(root, image=paper_img, text="Paper", compound="top", bg='lightblue').pack(side=tk.LEFT, padx=10)
tk.Label(root, image=scissors_img, text="Scissors", compound="top", bg='lightblue').pack(side=tk.LEFT, padx=10)

# Start the timer
update_timer()

# Run the main loop
root.mainloop()
