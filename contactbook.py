import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# Contact storage
contacts = []

# Function to add a new contact
def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if name == "" or phone == "":
        messagebox.showerror("Input Error", "Name and phone number are required.")
        return

    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    messagebox.showinfo("Success", "Contact added successfully.")
    refresh_contact_list()

# Function to refresh contact list display
def refresh_contact_list():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Function to view all contact details
def view_contact():
    selected_index = contact_listbox.curselection()
    if not selected_index:
        messagebox.showerror("Selection Error", "Please select a contact to view.")
        return
    index = selected_index[0]
    contact = contacts[index]
    messagebox.showinfo(
        "Contact Details",
        f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}"
    )

# Function to search contacts by name or phone number
def search_contact():
    query = simpledialog.askstring("Search Contact", "Enter name or phone number:")
    if query:
        contact_listbox.delete(0, tk.END)
        for contact in contacts:
            if query.lower() in contact["name"].lower() or query in contact["phone"]:
                contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Function to update selected contact
def update_contact():
    selected_index = contact_listbox.curselection()
    if not selected_index:
        messagebox.showerror("Selection Error", "Please select a contact to update.")
        return
    index = selected_index[0]
    contact = contacts[index]

    new_name = simpledialog.askstring("Update Contact", "Enter new name:", initialvalue=contact['name'])
    new_phone = simpledialog.askstring("Update Contact", "Enter new phone number:", initialvalue=contact['phone'])
    new_email = simpledialog.askstring("Update Contact", "Enter new email:", initialvalue=contact['email'])
    new_address = simpledialog.askstring("Update Contact", "Enter new address:", initialvalue=contact['address'])

    if new_name and new_phone:
        contacts[index] = {"name": new_name, "phone": new_phone, "email": new_email, "address": new_address}
        messagebox.showinfo("Success", "Contact updated successfully.")
        refresh_contact_list()

# Function to delete selected contact
def delete_contact():
    selected_index = contact_listbox.curselection()
    if not selected_index:
        messagebox.showerror("Selection Error", "Please select a contact to delete.")
        return
    index = selected_index[0]
    contacts.pop(index)
    messagebox.showinfo("Success", "Contact deleted successfully.")
    refresh_contact_list()

# Main GUI window
root = tk.Tk()
root.title("Contact Management")
root.geometry("400x400")

# Input fields for contact details
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack(pady=5)

phone_label = tk.Label(root, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(root, width=40)
phone_entry.pack(pady=5)

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root, width=40)
email_entry.pack(pady=5)

address_label = tk.Label(root, text="Address:")
address_label.pack()
address_entry = tk.Entry(root, width=40)
address_entry.pack(pady=5)

# Buttons for contact operations
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Contact", command=add_contact, width=15)
add_button.grid(row=0, column=0, padx=5, pady=5)

view_button = tk.Button(button_frame, text="View Contact", command=view_contact, width=15)
view_button.grid(row=0, column=1, padx=5, pady=5)

search_button = tk.Button(button_frame, text="Search Contact", command=search_contact, width=15)
search_button.grid(row=1, column=0, padx=5, pady=5)

update_button = tk.Button(button_frame, text="Update Contact", command=update_contact, width=15)
update_button.grid(row=1, column=1, padx=5, pady=5)

delete_button = tk.Button(button_frame, text="Delete Contact", command=delete_contact, width=15)
delete_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Contact list display
contact_listbox = tk.Listbox(root, width=50, height=10)
contact_listbox.pack(pady=10)

# Run the main loop
root.mainloop()
