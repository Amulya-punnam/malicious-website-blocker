---

#  Firewall Application – Malicious Website Blocker

A GUI-based cybersecurity application built using Python and Tkinter to block malicious websites, scan URLs for threats, and maintain secure access using password protection.

This project was developed as part of a Cyber Security Internship to demonstrate practical implementation of host-based website filtering and threat intelligence integration.

---

## Features

* 🔐 Password-protected access (SHA-256 hashing)
* 🚫 Block websites via Windows hosts file
* 🔓 Unblock previously blocked websites
* 🔎 Scan URLs using OpenPhish public threat feed
* 📝 Action logging system
* 🖥️ User-friendly GUI interface

---

##  Technologies Used

* Python
* Tkinter (GUI)
* Requests (API calls)
* Windows Hosts File
* SHA-256 Hashing
* OpenPhish Threat Intelligence Feed

---

##  Project Structure

```
Firewall-Application/
│
├── main.py
│
├── core/
│   ├── blocker.py
│   ├── scanner.py
│   ├── password_manager.py
│   ├── logger.py
│   └── utils.py
│
├── gui/
│   └── app.py
│
├── data/
│   ├── app_password.dat        (auto-created)
│   └── action_history.log      (auto-created)
│
├── requirements.txt
└── README.md
```

---

##  How It Works

### 1️⃣ Website Blocking

* Adds entries to the Windows hosts file:

  ```
  127.0.0.1 example.com
  ```
* Flushes DNS cache
* Prevents browser access

### 2️⃣ URL Scanning

* Downloads latest malicious URL feed from OpenPhish
* Compares user input URLs
* Displays whether URL is Safe or Malicious

### 3️⃣ Password Protection

* First-time setup requires password creation
* Password stored securely using SHA-256 hashing
* Required for blocking/unblocking actions

---

##  Installation & Setup

### Step 1: Clone Repository

```
git clone https://github.com/Amulya-punnam/malicious-website-blocker.git
cd firewall-application
```

### Step 2: Install Dependencies

```
pip install -r requirements.txt
```

### Step 3: Run Application

Run terminal as Administrator (important):

```
python main.py
```

---

##  Important Notes

* Must run as Administrator to modify hosts file.
* Windows OS required (hosts path configured for Windows).
* Data files are auto-created inside `/data` folder.
* For password reset, delete `data/app_password.dat`.

---

##  Learning Outcomes

* DNS and hosts file manipulation
* Secure password storage using hashing
* Threat intelligence integration
* GUI application development
* Modular project architecture

---

##  Future Improvements

* Linux & macOS support
* Real-time URL monitoring
* GUI improvements
* Export logs to CSV
* Advanced phishing detection using APIs

---

## Developed By

Cyber Security Internship Project
Firewall-based Malicious Website Blocking System

---

## License

This project is developed for educational purposes only.

