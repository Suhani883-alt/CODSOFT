import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel, StringVar, OptionMenu

# Initialize the root window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")

# List to store tasks
tasks = []

# Dictionary to map statuses with colors
status_colors = {
    "Pending": "orange",
    "In Progress": "blue",
    "Completed": "green",
}

def display_tasks():
    """Clear the listbox and display all tasks with colors based on status."""
    task_listbox.delete(0, tk.END)
    for task in tasks:
        color = status_colors.get(task['status'], "black")
        task_listbox.insert(tk.END, f"{task['name']} [{task['status']}]")
        task_listbox.itemconfig(tk.END, {'fg': color})

def add_task():
    """Prompt to add a new task."""
    task_name = simpledialog.askstring("Add Task", "Enter task name:")
    if task_name:
        tasks.append({"name": task_name, "status": "Pending"})
        display_tasks()

def update_task():
    """Update the selected task's status using a dropdown."""
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Select Task", "Please select a task to update.")
        return

    task_index = selected[0]
    task = tasks[task_index]

    # Create a top-level window for the status selection
    update_window = Toplevel(root)
    update_window.title("Update Task Status")
    update_window.geometry("250x150")
    
    tk.Label(update_window, text="Select new status:").pack(pady=10)

    # Dropdown menu for status selection
    status_var = StringVar(update_window)
    status_var.set(task['status'])  # Set current status as default
    status_options = ["Pending", "In Progress", "Completed"]
    status_menu = OptionMenu(update_window, status_var, *status_options)
    status_menu.pack(pady=10)

    def save_status():
        new_status = status_var.get()
        task['status'] = new_status
        display_tasks()
        update_window.destroy()
        messagebox.showinfo("Task Updated", f"Task '{task['name']}' updated to '{new_status}'!")

    tk.Button(update_window, text="Save", command=save_status).pack(pady=10)

def delete_task():
    """Delete the selected task."""
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Select Task", "Please select a task to delete.")
        return

    task_index = selected[0]
    task_name = tasks[task_index]['name']
    tasks.pop(task_index)
    display_tasks()
    messagebox.showinfo("Task Deleted", f"Task '{task_name}' has been deleted.")

# GUI Elements
frame = tk.Frame(root)
frame.pack(pady=10)

task_listbox = tk.Listbox(frame, width=40, height=15, font=("Arial", 14), selectmode=tk.SINGLE)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task, width=15)
add_button.pack(pady=5)

update_button = tk.Button(root, text="Update Task", command=update_task, width=15)
update_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, width=15)
delete_button.pack(pady=5)

# Start the main event loop
display_tasks()  # Initialize the display
root.mainloop()
