import pyperclip
import pyautogui
import time
import platform

def type_line(line):
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

print("Switch to your target window. Typing will start in 3 seconds...")
time.sleep(3)

text = pyperclip.paste()
for line in text.splitlines():
    type_line(line)
