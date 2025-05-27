# app/config.py
import json
import os

import click
import psutil

APP_DIR = os.path.dirname(os.path.abspath(__file__))
PID_FILE = os.path.join(APP_DIR, "app.pid")
CONFIG_PATH = os.path.join(APP_DIR, "config.json")


def load_config():
    if not os.path.exists(CONFIG_PATH):
        return {"work_duration": 25, "break_duration": 5}
    with open(CONFIG_PATH, "r") as file:
        return json.load(file)


def save_config(config):
    with open(CONFIG_PATH, "w") as file:
        json.dump(config, file)


def get_pid():
    """Get the PID of the running application."""
    if not os.path.isfile(PID_FILE):
        return None
    with open(PID_FILE, "r") as f:
        return int(f.read())


def set_pid(pid):
    """Set the PID of the running application."""
    with open(PID_FILE, "w") as f:
        f.write(str(pid))


def delete_process():
    """Delete the PID file."""
    pid = get_pid()
    if pid is None:
        click.echo("Application is not running.")
        return
    process = psutil.Process(pid)
    process.terminate()
    process.wait(timeout=3)
    os.remove(PID_FILE)


def is_process_running():
    """Check if the application process is running."""
    pid = get_pid()
    if pid is None or not psutil.pid_exists(pid):
        return None
    return pid
