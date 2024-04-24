import pyautogui
from pynput import keyboard
from PyQt5.QtCore import QThread
import sys
class HotkeyListener(QThread):

    def __init__(self, hotkey_start,hotkey_stop, text):
        super().__init__()
        self.hotkey_start = hotkey_start
        self.hotkey_stop = hotkey_stop
        self.text = text

    def on_activate(self):    
        pyautogui.typewrite(self.text)

    def stop(self):
        sys.exit() 

    def run(self):
        with keyboard.GlobalHotKeys({self.hotkey_start: self.on_activate,self.hotkey_stop: self.stop}) as h:
            h.join()

def main():
    hotkey_start = input('Enter the hotkey_start: ')
    hotkey_stop = input('Enter the hotkey_stop: ')
    text = input('Enter the text to type: ')
    
    listener = HotkeyListener(hotkey_start,hotkey_stop, text)
    listener.run()

if __name__ == '__main__':
    main()