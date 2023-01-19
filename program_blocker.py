import time
import os
import sys

import keyboard

def pkill(process_name):
    os.system(f'TASKKILL /f /IM {process_name}')
    
def program_blocker():
    os.system('cls')
    
    pkill('Viber.exe')
    pkill('Telegram.exe')
    pkill('Chrome.exe')
    pkill('Discord.exe')
    pkill('sublime_text.exe')
    pkill('lghub.exe')
    pkill('opera.exe')
    pkill('firefox.exe')
    pkill('yandex.exe')
    pkill('msedge.exe')
    
    os.system('cls')
    
def Start():
    while True:
        if keyboard.is_pressed('o'):
            sys.exit()
        else:
            program_blocker()
            
Start()
