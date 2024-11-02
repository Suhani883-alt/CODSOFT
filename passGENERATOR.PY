import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate the password
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Invalid Length", "Please enter a positive number for length.")
            return
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for length.")
        return

    # Options for password complexity
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()

    if not (use_upper or use_lower or use_digits or use_special):
        messagebox.showerror("No Options Selected", "Please select at least one character type.")
        return

    # Create character pool based on selected options
    char_pool = ""
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation

    # Generate password by randomly choosing characters from the pool
    password = ''.join(random.choice(char_pool) for _ in range(length))
    
    # Display the generated password
    password_entry.config(state='normal')  # Ensure the field is writable
    password_entry.delete(0, tk.END)  # Clear any previous password
    password_entry.insert(0, password)  # Insert the new password
    password_entry.config(state='readonly')  # Make the field read-only again

# Initialize the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

# Title Label
title_label = tk.Label(root, text="Password Generator", font=("Arial", 16))
title_label.pack(pady=10)

# Length Label and Entry
length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=5)
length_entry = tk.Entry(root, width=10)
length_entry.pack(pady=5)

# Checkbox options for character types
upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()

upper_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var)
upper_check.pack(pady=2)
lower_check = tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var)
lower_check.pack(pady=2)
digits_check = tk.Checkbutton(root, text="Include Digits", variable=digits_var)
digits_check.pack(pady=2)
special_check = tk.Checkbutton(root, text="Include Special Characters", variable=special_var)
special_check.pack(pady=2)

# Generate Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12), width=20)
generate_button.pack(pady=20)

# Entry to display the generated password
password_entry = tk.Entry(root, width=30, font=("Arial", 12), state='readonly')
password_entry.pack(pady=10)

# Run the application
root.mainloop()
