import pyautogui
import csv
import sys
import time
from playsound import playsound


reader = csv.DictReader(open("/Users/aashild/Documents/Python/Åshild Autotilbud/data.csv"))

time.sleep(10)

playsound("AutoReq/Done_alert.mp3") # DING DING


for row in reader:
    print('Typing itemnumber:' + row['Varenummer'])
    pyautogui.typewrite(row['Varenummer'])
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.typewrite(row['Fysisk Antall'])
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.typewrite(row['Innkjøpsverdi'])
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('backspace')
    pyautogui.keyDown('ctrl')
    pyautogui.typewrite('n')
    pyautogui.keyUp('ctrl')

playsound("AutoReq/Done_alert.mp3") # DING DING
playsound("AutoReq/Done_alert.mp3") # DING DING

