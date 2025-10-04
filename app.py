from flask import Flask, render_template
import pyperclip
import pyautogui
import time

# Initialize the Flask app
app = Flask(__name__)

# This function defines what happens when you go to the main page
@app.route('/')
def index():
    # It will show the 'index.html' page
    return render_template('index.html')

# This function runs when the button on the webpage is clicked
@app.route('/run_script', methods=['POST'])
def run_script():
    try:
        # Give yourself 3 seconds to switch to the target window
        time.sleep(3)

        # Get text from the clipboard
        text = pyperclip.paste()
        lines = text.splitlines()

        # Type each line
        for line in lines:
            stripped_line = line.lstrip(' \t')
            pyautogui.write(stripped_line, interval=0)
            pyautogui.press('enter')
        
        print("Script executed successfully!")
        return "<h3>✅ Typing complete! You can close this tab.</h3>"

    except Exception as e:
        print(f"An error occurred: {e}")
        return f"<h3>❌ An error occurred: {e}</h3>"

# This allows you to run the app by running 'python app.py'
if __name__ == '__main__':
    app.run(port=5000)