from Alarm import Alarm
from dotenv import set_key
from pathlib import Path
import os


def set_auto_save(t: str) -> str:
    if t in ("y", "n"):
        set_key(Path('.env'), 'ALARM_AUTOSAVE', t)
    return f"Alarm auto start set to {t}"

def boot_auto_save() -> None:
    ALARM_AUTOSAVE = str(os.getenv("ALARM_AUTOSAVE", "y"))
    if ALARM_AUTOSAVE == "y":
        alarm_manager.boot_auto_save()

def set_auto_start(t: str) -> str:
    if t in ("y", "n"):
        set_key(Path('.env'), 'ALARM_AUTOSTART', t)
    return f"Alarm auto start set to {t}"

def boot_auto_start() -> None:
    ALARM_AUTOSTART = str(os.getenv("ALARM_AUTOSTART", "y"))
    if ALARM_AUTOSTART == "y":
        alarm_manager.start_all_alarms()

def load_alarms() -> str:
    return alarm_manager.load_alarms()

def add_alarm(alarm: Alarm.Alarm = None, **kwargs) -> str: # type: ignore
    if alarm is not None:
        a = alarm_manager.add_alarm(alarm)
    else:
        a = alarm_manager.add_alarm(**kwargs)

    return a.title if a else "ERROR"

def start_alarm(name: str) -> str:
    return alarm_manager.start_alarm(name)

def start_all_alarms() -> list[str]:
    return alarm_manager.start_all_alarms()

def clear_all_alarms() -> str:
    return alarm_manager.clear_all_alarms()

def clear_alarm(name: str) -> str:
    return alarm_manager.clear_alarm(name)

def list_alarms() -> list[dict]:
    return [a.to_json() for a in alarm_manager.list_alarms()]



alarm_manager = Alarm.AlarmManager()
boot_auto_start()
boot_auto_save()
