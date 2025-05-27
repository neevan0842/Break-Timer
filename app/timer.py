# app/timer.py
from PyQt6.QtCore import QTimer


class Timer:
    def __init__(self, overlay, work_duration, break_duration):
        self.overlay = overlay
        self.work_duration = (
            work_duration * 60 * 1000
        )  # Convert minutes to milliseconds
        self.break_duration = break_duration * 60 * 1000
        self.timer = QTimer()
        self.timer.timeout.connect(self.switch_state)
        self.is_work_time = True

    def start(self):
        self.timer.start(self.work_duration)

    def switch_state(self):
        self.is_work_time = not self.is_work_time
        if self.is_work_time:
            self.overlay.color = "green"
            self.timer.start(self.work_duration)
        else:
            self.overlay.color = "red"
            self.timer.start(self.break_duration)
        self.overlay.update()
