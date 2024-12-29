import pyautogui
import pyperclip
import time
import schedule
import threading
import os

# 현재 실행 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def send_message():
    threading.Timer(10, send_message).start()
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
    pyautogui.doubleClick(clickPosition.x + 15, clickPosition.y)

    pyperclip.copy("해당 메시지는 사용자 설정 시간에 의해 전송되는 메시지입니다.")
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1.0)

    pyautogui.write(["enter"])
    time.sleep(1.0)


# 매일 16시 20분마다 실행
schedule.every().day.at("16:20").do(send_message(), "매일  16시 20분마다 실행")

# 매주 일요일 16시 30분마다 실행
# schedule.every().sunday.at("16:30").do(send_message())

# 30분마다 실행
# schedule.every(30).minutes.do(send_message())