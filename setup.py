from setuptools import setup

APP = ['gui_typer.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': False,
    'packages': ['pyperclip', 'pyautogui', 'tkinter', 'rubicon'],
    'plist': {
        'CFBundleName': 'AutoTyper',
        'CFBundleDisplayName': 'Auto Typer',
        'CFBundleIdentifier': 'com.autotyper.app',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'NSHighResolutionCapable': True,
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
