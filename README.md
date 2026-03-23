# ⌨️ AutoTyper

AutoTyper is a Windows desktop tool that **automatically types your clipboard code** into any editor — including CodeChef, Codeforces, or any online judge that blocks paste.

---

## 🚀 How It Works

Instead of pasting, AutoTyper **simulates real keyboard input** character by character — so it bypasses paste restrictions on online coding portals.

---

## 📦 Requirements

- Python 3.x
- pip packages: `pyautogui`, `pyperclip`

---

## ⚙️ Installation

**1. Clone or download this project**

**2. Install dependencies**
```
pip install pyautogui pyperclip
```

**3. Run the app**
```
python gui_typer.py
```

---

## 🖥️ Usage

1. **Copy** your code — `Ctrl+C`
2. **Run** the app — `python gui_typer.py`
3. **Click** the `Start Typing` button
4. **Switch** to your CodeChef / target editor within 5 seconds
5. AutoTyper will type your code automatically ✅

---

## ✅ Features

- Handles all special characters — `{`, `}`, `#`, `<`, `>`, `*`, `+`, etc.
- Preserves code indentation (spaces & tabs)
- Clears editor auto-indent before typing each line
- Fast typing speed with accurate output
- Clean dark-themed GUI

---

## 📁 Project Structure

```
autotyper/
├── gui_typer.py      # Main GUI application
├── auto_typer.py     # Terminal version (no GUI)
├── setup.py          # App packaging config
└── README.md         # This file
```

---

## ⚠️ Notes

- Make sure your **cursor is clicked inside the code editor** before the 5-second countdown ends
- Works best on **Windows**
- Do **not** move your mouse or type anything during the typing process

---

## 👨‍💻 Author

Built for competitive programmers to bypass paste restrictions on online judges.
