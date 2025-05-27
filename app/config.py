# app/config.py
import json
import os

CONFIG_PATH = "config.json"


def load_config():
    if not os.path.exists(CONFIG_PATH):
        return {"work_duration": 25, "break_duration": 5}
    with open(CONFIG_PATH, "r") as file:
        return json.load(file)


def save_config(config):
    with open(CONFIG_PATH, "w") as file:
        json.dump(config, file)
