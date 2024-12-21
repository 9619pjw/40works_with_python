import pyautogui
import time
import pyperclip

pyautogui.moveTo(191, 289, 0.2)
pyautogui.click()
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("서울 날씨")
pyautogui.hotkey('command', 'v')
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)

st_x = 4
st_y = 336
ed_x = 609
ed_y = 714

#pyautogui.screenshot(r"10. 오토마우스를 활용한 웹페이지 자동화/서울날씨.png", region=(st_x, st_y, ed_x, ed_y))

# 스크린샷 저장 경로 확인
screenshot_path = r'10. Weather with Auto\seoul.png'

# 스크린샷 찍기
pyautogui.screenshot(screenshot_path, region=(st_x, st_y, ed_x-st_x, ed_y-st_y))