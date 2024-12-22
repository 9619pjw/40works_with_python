import pyautogui
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