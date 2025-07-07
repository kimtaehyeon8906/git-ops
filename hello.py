import win32gui
import win32api
import win32con
import time
import random
import threading
from pymemuc import PyMemuc

def find_memu_main():
    memu_hwnd = win32gui.FindWindow(None, "(NMPlayer)")
    if memu_hwnd:
        main_window = win32gui.FindWindowEx(memu_hwnd, None, None, "MainWindowWindow")
        if main_window:
            center_window = win32gui.FindWindowEx(main_window, None, None, "CenterWidgetWindow")
            if center_window:
                return win32gui.FindWindowEx(center_window, None, None, "RenderWindowWindow")
    return None

def send_text(hwnd, text):
    for char in text:
        win32api.PostMessage(hwnd, win32con.WM_CHAR, ord(char), 0)

def send_key(hwnd, key):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, ord(key), 0)
    time.sleep(0.05)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, ord(key), 0)

def click(hwnd, x, y):
    lParam = (y << 16) | x
    win32api.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32api.PostMessage(hwnd, win32con.WM_LBUTTONUP, None, lParam)

def automation_task(hwnd, memuc, nickname):
    while True:
        success = memuc.set_configuration_vm("imei", "".join(str(random.randint(0, 9)) for _ in range(15)), 0, "NMPlayer")
        if not success:
            break
        
        for _ in range(7):
            for key in "BOK":
                send_key(hwnd, key)
                time.sleep(0.2)

            time.sleep(0.05)
            memuc.input_text_vm(nickname, 0, "NMPlayer")
            time.sleep(0.05)
            click(hwnd, 683, 311)
            time.sleep(0.05)
            send_key(hwnd, "O")
            time.sleep(0.05)
            send_key(hwnd, "O")
            time.sleep(0.05)

    print("Done")

def main():
    hwnd = find_memu_main()
    if not hwnd:
        print("MEmu 창을 찾을 수 없습니다.")
        return

    memuc = PyMemuc()

    nickname = input("원하는 닉네임을 입력하세요: ")

    automation_thread = threading.Thread(target=automation_task, args=(hwnd, memuc, nickname), daemon=True)
    automation_thread.start()

    while automation_thread.is_alive():
        time.sleep(1)

if __name__ == "__main__":
    main()

