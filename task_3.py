import random
import string
import tkinter as tk
import pyperclip

def generate_password():
    length = length_var.get()
    if length < 6:
        password_var.set("Password too short!")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

def copy_to_clipboard():
    pyperclip.copy(password_var.get())

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")

# Variables
length_var = tk.IntVar(value=12)
password_var = tk.StringVar()

# UI Elements
tk.Label(root, text="Password Length:").pack(pady=5)
tk.Scale(root, from_=6, to=32, orient="horizontal", variable=length_var).pack(pady=5)
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)
tk.Entry(root, textvariable=password_var, width=30).pack(pady=5)
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=10)

root.mainloop()
