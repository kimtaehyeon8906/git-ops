import win32gui
import win32api
import win32con
import time
import random
import threading
import subprocess
import signal
import sys
from pymemuc import PyMemuc

INSTANCE_NAME = "NMPlayer"
MEMUC_PATH = r"C:\Program Files\Microvirt\MEmu\memuc.exe"
RUNNING = True

def find_memu_main(instance_name):
    try:
        memu_hwnd = win32gui.FindWindow(None, f"({instance_name})")
        if memu_hwnd:
            main_window = win32gui.FindWindowEx(memu_hwnd, None, None, "MainWindowWindow")
            if main_window:
                center_window = win32gui.FindWindowEx(main_window, None, None, "CenterWidgetWindow")
                if center_window:
                    return win32gui.FindWindowEx(center_window, None, None, "RenderWindowWindow")
    except Exception as e:
        print(f"[ERROR] 핸들 탐색 중 오류: {e}")
    return None

def send_key(hwnd, key):
    try:
        win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, ord(key), 0)
        time.sleep(0.02)
        win32api.PostMessage(hwnd, win32con.WM_KEYUP, ord(key), 0)
    except Exception as e:
        print(f"[ERROR] 키 전송 실패 ({key}): {e}")

def get_vm_index_by_name(instance_name):
    try:
        result = subprocess.check_output(f'"{MEMUC_PATH}" listvms', shell=True, encoding="utf-8")
        for line in result.strip().splitlines():
            parts = line.strip().split(",")
            if len(parts) >= 2 and parts[1] == instance_name:
                return int(parts[0])
    except Exception as e:
        print(f"[ERROR] VM 인덱스 조회 실패: {e}")
    return None

def automation_task(hwnd, memuc, instance_name):
    vm_index = get_vm_index_by_name(instance_name)
    if vm_index is None:
        print(f"[ERROR] {instance_name} 인스턴스를 찾을 수 없습니다.")
        return

    loop_count = 0
    print(f"[INFO] 자동화 루프 시작됨 (VM Index: {vm_index})")

    while RUNNING:
        try:
            send_key(hwnd, "Q")
            time.sleep(0.1)
            for _ in range(3):
                send_key(hwnd, "E")
                time.sleep(0.1)

            loop_count += 1
            if loop_count % 6 == 0:
                imei = "".join(str(random.randint(0, 9)) for _ in range(15))
                for attempt in range(3):
                    try:
                        memuc.set_configuration_vm("imei", imei, vm_index, instance_name)
                        break
                    except Exception as e:
                        print(f"[ERROR] IMEI 설정 실패 (시도 {attempt+1}/3): {e}")
                        time.sleep(1)
        except Exception as e:
            print(f"[ERROR] 루프 오류 발생: {e}")
            time.sleep(1)

def handle_exit(signum, frame):
    global RUNNING
    print("\n[INFO] 프로그램 종료 요청됨. 루프 종료 중...")
    RUNNING = False
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, handle_exit)
    signal.signal(signal.SIGTERM, handle_exit)

    hwnd = find_memu_main(INSTANCE_NAME)
    if not hwnd:
        print(f"[ERROR] 창을 찾을 수 없습니다: {INSTANCE_NAME}")
        input("계속하려면 Enter를 누르세요...")
        return

    memuc = PyMemuc()
    print(f"[INFO] {INSTANCE_NAME} 자동화 시작됨")

    automation_thread = threading.Thread(target=automation_task, args=(hwnd, memuc, INSTANCE_NAME), daemon=True)
    automation_thread.start()

    try:
        while RUNNING:
            if not win32gui.IsWindow(hwnd):
                print("[ERROR] 대상 창이 사라졌습니다. 프로그램 종료됨.")
                break
            time.sleep(1)
    except KeyboardInterrupt:
        handle_exit(None, None)

if __name__ == "__main__":
    main()

