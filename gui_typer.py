import tkinter as tk
from tkinter import messagebox
import pyperclip
import pyautogui
import time
import threading
import platform

def type_line(line):
    """Cross-platform line typing using clipboard paste for special characters."""
    stripped = line.lstrip(' \t')
    if not stripped:
        pyautogui.press('enter')
        return
    pyperclip.copy(stripped)
    if platform.system() == 'Darwin':
        pyautogui.hotkey('command', 'v')
    else:
        pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.05)
    pyautogui.press('enter')

def start_typing():
    def type_text():
        try:
            status_label.config(text="⏳ Switch to target window... (3 seconds)", fg="#FF9800")
            window.update()
            time.sleep(3)

            text = pyperclip.paste()
            lines = text.splitlines()

            for line in lines:
                type_line(line)

            status_label.config(text="✅ Typing complete!", fg="#4CAF50")
        except Exception as e:
            status_label.config(text=f"❌ Error: {e}", fg="#F44336")

    threading.Thread(target=type_text, daemon=True).start()

window = tk.Tk()
window.title("Auto Typer")
window.geometry("600x500")
window.resizable(False, False)
window.configure(bg="#1e1e2e")

title_frame = tk.Frame(window, bg="#1e1e2e")
title_frame.pack(pady=40)

title_label = tk.Label(title_frame, text="⌨️ Auto Typer", font=("Arial", 36, "bold"), 
                      bg="#1e1e2e", fg="#89b4fa")
title_label.pack()

subtitle_label = tk.Label(title_frame, text="Clipboard to Keyboard Automation", 
                         font=("Arial", 14), bg="#1e1e2e", fg="#cdd6f4")
subtitle_label.pack(pady=5)

instructions_frame = tk.Frame(window, bg="#313244", relief="flat", bd=0)
instructions_frame.pack(pady=30, padx=50, fill="both")

instructions_title = tk.Label(instructions_frame, text="How to Use:", 
                             font=("Arial", 16, "bold"), bg="#313244", fg="#f5e0dc", anchor="w")
instructions_title.pack(pady=(20, 10), padx=20, anchor="w")

instructions = [
    "1. Copy the text you want to type",
    "2. Click the 'Start Typing' button below",
    "3. Quickly switch to your target window",
    "4. Text will auto-type after 3 seconds"
]

for instruction in instructions:
    label = tk.Label(instructions_frame, text=instruction, font=("Arial", 13), 
                    bg="#313244", fg="#cdd6f4", anchor="w")
    label.pack(pady=5, padx=30, anchor="w")

instructions_frame.pack_configure(pady=(30, 20))

start_button = tk.Button(window, text="Start Typing", command=start_typing, 
                        bg="#89b4fa", fg="#1e1e2e", font=("Arial", 18, "bold"), 
                        padx=50, pady=15, cursor="hand2", relief="flat", 
                        activebackground="#74c7ec", activeforeground="#1e1e2e")
start_button.pack(pady=20)

status_label = tk.Label(window, text="Ready", font=("Arial", 14), bg="#1e1e2e", fg="#a6adc8")
status_label.pack(pady=10)

window.mainloop()
