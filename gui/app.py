import tkinter as tk
from tkinter import scrolledtext
import os

from core.password_manager import initial_password_setup, check_password
from core.blocker import block_sites, unblock_sites
from core.scanner import scan_urls
from core.utils import parse_urls


def get_urls_from_user(root, title):
    dialog = tk.Toplevel(root)
    dialog.title(title)
    dialog.geometry("350x250")

    tk.Label(dialog, text="Enter URLs (comma or new line):").pack(pady=5)
    text_area = scrolledtext.ScrolledText(dialog, height=6)
    text_area.pack()

    result = {"urls": []}

    def submit():
        result["urls"] = parse_urls(text_area.get("1.0", tk.END))
        dialog.destroy()

    tk.Button(dialog, text="Submit", command=submit).pack(pady=10)

    dialog.transient(root)
    dialog.grab_set()
    root.wait_window(dialog)

    return result["urls"]


def run_app():
    root = tk.Tk()
    root.withdraw()

    if not os.path.exists("data/app_password.dat"):
        if not initial_password_setup(root):
            root.destroy()
            return

    root.deiconify()
    root.title("Firewall Application")
    root.geometry("400x400")

    tk.Label(root, text="Website Blocker", font=("Arial", 18, "bold")).pack(pady=20)

    def handle_block():
        if check_password():
            urls = get_urls_from_user(root, "Block Websites")
            block_sites(urls)

    def handle_unblock():
        if check_password():
            urls = get_urls_from_user(root, "Unblock Websites")
            unblock_sites(urls)

    def handle_scan():
        urls = get_urls_from_user(root, "Scan URLs")
        scan_urls(urls)

    tk.Button(root, text="Block Websites", command=handle_block, width=20).pack(pady=5)
    tk.Button(root, text="Unblock Websites", command=handle_unblock, width=20).pack(pady=5)
    tk.Button(root, text="Scan URLs", command=handle_scan, width=20).pack(pady=5)

    root.mainloop()
