import tkinter as tk
import random

# Initialize scores
user_score = 0
computer_score = 0

# Function to generate computer's choice and determine the winner
def play_round(user_choice):
    global user_score, computer_score
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    # Display choices
    user_choice_label.config(text=f"Your Choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")

    # Determine the result
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1

    # Update result and scores
    result_label.config(text=result)
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer's Score: {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="Your Choice: ")
    computer_choice_label.config(text="Computer's Choice: ")
    result_label.config(text="Result: ")
    user_score_label.config(text="Your Score: 0")
    computer_score_label.config(text="Computer's Score: 0")

# Initialize main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("400x400")

# Title Label
title_label = tk.Label(root, text="Rock, Paper, Scissors Game", font=("Arial", 16))
title_label.pack(pady=10)

# User choice display
user_choice_label = tk.Label(root, text="Your Choice: ", font=("Arial", 12))
user_choice_label.pack(pady=5)

# Computer choice display
computer_choice_label = tk.Label(root, text="Computer's Choice: ", font=("Arial", 12))
computer_choice_label.pack(pady=5)

# Result label
result_label = tk.Label(root, text="Result: ", font=("Arial", 14), fg="blue")
result_label.pack(pady=20)

# Score labels
user_score_label = tk.Label(root, text="Your Score: 0", font=("Arial", 12))
user_score_label.pack(pady=5)
computer_score_label = tk.Label(root, text="Computer's Score: 0", font=("Arial", 12))
computer_score_label.pack(pady=5)

# Buttons for user to choose rock, paper, or scissors
rock_button = tk.Button(root, text="Rock", command=lambda: play_round("Rock"), font=("Arial", 12), width=10)
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", command=lambda: play_round("Paper"), font=("Arial", 12), width=10)
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_round("Scissors"), font=("Arial", 12), width=10)
scissors_button.pack(pady=5)

# Reset button to start a new game
reset_button = tk.Button(root, text="Reset Game", command=reset_game, font=("Arial", 12), width=10, fg="red")
reset_button.pack(pady=20)

# Run the main event loop
root.mainloop()
