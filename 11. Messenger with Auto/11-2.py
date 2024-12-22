import pyautogui
import pyperclip
import time
import os

# 현재 실행 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))


try:
    picPosition = pyautogui.locateOnScreen('pic1.png')
    print(picPosition)
except pyautogui.ImageNotFoundException:
    try:
        picPosition = pyautogui.locateOnScreen('pic2.png')
        print(picPosition)
    except pyautogui.ImageNotFoundException:
        try:
            picPosition = pyautogui.locateOnScreen('pic3.png')
            print(picPosition)
        except pyautogui.ImageNotFoundException:
            print('ImageNotFoundException')

clickPosition = pyautogui.center(picPosition)
pyautogui.doubleClick(clickPosition)

pyperclip.copy("이 메시지는 자동으로 전송되는 메시지입니다.")
pyautogui.hotkey("ctrl", "v")
time.sleep(1.0)

pyautogui.write(["enter"])
time.sleep(1.0)

pyautogui.write(["escape"])
time.sleep(1.0)