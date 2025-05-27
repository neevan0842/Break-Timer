# main.py
import sys
from PyQt6.QtWidgets import QApplication
from app.overlay import Overlay
from app.timer import Timer
from app.config import load_config


def main():
    app = QApplication(sys.argv)
    config = load_config()
    overlay = Overlay("green")
    timer = Timer(overlay, config["work_duration"], config["break_duration"])
    timer.start()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
