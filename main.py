#Password Generator
import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_password():
    global password_label
    length = int(length_entry.get())
    complexity = int(complexity_entry.get())

    if length <= 0 or complexity <= 0:
        messagebox.showerror("Error", "Length and complexity must be greater than 0.")
        return
    
    characters = ''
    if complexity >= 1:
        characters += string.ascii_letters
    if complexity >= 2:
        characters += string.digits
    if complexity >= 3:
        characters += string.punctuation
    
    if not characters:
        messagebox.showerror("Error", "Select at least one complexity option.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text=f"Generated Password: {password}")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")

length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

complexity_label = tk.Label(root, text="Password Complexity (1-3):")
complexity_label.pack(pady=5)
complexity_entry = tk.Spinbox(root, from_=1, to=3)
complexity_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=(10))

# Declare password_label
password_label = tk.Label(root, text="")
password_label.pack(pady=10)

root.mainloop()
