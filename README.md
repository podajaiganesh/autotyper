# AutoTyper ⌨️

A cross-platform desktop app that automatically types out the contents of your clipboard into any application — useful for environments that block paste (VMs, remote desktops, restricted terminals, etc).

Works on **macOS** and **Windows**.

---

## Requirements

- Python 3.11+
- pip (comes with Python)

---

## Installation

### macOS

**1. Clone or download the project**
```bash
git clone https://github.com/podajaiganesh/autotyper.git
cd autotyper
```

**2. Create and activate a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install pyperclip pyautogui
```

**4. Run the app**
```bash
python3 gui_typer.py
```

---

### Windows

**1. Install Python**
- Download Python 3.11+ from https://www.python.org/downloads/
- During installation, check **"Add Python to PATH"**

**2. Clone or download the project**
```bash
git clone https://github.com/podajaiganesh/autotyper.git
cd autotyper
```

Or download the ZIP from GitHub and extract it.

**3. Create and activate a virtual environment**
```cmd
python -m venv venv
venv\Scripts\activate
```

**4. Install dependencies**
```cmd
pip install pyperclip pyautogui
```

**5. Run the app**
```cmd
python gui_typer.py
```

---

## How to Use

1. **Copy** the text you want to type (`Cmd+C` on Mac / `Ctrl+C` on Windows)
2. **Open** AutoTyper and click **"Start Typing"**
3. **Switch** to the target window within **3 seconds**
4. The app will automatically type out your clipboard line by line

---

## Building a Standalone App (No Terminal Needed)

### macOS — Build as .app

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name="AutoTyper" --windowed -y gui_typer.py
```

The app will be at `dist/AutoTyper.app`. Double-click to run it.

> If macOS blocks it: **System Settings → Privacy & Security → Open Anyway**

### Windows — Build as .exe

```cmd
venv\Scripts\activate
pip install pyinstaller
pyinstaller --name="AutoTyper" --windowed --onefile gui_typer.py
```

The executable will be at `dist\AutoTyper.exe`. Double-click to run it.

---

## Project Structure

```
autotyper/
├── gui_typer.py       # Main GUI application (cross-platform)
├── auto_typer.py      # Standalone CLI script (no GUI)
├── setup.py           # py2app build config (macOS)
├── AutoTyper.spec     # PyInstaller build spec
├── README.md
├── venv/              # Virtual environment (not committed)
├── build/             # PyInstaller build files
└── dist/
    ├── AutoTyper.app  # Built macOS app
    └── AutoTyper.exe  # Built Windows executable
```

---

## Troubleshooting

### macOS

**App won't open**
> System Settings → Privacy & Security → click "Open Anyway"

**Accessibility permission error**
> System Settings → Privacy & Security → Accessibility → enable AutoTyper

**`python` command not found**
> Use `python3` instead

### Windows

**`python` is not recognized**
> Reinstall Python and make sure to check **"Add Python to PATH"** during setup

**`pip` is not recognized**
> Run `python -m pip install pyperclip pyautogui` instead

**Text not pasting into target window**
> Some apps block `Ctrl+V`. Try a different target app or run AutoTyper as Administrator

**Antivirus blocks the .exe**
> This is a false positive. Add an exception for `AutoTyper.exe` in your antivirus settings

### Both Platforms

**Text not typing correctly**
> Switch to the target window quickly within the 3-second countdown
