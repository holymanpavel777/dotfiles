import time
import sys
import os

# Простейший флаг-файл для управления состоянием
STATE_FILE = "/tmp/pomodoro_state"

def get_status():
    if not os.path.exists(STATE_FILE):
        return " "
    
    with open(STATE_FILE, "r") as f:
        start_time = float(f.read())
    
    elapsed = int(time.time() - start_time)
    remaining = 25 * 60 - elapsed # 25 минут
    
    if remaining <= 0:
        return "󱫐 Перерыв!"
    
    mins, secs = divmod(remaining, 60)
    return f"󱫠 {mins:02d}:{secs:02d}"

if __name__ == "__main__":
    print(get_status())
