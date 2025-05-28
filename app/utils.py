# app/config.py
import json
import os
import psutil
from app.logger import logger

APP_DIR = os.path.dirname(os.path.abspath(__file__))
PID_FILE = os.path.join(APP_DIR, "app.pid")
CONFIG_PATH = os.path.join(APP_DIR, "config.json")


def load_config():
    """Load application configuration from file."""
    if not os.path.exists(CONFIG_PATH):
        return {"work_duration": 25, "break_duration": 5}
    with open(CONFIG_PATH, "r") as file:
        config = json.load(file)
        return config


def save_config(config):
    """Save application configuration to file."""
    with open(CONFIG_PATH, "w") as file:
        json.dump(config, file)
        logger.info(f"Saved config: {config}")


def get_pid():
    """Get the PID of the running application."""
    if not os.path.isfile(PID_FILE):
        logger.debug("No PID file found")
        return None
    with open(PID_FILE, "r") as f:
        pid = int(f.read())
        logger.debug(f"Read PID: {pid}")
        return pid


def set_pid(pid):
    """Set the PID of the running application."""
    with open(PID_FILE, "w") as f:
        f.write(str(pid))


def delete_process():
    """Delete the PID file and terminate the process."""
    pid = get_pid()
    if pid is None:
        logger.error("Application is not running")
        raise RuntimeError("Application is not running.")
    process = psutil.Process(pid)
    process.terminate()
    process.wait(timeout=3)
    os.remove(PID_FILE)
    logger.info(f"Terminated process with PID: {pid}")


def is_process_running():
    """Check if the application process is running."""
    pid = get_pid()
    if pid is None or not psutil.pid_exists(pid):
        logger.debug("Process is not running")
        return None
    logger.debug(f"Process is running with PID: {pid}")
    return pid
