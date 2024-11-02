import tkinter as tk
from tkinter import messagebox
import math

# Initialize the main window
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("300x500")

# Function to perform the calculation
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get()) if entry2.get() else None
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")
        return

    operation = operation_var.get()

    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 == 0:
            messagebox.showerror("Math Error", "Cannot divide by zero.")
            return
        result = num1 / num2
    elif operation == "Modulus":
        result = num1 % num2
    elif operation == "Exponentiation":
        result = num1 ** num2
    elif operation == "Floor Division":
        if num2 == 0:
            messagebox.showerror("Math Error", "Cannot divide by zero.")
            return
        result = num1 // num2
    elif operation == "Square Root":
        result = math.sqrt(num1)
    else:
        messagebox.showerror("No Operation Selected", "Please select an operation.")
        return

    result_label.config(text=f"Result: {result}")

# Input fields for numbers
entry1 = tk.Entry(root, width=15, font=("Arial", 14))
entry1.pack(pady=10)
entry2 = tk.Entry(root, width=15, font=("Arial", 14))
entry2.pack(pady=10)

# Dropdown menu for operation selection
operation_var = tk.StringVar(root)
operation_var.set("Select Operation")  # Default value
operation_menu = tk.OptionMenu(root, operation_var, 
                               "Add", "Subtract", "Multiply", "Divide",
                               "Modulus", "Exponentiation", "Floor Division", "Square Root")
operation_menu.config(width=15)
operation_menu.pack(pady=10)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate, font=("Arial", 14), width=10)
calculate_button.pack(pady=20)

# Label to display the result
result_label = tk.Label(root, text="Result: ", font=("Arial", 14))
result_label.pack(pady=20)

# Run the main loop
root.mainloop()
