import requests
from tkinter import messagebox


def scan_urls(urls):
    try:
        messagebox.showinfo("Fetching Data", "Downloading OpenPhish feed...")
        response = requests.get("https://openphish.com/feed.txt", timeout=10)

        if response.status_code != 200:
            messagebox.showerror("Error", "Failed to fetch OpenPhish data.")
            return

        openphish_data = set(response.text.lower().splitlines())

        results = {}
        for url in urls:
            if any(url.lower() in phish for phish in openphish_data):
                results[url] = "Malicious"
            else:
                results[url] = "Safe"

        result_text = "\n".join([f"{u} → {r}" for u, r in results.items()])
        messagebox.showinfo("Scan Results", result_text)

    except Exception as e:
        messagebox.showerror("Error", str(e))
