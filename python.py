import tkinter as tk
from tkinter import messagebox
import random

def start_game():
    """Initialize the game variables and UI components."""
    global target_number, attempts
    target_number = random.randint(1, 20)  # Random number between 1 and 20
    attempts = 0
    instructions_label.config(text="Guess a number between 1 and 20!")
    entry.delete(0, tk.END)

def check_guess():
    """Check the player's guess against the target number."""
    global attempts
    try:
        guess = int(entry.get())
        attempts += 1

        if guess < target_number:
            feedback_label.config(text="Too low! Try again.")
        elif guess > target_number:
            feedback_label.config(text="Too high! Try again.")
        else:
            messagebox.showinfo("Congratulations!", f"You guessed it! The number was {target_number}.\nIt took you {attempts} attempts.")
            start_game()
    except ValueError:
        feedback_label.config(text="Please enter a valid number.")

# Set up the main window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")
root.resizable(False, False)

# Create UI components
instructions_label = tk.Label(root, text="Guess a number between 1 and 20!", font=("Arial", 14))
instructions_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=5)

check_button = tk.Button(root, text="Check Guess", font=("Arial", 12), command=check_guess)
check_button.pack(pady=5)

feedback_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
feedback_label.pack(pady=10)

restart_button = tk.Button(root, text="Restart Game", font=("Arial", 12), command=start_game)
restart_button.pack(pady=10)

# Start the game
start_game()

# Run the application
root.mainloop()
