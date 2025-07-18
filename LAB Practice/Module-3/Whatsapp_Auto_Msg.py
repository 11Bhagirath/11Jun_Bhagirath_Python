import pyautogui
import time 

Message = "Hi Good Morning!"
count = 2

print("You Have 10 Sec To Open The Whatsapp!")
time.sleep(10)

for i in range(count):
    pyautogui.typewrite(Message)
    pyautogui.press("Enter")
    time.sleep(5)