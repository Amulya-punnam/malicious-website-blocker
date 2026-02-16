import subprocess
from tkinter import messagebox
from core.logger import log_action

HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"
REDIRECT_IP = "127.0.0.1"


def flush_dns_cache():
    try:
        subprocess.run("ipconfig /flushdns", shell=True, check=True)
    except Exception:
        messagebox.showwarning("Warning", "Could not flush DNS cache.")


def block_sites(websites):
    try:
        with open(HOSTS_PATH, 'r+') as file:
            content = file.read()
            blocked_now = []

            for site in websites:
                if site not in content:
                    file.write(f"\n{REDIRECT_IP}\t{site}")
                    blocked_now.append(site)

        flush_dns_cache()

        if blocked_now:
            log_action("Blocked", blocked_now)
            messagebox.showinfo("Success", "Blocked:\n" + "\n".join(blocked_now))
        else:
            messagebox.showinfo("Info", "All sites already blocked.")

    except PermissionError:
        messagebox.showerror("Error", "Run as Administrator.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def unblock_sites(websites):
    try:
        with open(HOSTS_PATH, 'r') as file:
            lines = file.readlines()

        with open(HOSTS_PATH, 'w') as file:
            for line in lines:
                if not any(site in line for site in websites):
                    file.write(line)

        flush_dns_cache()
        log_action("Unblocked", websites)
        messagebox.showinfo("Success", "Unblocked successfully.")

    except PermissionError:
        messagebox.showerror("Error", "Run as Administrator.")
    except Exception as e:
        messagebox.showerror("Error", str(e))
