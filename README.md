# AutoTyper ⌨️

A macOS desktop app that automatically types out the contents of your clipboard into any application — useful for environments that block paste (VMs, remote desktops, restricted terminals, etc).

---

## Requirements

- macOS
- Python 3.11+

---

## Installation

### 1. Clone or Download the project

```bash
git clone https://github.com/your-username/autotyper.git
cd autotyper
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install pyperclip pyautogui
```

---

## Running the App

### Option A — Run as Python script

```bash
source venv/bin/activate
python3 gui_typer.py
```

### Option B — Run as macOS App (no terminal needed)

A pre-built `.app` is available in the `dist/` folder:

```
dist/AutoTyper.app
```

Just double-click `AutoTyper.app` to launch it.

> If macOS blocks it, go to **System Settings → Privacy & Security** and click **"Open Anyway"**.

To install it permanently, drag `AutoTyper.app` to your **Applications** folder.

---

## How to Use

1. **Copy** the text you want to type (Cmd + C)
2. **Open** AutoTyper and click **"Start Typing"**
3. **Switch** to the target window within **3 seconds**
4. The app will automatically type out your clipboard line by line

---

## Building the macOS App Yourself

Make sure you have the venv activated, then run:

```bash
pip install pyinstaller
pyinstaller --name="AutoTyper" --windowed -y gui_typer.py
```

The built app will be at `dist/AutoTyper.app`.

---

## Project Structure

```
autotyper/
├── gui_typer.py       # Main GUI application
├── auto_typer.py      # Standalone CLI script (no GUI)
├── setup.py           # py2app build config
├── AutoTyper.spec     # PyInstaller build spec
├── README.md
├── venv/              # Virtual environment
├── build/             # PyInstaller build files
└── dist/
    └── AutoTyper.app  # Built macOS app
```

---

## Troubleshooting

**App won't open on macOS**
> Go to System Settings → Privacy & Security → click "Open Anyway"

**Accessibility permission error**
> Go to System Settings → Privacy & Security → Accessibility → enable AutoTyper

**`python` command not found**
> Use `python3` instead. macOS uses `python3` by default.

**Text not typing correctly**
> Make sure you switch to the target window quickly within the 3-second countdown.
