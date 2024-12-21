import pyautogui
import time
import pyperclip
pyautogui.PAUSE = 0.5

pyautogui.moveTo(191, 289, 0.2)
pyautogui.click()
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("서울 날씨")
pyautogui.hotkey('command', 'v')
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)
