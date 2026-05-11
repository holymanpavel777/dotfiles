#!/usr/bin/env python3
import time
import sys
import os
import json

# Настройки
WORK_TIME = 25 * 60
BREAK_TIME = 5 * 60
STATE_FILE = "/tmp/pomodoro_state"
# Путь к любому короткому звуку (можешь заменить на свой)
ALERT_SOUND = "/usr/share/sounds/freedesktop/stereo/complete.oga"

def send_notify(title, message):
    os.system(f'notify-send -u critical -i clock "{title}" "{message}"')
    if os.path.exists(ALERT_SOUND):
        os.system(f'mpv --no-video {ALERT_SOUND} > /dev/null 2>&1 &')

def get_status():
    if not os.path.exists(STATE_FILE):
        return {"text": "Ready", "class": "stopped"}

    with open(STATE_FILE, "r") as f:
        data = f.read().split()
        start_time = float(data[0])
        is_break = data[1] == "break" if len(data) > 1 else False

    duration = BREAK_TIME if is_break else WORK_TIME
    elapsed = int(time.time() - start_time)
    remaining = duration - elapsed

    if remaining <= 0:
        if remaining == 0: # Уведомление сработает один раз
            msg = "Перерыв окончен! За работу." if is_break else "Помидор завершен! Отдохни."
            send_notify("Pomodoro", msg)
        
        # Автоматически не переключаем, ждем клика
        return {"text": "󱫐 Done!", "class": "finished"}

    mins, secs = divmod(remaining, 60)
    label = "󱫠" if not is_break else "☕"
    return {
        "text": f"{label} {mins:02d}:{secs:02d}",
        "class": "break" if is_break else "work"
    }

if __name__ == "__main__":
    # Выводим JSON для Waybar
    print(json.dumps(get_status()))
