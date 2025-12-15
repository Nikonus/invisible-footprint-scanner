# 🕵️ Invisible Internet Footprint Scanner (CLI)

A **Python-based OSINT (Open Source Intelligence) CLI tool** that helps users understand **where their digital identity is publicly visible on the internet** and guides them on **how to reduce their online footprint**.

> ⚠️ This tool is built for **privacy awareness and education only**.  
> It does **NOT** access private databases or bypass security systems.

---

## 🚀 Features

### ✅ Username Footprint Scanning
Checks whether a **public account exists** for a given username on platforms like:
- GitHub
- Reddit
- Dev.to
- Medium

This is done using **public profile URLs only**.

---

### ✅ Email Footprint Analysis
For a given email address, the tool:
- Checks for **public Gravatar presence**
- Identifies the **email provider**
- Gives awareness about **possible platforms to review**

⚠️ No private email databases are accessed.

---

### ✅ Phone Number Awareness Scan
- Detects **country code**
- Validates basic format
- Explains limitations of phone OSINT due to privacy laws

---

### ✅ Privacy-First Design
- No login attempts
- No scraping private APIs
- No paid or leaked databases
- No brute-force techniques

---

## 🧠 Why this tool exists

Many users want to:
- Know **where they may have old accounts**
- Remove unused or unwanted accounts
- Reduce digital traceability
- Improve online privacy

There is **no legal way** to automatically list all websites where someone created accounts.

This tool instead focuses on:
- **Confirmed public evidence**
- **Strong OSINT signals**
- **Clear user guidance**

---

## 🛠️ Tech Stack

- Python 3
- Requests (HTTP checks)
- CLI-based interface
- Modular backend design

---

## 📂 Project Structure

invisible-footprint-scanner/
├── scan.py # Main CLI entry point
├── email_scan.py # Email OSINT logic
├── phone_scan.py # Phone number analysis
├── platforms.py # Username-based platform checks
├── risk.py # Risk scoring logic
└── README.md



---

## ▶️ How to Run

### 1️⃣ Install dependencies

pip install requests
[+] Scanning username: Nikonus

📌 Example Output

GitHub    : FOUND
Reddit    : FOUND
Dev.to    : NOT FOUND
Medium    : NOT FOUND

Platforms Found: 2
Footprint Score: 3.5 / 10
