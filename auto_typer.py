
import pyperclip
import pyautogui
import time

print("Switch to your target window. Typing will start in 3 seconds...")
time.sleep(3)

text = pyperclip.paste()

lines = text.splitlines()

for line in lines:
    # Remove leading tabs and spaces
    stripped_line = line.lstrip(' \t')
    
    # Type the stripped line (no delay for speed)
    pyautogui.write(stripped_line, interval=0)
    
    # Press Enter to move to next line
    pyautogui.press('enter')
