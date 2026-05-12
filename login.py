import pyautogui
import time

def fazer_login():
    pyautogui.hotkey("ctrl", "l")

    pyautogui.write(
        "https://dlp.hashtagtreinamentos.com/python/intensivao/login",
        interval=0.05
    )

    pyautogui.press("enter")

    time.sleep(5)

    pyautogui.click(x=687, y=409)
    pyautogui.write("pythonimpressionador@gmail.com")

    pyautogui.press("tab")
    pyautogui.write("sua senha")

    pyautogui.press("tab")
    pyautogui.press("enter")
