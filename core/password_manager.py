import hashlib
import os
from tkinter import messagebox, simpledialog

PASSWORD_FILE = "data/app_password.dat"


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def load_stored_hash():
    try:
        with open(PASSWORD_FILE, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return None


def initial_password_setup(parent):
    messagebox.showinfo("Welcome!", "Please set a password.", parent=parent)

    while True:
        p1 = simpledialog.askstring("Create Password", "Enter password:", show='*', parent=parent)
        if not p1:
            return False
        p2 = simpledialog.askstring("Confirm Password", "Confirm password:", show='*', parent=parent)
        if not p2:
            return False

        if p1 == p2:
            os.makedirs("data", exist_ok=True)
            with open(PASSWORD_FILE, 'w') as f:
                f.write(hash_password(p1))
            messagebox.showinfo("Success", "Password set successfully.", parent=parent)
            return True
        else:
            messagebox.showerror("Error", "Passwords do not match.", parent=parent)


def check_password():
    stored_hash = load_stored_hash()
    if not stored_hash:
        messagebox.showerror("Error", "No password set.")
        return False

    password = simpledialog.askstring("Password Required", "Enter password:", show='*')
    if not password:
        return False

    return hash_password(password) == stored_hash
