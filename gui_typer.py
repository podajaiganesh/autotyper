import tkinter as tk
import pyperclip
import pyautogui
import time
import threading

# Characters that pyautogui.write() cannot handle — must use hotkey
SPECIAL = {
    '{': ['{'], '}': ['}'], '(': ['('], ')': [')'],
    '[': ['['], ']': [']'], '<': ['<'], '>': ['>'],
    '#': ['#'], '!': ['!'], '@': ['@'], '$': ['$'],
    '%': ['%'], '^': ['^'], '&': ['&'], '*': ['*'],
    '-': ['-'], '+': ['+'], '=': ['='], '|': ['|'],
    '\\': ['\\'], '/': ['/'], ':': [':'], ';': [';'],
    '"': ['"'], "'": ["'"], ',': [','], '.': ['.'],
    '?': ['?'], '`': ['`'], '~': ['~'], '_': ['_'],
    ' ': ['space'],
}

def type_line(line):
    i = 0
    while i < len(line):
        ch = line[i]
        if ch == '\t':
            # type 4 spaces for a tab
            for _ in range(4):
                pyautogui.press('space')
            i += 1
        elif ch in SPECIAL:
            pyautogui.press(SPECIAL[ch][0])
            i += 1
        else:
            # collect consecutive normal chars and write them at once
            chunk = ''
            while i < len(line) and line[i] not in SPECIAL and line[i] != '\t':
                chunk += line[i]
                i += 1
            if chunk:
                pyautogui.write(chunk, interval=0.01)

def start_typing():
    def type_text():
        try:
            original_text = pyperclip.paste()
            if not original_text.strip():
                status_label.config(text="⚠️ Clipboard is empty! Copy your code first.", fg="#FF9800")
                return

            status_label.config(text="⏳ Switch to target window... (5 seconds)", fg="#FF9800")
            window.update()
            time.sleep(5)

            lines = original_text.splitlines()
            for i, line in enumerate(lines):
                # Kill any auto-indent the editor inserted on this line
                pyautogui.hotkey('home')          # go to line start
                pyautogui.hotkey('shift', 'end')  # select to line end
                pyautogui.press('backspace')       # delete selected auto-indent
                time.sleep(0.01)
                type_line(line)
                if i < len(lines) - 1:
                    pyautogui.press('enter')
                    time.sleep(0.04)

            status_label.config(text="✅ Typing complete!", fg="#4CAF50")
        except Exception as e:
            status_label.config(text=f"❌ Error: {e}", fg="#F44336")

    threading.Thread(target=type_text, daemon=True).start()

window = tk.Tk()
window.title("Auto Typer")
window.geometry("600x620")
window.resizable(False, False)
window.configure(bg="#1e1e2e")

title_frame = tk.Frame(window, bg="#1e1e2e")
title_frame.pack(pady=20)

tk.Label(title_frame, text="⌨️ Auto Typer", font=("Arial", 36, "bold"),
         bg="#1e1e2e", fg="#89b4fa").pack()
tk.Label(title_frame, text="Clipboard to Keyboard Automation",
         font=("Arial", 14), bg="#1e1e2e", fg="#cdd6f4").pack(pady=5)

instructions_frame = tk.Frame(window, bg="#313244", relief="flat", bd=0)
instructions_frame.pack(pady=10, padx=50, fill="both")

tk.Label(instructions_frame, text="How to Use:", font=("Arial", 16, "bold"),
         bg="#313244", fg="#f5e0dc", anchor="w").pack(pady=(20, 10), padx=20, anchor="w")

for instruction in [
    "1. Copy the code you want to type  (Ctrl+C)",
    "2. Click the 'Start Typing' button below",
    "3. Quickly switch to your CodeChef editor",
    "4. Code will be typed after 5 seconds"
]:
    tk.Label(instructions_frame, text=instruction, font=("Arial", 13),
             bg="#313244", fg="#cdd6f4", anchor="w").pack(pady=5, padx=30, anchor="w")

instructions_frame.pack_configure(pady=(10, 10))

tk.Button(window, text="Start Typing", command=start_typing,
          bg="#89b4fa", fg="#1e1e2e", font=("Arial", 18, "bold"),
          padx=50, pady=15, cursor="hand2", relief="flat",
          activebackground="#74c7ec", activeforeground="#1e1e2e").pack(pady=20)

status_label = tk.Label(window, text="Ready — Copy your code then click Start Typing",
                        font=("Arial", 12), bg="#1e1e2e", fg="#a6adc8", wraplength=500)
status_label.pack(pady=10)

window.mainloop()
