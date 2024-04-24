import pyautogui
from pynput import keyboard
from PyQt5.QtCore import QThread
import sys

class HotkeyListener(QThread):

    def __init__(self, hotkey_start,hotkey_stop, texts_list):
        super().__init__()
        self.hotkey_start = hotkey_start
        self.hotkey_stop = hotkey_stop
        self.texts_list = texts_list
        self.i = 0

    def on_activate(self):
        if self.i < len(self.texts_list) and self.texts_list[self.i] != 'finalize':
            pyautogui.typewrite(self.texts_list[self.i])
            self.i += 1
        else:
            pyautogui.typewrite('no more')

    def stop(self):
        sys.exit() 

    def run(self):
        with keyboard.GlobalHotKeys({self.hotkey_start: self.on_activate,self.hotkey_stop: self.stop}) as h:
            h.join()

def main():   
    text=''
    texts_list=[]
    hotkey_start = input('Enter the hotkey_start: ')
    hotkey_stop = input('Enter the hotkey_stop: ')
    while text!='finalize':
        text = input('''Enter the paragraphs to type, enter 'finalize' when you are done: ''')
        texts_list.append(text)
    
    listener = HotkeyListener(hotkey_start,hotkey_stop, texts_list)
    listener.run()

if __name__ == '__main__':
    main()