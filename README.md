# 🔐 Tkinter Password Generator

A simple password generator built with **Python Tkinter**.  
This GUI application allows users to generate secure random passwords with customizable length and optional special characters. It also includes clipboard copy functionality and reset options.

---

## ✨ Features
- Choose password length (numeric input only).
- Option to include special characters (`!@#$%&`).
- Generate random passwords using letters and digits.
- Copy generated password to clipboard with one click.
- Reset the form to start fresh.
- Custom icons for the app window and reset button.

---

## 📂 Project Structure

Password-Generator/
│
├── password_generator.py   # Main Tkinter application
├── icon.png                # App icon
├── reset.png               # Reset button image
└── README.md               # Documentation

---

## ▶️ How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/Password-Generator.git
   cd Password-Generator
2. Run the program:

bash
python password_generator.py


🛠 Requirements
Python 3.x

Tkinter (comes pre-installed with Python)

Standard libraries: string, random

📌 Notes
Ensure icon.png and reset.png are in the same folder as password_generator.py.

If you move the images, update the PhotoImage(file="...") paths in the code.
